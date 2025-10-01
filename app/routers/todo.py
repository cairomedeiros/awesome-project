from fastapi import APIRouter

router = APIRouter()

@router.get("/todos/", tags=["todo"])
async def get_todos():
    return [{"todo": "write test"}, {"todo": "delete folders"}]