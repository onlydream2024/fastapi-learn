import os
from loguru import logger
from pydantic_settings import BaseSettings

class SharedConfigs(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV")

class DevConfigs(SharedConfigs):
    pass

class StageConfigs(SharedConfigs):
    pass

class ProdConfigs(SharedConfigs):
    pass

if str(os.getenv("ENVIRONMENT")).upper() == "PROD":
    configs = ProdConfigs()
elif str(os.getenv("ENVIRONMENT")).upper() == "STAGE":
    configs = StageConfigs()
else:
    configs = DevConfigs()
    
logger.info("ENVIRONMENT: " + str(os.getenv("ENVIRONMENT", "DEV").upper()))
