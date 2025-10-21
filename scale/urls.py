from django.urls import path
from . import views

urlpatterns = [
path('dashboard/',views.activity_dashboard, name='activity_dashboard' ),
path('csv_export/', views.export_site_activity_csv, name='export_csv'),
]