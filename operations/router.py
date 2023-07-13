from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session

router = APIRouter(
    prefix='/operations',
    tags=['Operations']
)

@router.get('/')
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    return 'work with BD'