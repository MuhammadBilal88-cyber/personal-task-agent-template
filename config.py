import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "llama-3.3-70b-versatile"
MAX_TOKENS = 4096
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MAX_ITERATIONS = 10
LOG_DIR = "logs"

# Tools that run WITHOUT asking for approval (read-only)
AUTO_APPROVE = [
    "research_topic",   # Read-only – safe
    "save_draft",       # Read-only – safe
]

# publish_post is NOT in AUTO_APPROVE → will always ask for approval