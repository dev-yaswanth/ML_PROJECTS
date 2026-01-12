import logging
import os
from datetime import datetime

# Log file name
LOG_FILE = f"Log_{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
# log files naming convention = Log_01_12_26_11_05_30.log
# strftime converts a date/time into a formatted string. str → string ,f → format,time → date & time

# Logs directory (ONLY folder)
logs_path = os.path.join(os.getcwd(), "Logs", datetime.now().strftime("%d_%m_%Y"))
# logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) # instead of  LOG_FILE we can pass date so that we can save files in different folders

# C:\ML_PROJECT\logs

os.makedirs(
    logs_path, exist_ok=True
)  # exist_ok to override if file or path exists --Create logs folder if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# C:\ML_PROJECT\logs\01_12_26_11_05_30.log


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    # Testing
    logging.info("Logging system initialized")
    logging.warning("This is a warning")
    logging.error("This is an error")
