from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .forms import ActivityFilterForm 
from .models import SiteActivity
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import TruncDate
from django.db.models import Count
import csv
from django.http import HttpResponse
# from .serializers import SiteActivitySerializer

# Create your views here.
@api_view(['POST'])
def create_activity(request):
    if request.method == 'POST':
        #log the activity
        return Response({'message': 'Activity logged'})
    
def activity_dashboard(request):
    form = ActivityFilterForm(request.GET or None)
    activities = SiteActivity.objects.all()

    #Get current time for fallback
    today = timezone.now()
    default_start = today - timedelta(days=6)

    #Default range: last 7 days
    start_date = default_start.date()
    end_date = today.date()

    #Update if user provided custom dates
    if form.is_valid():
       if form.cleaned_data.get('start_date'):
           start_date = form.cleaned_data['start_date']
       if form.cleaned_data.get('end_date'):
           end_date = form.cleaned_data['end_date']

           #Apply filters to activities
           activities = activities.filter(
               created_at__range=[start_date, end_date]
           )

     #Group by date and count
    daily_counts = (
        activities
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(total=Count('id'))
        .order_by('day')
    )

    # Prepare chart labels and data
    labels = []
    data = []

    # fill in missing dates too
    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    daily_dict = {entry['day']: entry['total'] for entry in daily_counts}

    for d in date_range:
        labels.append(d.strftime("%b %d"))
        data.append(daily_dict.get(d, 0))  # 0 if no activity that day

    context = {
        'form': form,
        'chart_labels': labels,
        'chart_data': data,
    }
    return render(request, 'frontend/activity_dashboard.html', context)

# analytics/views.py
def export_site_activity_csv(request):
    # Create the HTTP response with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="site_activity.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    writer.writerow(['Event Type', 'Page URL', 'User IP', 'User Agent', 'Created At'])

    # Fetch all activity data
    activities = SiteActivity.objects.all().order_by('-created_at')

    # Write each row
    for activity in activities:
        writer.writerow([
            activity.event_type,
            activity.page_url,
            activity.user_ip,
            activity.user_agent,
            activity.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    return response
