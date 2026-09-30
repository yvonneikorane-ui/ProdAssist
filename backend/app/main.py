from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from .analysis import analyze_record
from .config import settings
from .database import (
    Base,
    SessionLocal,
    engine,
    get_db,
)
from .models import HumanDecision, ProductionRecord
from .schemas import (
    AnalysisResult,
    DecisionCreate,
    DecisionOut,
    ProductionRecordOut,
)
from .seed import seed_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        seed_database(db)

    yield


app = FastAPI(
    title="ProdAssist API",
    version="1.0.0",
    description=(
        "Human-in-the-loop digital assistance "
        "demonstrator for production management."
    ),
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health(
    db: Session = Depends(get_db),
) -> dict[str, str]:

    try:
        db.execute(select(1))
        return {
            "status": "ok",
            "database": "connected",
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )

@app.get(
    "/api/production",
    response_model=list[ProductionRecordOut],
)
def list_production(
    machine_id: str | None = Query(default=None),
    db: Session = Depends(get_db),
) -> list[ProductionRecord]:

    statement = select(ProductionRecord).order_by(
        ProductionRecord.timestamp.desc()
    )

    if machine_id:
        statement = statement.where(
            ProductionRecord.machine_id == machine_id
        )

    return list(db.scalars(statement).all())


@app.get(
    "/api/production/{production_id}",
    response_model=ProductionRecordOut,
)
def get_production(
    production_id: str,
    db: Session = Depends(get_db),
) -> ProductionRecord:

    record = db.get(
        ProductionRecord,
        production_id,
    )

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Production record not found",
        )

    return record


@app.get(
    "/api/production/{production_id}/analysis",
    response_model=AnalysisResult,
)
def get_analysis(
    production_id: str,
    db: Session = Depends(get_db),
) -> AnalysisResult:

    record = db.get(
        ProductionRecord,
        production_id,
    )

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Production record not found",
        )

    result = analyze_record(record)

    return AnalysisResult(
        production_id=production_id,
        **result.__dict__,
    )


@app.post(
    "/api/decisions",
    response_model=DecisionOut,
    status_code=201,
)
def create_decision(
    payload: DecisionCreate,
    db: Session = Depends(get_db),
) -> HumanDecision:

    if db.get(
        ProductionRecord,
        payload.production_id,
    ) is None:

        raise HTTPException(
            status_code=404,
            detail="Production record not found",
        )

    decision = HumanDecision(
        **payload.model_dump()
    )

    db.add(decision)
    db.commit()
    db.refresh(decision)

    return decision


@app.get(
    "/api/decisions/{production_id}",
    response_model=list[DecisionOut],
)
def list_decisions(
    production_id: str,
    db: Session = Depends(get_db),
) -> list[HumanDecision]:

    statement = (
        select(HumanDecision)
        .where(
            HumanDecision.production_id
            == production_id
        )
        .order_by(
            HumanDecision.created_at.desc()
        )
    )

    return list(
        db.scalars(statement).all()
    )
