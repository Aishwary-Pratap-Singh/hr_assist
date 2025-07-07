import os
from django.conf import settings
import PyPDF2
from .agent import run_agent

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

def get_jd_text_as_string():
    """
    Main function to get all jd text content as a JSON-formatted string.
    """
    directory = get_jd_directory()
    pdf_files = get_pdf_files(directory)
    jd_text_dict = build_resume_text_dict(pdf_files)
    print(jd_text_dict)
    return jd_text_dict

def call_agent():
    resume = get_all_resume_text_as_string()
    jd = get_jd_text_as_string()
    print("resume: ", resume, "\n jd: ", jd)
    return run_agent(resume, jd)

    