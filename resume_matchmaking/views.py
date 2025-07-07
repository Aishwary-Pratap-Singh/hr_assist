
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .agent_workflow.agent_service import get_all_resume_text_as_string, get_jd_text_as_string, call_agent
import PyPDF2

def health(request):
    return JsonResponse({"status": "ok"})

def extract_pdf_text(file_obj):
    """
    Extracts text from a PDF file object.
    """
    reader = PyPDF2.PdfReader(file_obj)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

@method_decorator(csrf_exempt, name='dispatch')
class JDUploadView(View):
    """
    API endpoint that allows users to upload a Job Description (JD) as a PDF file.

    Methods
    -------
    post(request):
        Handles POST requests with a PDF file uploaded under the 'jd' key.
        Returns a JSON response with the file path if successful, or an error message.
    """
    def post(self, request):
        """
        Handle POST request to upload a JD PDF file.

        Parameters
        ----------
        request : HttpRequest
            The HTTP request object containing the uploaded file.

        Returns
        -------
        JsonResponse
            JSON response indicating success or failure, and the file path if successful.
        """
        jd_file = request.FILES.get('jd')
        if not jd_file:
            return JsonResponse({'error': 'No file uploaded.'}, status=400)

        if not jd_file.name.lower().endswith('.pdf'):
            return JsonResponse({'error': 'Only PDF files are allowed.'}, status=400)

        # Save the file (optional: customize storage location)
        file_path = default_storage.save(f'uploads/jd/{jd_file.name}', ContentFile(jd_file.read()))

        # Here you can add PDF processing logic if needed

        return JsonResponse({'message': 'JD PDF uploaded successfully.', 'file_path': file_path}, status=201)
    

@method_decorator(csrf_exempt, name='dispatch')
class ResumeUploadView(View):
    """
    API endpoint that allows users to upload a candidate's resume as a PDF file.

    Methods
    -------
    post(request):
        Handles POST requests with a PDF file uploaded under the 'resume' key.
        Returns a JSON response with the file path if successful, or an error message.
    """
    def post(self, request):
        """
        Handle POST request to upload a candidate resume PDF file.

        Parameters
        ----------
        request : HttpRequest
            The HTTP request object containing the uploaded file.

        Returns
        -------
        JsonResponse
            JSON response indicating success or failure, and the file path if successful.
        """
        resume_file = request.FILES.get('resume')
        if not resume_file:
            return JsonResponse({'error': 'No file uploaded.'}, status=400)

        if not resume_file.name.lower().endswith('.pdf'):
            return JsonResponse({'error': 'Only PDF files are allowed.'}, status=400)

        # Save the file in 'uploads/candidate_resumes/' directory
        file_path = default_storage.save(f'uploads/candidate_resumes/{resume_file.name}', ContentFile(resume_file.read()))

        # Here you can add PDF processing logic if needed

        return JsonResponse({'message': 'Resume PDF uploaded successfully.', 'file_path': file_path}, status=201)
    

@method_decorator(csrf_exempt, name='dispatch')
class ListResumesView(View):
    def get(self, request):
        """
        API endpoint to list all resume files in the candidate_resumes folder.
        Returns a JSON response with the list of file names.
        """
        print("Listing resumes...")
        call_agent()
        return JsonResponse({'message': 'Resume fetched successfully.'}, status=200)
