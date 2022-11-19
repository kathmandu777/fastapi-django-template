from fastapi import APIRouter, Request

health_router = APIRouter()


@health_router.get("/")
async def get(request: Request) -> dict[str, str]:
    return {"status": "ok"}
