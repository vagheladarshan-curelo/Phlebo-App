import logging
import sys
from pydantic import ValidationError
from .config import settings

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Suppress redundant logging from libraries if needed
    # logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
