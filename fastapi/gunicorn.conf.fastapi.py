# WIP: for development
wsgi_app = "config.asgi:fastapi_app"
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:8000"
workers = 1
daemon = True
