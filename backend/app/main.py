import uvicorn
from dotenv import load_dotenv
from app.fastapi import app
import os


load_dotenv()

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
