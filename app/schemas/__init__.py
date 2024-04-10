from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class IpType(Enum):
    LOCALHOST = "LOCALHOST"
    REMOTE = "REMOTE"

class AddIpNameItem(BaseModel):
    ip_type: Optional[IpType] = IpType.LOCALHOST
