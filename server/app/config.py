import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger(__name__)

# Here, we defined a Settings class with two attributes:


# environment - defines the environment (i.e., dev, stage, prod)
# testing - defines whether or not we're in test mode
# BaseSettings, from Pydantic, validates the data so that when
# we create an instance of Settings, environment and testing
# will have types of str and bool, respectively.
class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


# Essentially, get_settings gets called for each request. If we refactored
# the config so that the settings were read from a file, instead of from
# environment variables, it would be much too slow.
# We're using lru_cache to cache the settings so get_settings is only called once.
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment")
    return Settings()