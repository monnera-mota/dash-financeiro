#%%
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("wh_USER")
DB_PASSWORD = os.getenv("wh_PASSWORD")
DB_HOST = os.getenv("wh_HOST")
DB_PORT = os.getenv("wh_PORT")
DB_NAME = os.getenv("wh_NAME")
conn_wh = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")