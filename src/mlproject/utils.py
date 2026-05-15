import os
import sys

import pandas as pd
import pymysql
from dotenv import load_dotenv

from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
            )
        
        logging.info("Connection Established",mydb)
        
        df = pd.read_sql_query("SELECT * FROM students", mydb)
        return df
    
    except Exception as e:
        raise CustomException(e, sys)