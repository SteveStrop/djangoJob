from . import views
from django.urls import path

urlpatterns = [
        path('', views.IndexListView.as_view(), name='index'),
        path('job/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),
        path('test-create', views.test_create, name='test-create'),
path('job/<int:pk>/edit/', views.job_form, name='job-form'),
]
