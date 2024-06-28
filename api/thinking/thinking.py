from fastapi import APIRouter
from pydantic import BaseModel

from core.gpt import create_thinking


think_router = APIRouter(prefix='/thinking')


class ThinkReq(BaseModel):
    negative: str

class ThinkResp(BaseModel):
    thinking: str

@think_router.post("/")
async def think(req: ThinkReq) -> ThinkResp:
    return ThinkResp(thinking=create_thinking(req.negative))
