from django.contrib import admin
# from django.urls import path
# from django.shortcuts import render
from .models import SiteActivity 
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

# Register your models here.
@admin.register(SiteActivity)
class SiteActivityAdmin( admin.ModelAdmin):
    change_list_template = "admin/dashboard.html"
    
    def changelist_view(self, request, extra_context = None):
        #Prepare data for Chart.js
        today = timezone.now()
        last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
        labels = [d.strftime("%b %d") for d in last_7_days]

        data = []
        for day in last_7_days:
            count = SiteActivity.objects.filter(
                created_at__date=day.date()
            ).count()
            data.append(count)

        extra_context = extra_context or {}
        extra_context['chart_labels'] = labels
        extra_context['chart_data'] = data

        return super().changelist_view(request, extra_context)



