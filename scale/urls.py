from django.urls import path
from .views import SiteActivityCreateView

urlpatterns = [
    path('activity/', SiteActivityCreateView.as_view(), name='create-activity'),
]