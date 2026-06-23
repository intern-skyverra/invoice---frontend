import os

# Project Root Folder
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

# Database Folder
DATABASE_DIR = os.path.join(
    BASE_DIR,
    "database"
)

# Create database folder automatically
os.makedirs(
    DATABASE_DIR,
    exist_ok=True
)

# Database File Path
DATABASE_PATH = os.path.join(
    DATABASE_DIR,
    "skyverra.db"
)