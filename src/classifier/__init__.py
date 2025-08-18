import os
import sys
import logging

# the logging format
logging_format = "[%(asctime)s | %(levelname)s | %(filename)s: line %(lineno)d] %(message)s"

# creating the logging directory and file 
log_dir = "logs" 
log_filepath = os.path.join(log_dir, 'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('cnnClassifierLogger')