# from us_visa.logger import logging

# logging.info("hey, welcome to our custom log ")


from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URL_KEY = os.getenv("MONGODB_URL")
print(f"MONGODB_URL_KEY: {MONGODB_URL_KEY}")