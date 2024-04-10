
from fastapi import Request

def get_request_ip(request: Request) -> str:
    client_ip = request.client.host
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        splitted_forwarded_for = forwarded_for.split(",")
        if (splitted_forwarded_for):
            client_ip = forwarded_for.split(",")[0]
    return client_ip
