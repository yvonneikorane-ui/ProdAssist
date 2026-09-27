import os

os.environ[
    "DATABASE_URL"
] = "sqlite+pysqlite:///:memory:"

from app.main import app


def test_api_application_exists():
    assert app.title == "ProdAssist API"
