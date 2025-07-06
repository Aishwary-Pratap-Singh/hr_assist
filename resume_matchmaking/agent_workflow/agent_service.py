# from dotenv import load_dotenv
# from agents import Agent, Runner, trace, function_tool
# from openai.types.responses import ResponseTextDeltaEvent
# from typing import Dict
# import sendgrid
# from sendgrid.helpers.mail import Mail, Email, To, Content
# import asyncio


import os
import json
from django.conf import settings
import PyPDF2

# def list_resume_files():
#     """
#     Returns a list of absolute file paths for all resumes in the candidate_resumes folder.
#     """
#     print("Listing resumes service...")
#     resumes_dir = os.path.join(settings.MEDIA_ROOT, "uploads", "candidate_resumes")
#     if not os.path.exists(resumes_dir):
#         return []
#     print(f"Resumes directory: {resumes_dir}")
#     # Only include files (not directories) and filter for PDFs
#     resumes = [
#         os.path.join(resumes_dir, f)
#         for f in os.listdir(resumes_dir)
#         if os.path.isfile(os.path.join(resumes_dir, f)) and f.lower().endswith('.pdf')
#     ]
#     print(resumes)
#     return resumes


def get_resume_directory():
    """
    Constructs and returns the absolute path to the resume directory.
    """
    return os.path.join(settings.MEDIA_ROOT, "uploads", "candidate_resumes")

def get_jd_directory():
    """
    Constructs and returns the absolute path to the jd directory.
    """
    return os.path.join(settings.MEDIA_ROOT, "uploads", "jd")

def get_pdf_files(directory_path):
    """
    Returns a list of full paths to .pdf files in the given directory.
    """
    if not os.path.exists(directory_path):
        return []

    return [
        os.path.join(directory_path, f)
        for f in os.listdir(directory_path)
        if os.path.isfile(os.path.join(directory_path, f)) and f.lower().endswith('.pdf')
    ]

def extract_pdf_text(file_path):
    """
    Extracts text from a PDF file path.
    """
    text = ""
    try:
        with open(file_path, "rb") as file_obj:
            reader = PyPDF2.PdfReader(file_obj)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        text = f"[Error reading {file_path}: {str(e)}]"
    return text

def build_resume_text_dict(file_paths):
    """
    Given a list of file paths, builds a dictionary {filename: extracted_text}.
    """
    return {
        os.path.basename(path): extract_pdf_text(path)
        for path in file_paths
    }

def get_all_resume_text_as_string():
    """
    Main function to get all resume text content as a JSON-formatted string.
    """
    directory = get_resume_directory()
    pdf_files = get_pdf_files(directory)
    resume_text_dict = build_resume_text_dict(pdf_files)
    print(resume_text_dict)
    return resume_text_dict
    # return json.dumps({"result": resume_text_dict})