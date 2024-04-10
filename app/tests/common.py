import os
import sys
from fastapi.testclient import TestClient

WORKDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(WORKDIR)

from app.main import app

test_client = TestClient(app)
