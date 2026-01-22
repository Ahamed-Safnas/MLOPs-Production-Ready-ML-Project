# import logging
# import os

# from from_root import from_root
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log_dir = 'logs'

# logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# # os.makedirs(log_dir, exist_ok=True)
# os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# logging.basicConfig(
#     filename=logs_path,
#     format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG,force=True
# )

import logging
import os
from datetime import datetime

 #this used to create path from root directory(local disk C)
# from from_root import from_root 

BASE_DIR = os.getcwd()
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = "logs"

 #this used to create path from root directory(local disk C)
# logs_path = os.path.join(from_root(), log_dir, LOG_FILE)


logs_path = os.path.join(BASE_DIR, log_dir, LOG_FILE)
# Create correct directory
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    force=True
)

# logger = logging.getLogger("us_visa_logger")

# print("LOGGER INITIALIZED AT:", logs_path)   # DEBUG LINE — REMOVE LATER
