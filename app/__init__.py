# app/__init__.py

# Import key functions to make them available at the package level
from app.qa_pipeline import run_qa_pipeline
from app.utils import clean_response, final_response_logic

# Define what gets imported with "from app import *"
__all__ = ['run_qa_pipeline', 'clean_response', 'final_response_logic']