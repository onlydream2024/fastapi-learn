from fastapi import status
from loguru import logger

from common import test_client

def test_get_ip():
    response = test_client.get("/api/ip")
    assert response.status_code == status.HTTP_200_OK
    logger.debug(response.json())

def test_add_ip_name():
    response = test_client.post("/api/ip/yours",
        headers={},
        json={},
    )
    assert response.status_code == status.HTTP_200_OK
    logger.debug(response.json())
