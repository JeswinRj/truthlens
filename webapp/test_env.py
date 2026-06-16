from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("GOOGLE_FACTCHECK_API_KEY"))