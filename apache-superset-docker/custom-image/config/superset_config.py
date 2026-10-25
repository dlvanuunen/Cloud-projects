# config/superset_config.py
import os
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://superset:{os.environ.get('SUPERSET_DB_PASSWORD')}"
    f"@superset-db:5432/superset"
)
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": "superset-redis",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 1,
}


class CeleryConfig:
    broker_url = "redis://superset-redis:6379/0"
    result_backend = "redis://superset-redis:6379/0"


CELERY_CONFIG = CeleryConfig
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
}
