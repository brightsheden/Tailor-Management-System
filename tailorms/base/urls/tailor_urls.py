from django.urls import path
from base.views import tailor_views as views

urlpatterns = [
    path('', views.getTailor, name='get_tailor'),
    path('available-work/', views.allAvailableWork, name='all_available_work'),
    path('job-done/', views.AllJobDone, name='all_job_done'),
    path('pending-job/', views.AllPendingJob, name='all_pending_job'),
    path('work/<int:pk>/edit/', views.editWork, name='edit_work'),
]
