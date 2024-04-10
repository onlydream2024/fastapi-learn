from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from loguru import logger

from app import dependencies
from app import schemas

router = APIRouter()

@router.get("/ip")
async def get_ip(ip: str=Depends(dependencies.get_request_ip)):
    return ip

@router.post("/ip/{ip_name}")
def add_ip_name(ip_name: str, body: schemas.AddIpNameItem, ip: str=Depends(dependencies.get_request_ip)):
    return JSONResponse(
        { 
            "name": ip_name, 
            "type": body.ip_type.value, 
            "ip": ip,
        },
        status_code=status.HTTP_200_OK,
    )
