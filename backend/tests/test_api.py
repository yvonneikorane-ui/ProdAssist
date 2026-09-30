import os

os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"

from app.main import app


def test_api_application_exists():
    assert app.title == "ProdAssist API"


def test_health_endpoint_exists():
    routes = {
        route.path
        for route in app.routes
    }

    assert "/api/health" in routes


def test_production_endpoint_exists():
    routes = {
        route.path
        for route in app.routes
    }

    assert "/api/production" in routes
