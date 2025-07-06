from django.urls import path
from .views import health, JDUploadView, ResumeUploadView, ListResumesView

urlpatterns = [
    path('health/', health, name='health'),
    path('upload-jd/', JDUploadView.as_view(), name='upload_jd'),
    path('upload-resume/', ResumeUploadView.as_view(), name='upload_resume'),
    path('list-resumes/', ListResumesView.as_view(), name='list_resumes'),


]