from django.urls import path
from .views import health, JDUploadView, ResumeUploadView

urlpatterns = [
    path('health/', health, name='health'),
    path('upload-jd/', JDUploadView.as_view(), name='upload_jd'),
    path('upload-resume/', ResumeUploadView.as_view(), name='upload_resume'),

]