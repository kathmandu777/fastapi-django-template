from os import environ as env

LOG_HANDLER_LEVEL = env.get("LOG_HANDLER_LEVEL", "DEBUG")
LOG_HANDLER_LEVEL_NULL = env.get("LOG_HANDLER_LEVEL_NULL", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_CONSOLE = env.get("LOG_HANDLER_LEVEL_CONSOLE", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_FILE = env.get("LOG_HANDLER_LEVEL_FILE", LOG_HANDLER_LEVEL)
LOG_HANDLER_FILE_PATH = env.get("LOG_HANDLER_FILE_PATH", "fastapi.log")
LOG_LOGGER_LEVEL = env.get("LOG_LOGGER_LEVEL", "DEBUG")
LOG_FILE_MAX_BYTES = int(env.get("LOG_FILE_MAX_BYTES", 1024 * 1024))
LOG_FILE_BACKUP_COUNT = int(env.get("LOG_FILE_BACKUP_COUNT", 5))


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d "%(message)s"'
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {},
    "handlers": {
        "null": {
            "level": LOG_HANDLER_LEVEL_NULL,
            "class": "logging.NullHandler",
        },
        "console": {
            "level": LOG_HANDLER_LEVEL_CONSOLE,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "level": LOG_HANDLER_LEVEL_FILE,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_HANDLER_FILE_PATH,
            "formatter": "verbose",
            "maxBytes": LOG_FILE_MAX_BYTES,
            "backupCount": LOG_FILE_BACKUP_COUNT,
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "WARNING",
        },
        "uvicorn": {
            "handlers": ["file", "console"],
            "level": "WARNING",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["null"],
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["file", "console"],
            "level": "WARNING",
            "propagate": False,
        },
        "django": {
            "handlers": ["file"],
            "level": "WARNING",  # DEBUGにするとSQLログが出力される
            "propagate": False,
        },
        "django.security.csrf": {
            "handlers": ["file", "console"],
            "level": "WARNING",
            "propagate": False,
        },
        "config": {
            "handlers": ["file"],
            "level": LOG_LOGGER_LEVEL,
            "propagate": False,
        },
        "app": {
            "handlers": ["file"],
            "level": LOG_LOGGER_LEVEL,
            "propagate": False,
        },
    },
}
