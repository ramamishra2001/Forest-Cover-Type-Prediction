import logging
import os
import datetime

Log_name=f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
Log_path=os.path.join(os.getcwd(),"logs",Log_name)

os.makedirs(os.path.dirname(Log_path),exist_ok=True)

logging.basicConfig(
    filename=Log_path,
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

if __name__=="__main__":
    logging.info("This is an information log")
    logging.warning("This is a warning log")
    logging.error("This is an error log")
    logging.critical("This is a critical log")