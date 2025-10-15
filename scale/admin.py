import csv
from .models import SiteActivity 
from django.contrib import admin
from django_admin_charts.admin import AdminChartMixin

# Register your models here.
@admin.register(SiteActivity)
class SiteActivityAdmin(AdminChartMixin, admin.ModelAdmin):
    change_list_template = "admin/analytics_dashboard.html"
    list_display = ('event_type', 'page_url', 'user_ip', 'created_at')
    chart_title = 'Activity Overview'
    chart_model = SiteActivity
    chart_date_field = 'created_at'
    chart_aggregate_field = 'id'
    chart_aggregate_func = 'count'
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attchment; filename="site_activities.csv"'
        writer = csv.writer(response)
        writer.writerow(['Event Type', 'Page URL', 'User Agent', 'Created At'])
        for obj in queryset:
            writer.writerow([obj.event_type, obj.page_url, obj.user_ip, obj.user_agent, obj.created_at])
        return response

    export_as_csv.short_description = "Eport Selected as CSV"


