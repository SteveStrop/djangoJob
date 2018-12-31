from . import views
from django.urls import path

urlpatterns = [
        path('', views.IndexListView.as_view(), name='index'),
        path('job/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),
]
