Analytics Dashboard (Django + REST API + Chart.js)

- A Django-based analytics dashboard that visualizes site activity through interactive charts using Chart.js, logs activity via a REST API, and allows data export to CSV — all accessible directly from the Django Admin panel.

#Features

- Admin Dashboard with Charts:
Visualizes SiteActivity data for the past 7 days using Chart.js directly inside the Django admin interface.

- REST API for Activity Logging:
Uses Django REST Framework (DRF) to log and retrieve site activity data (e.g., page visits, events).

- Time-Based Analytics:
Tracks activity by date, letting you monitor trends and engagement patterns.

- CSV Export Support (coming soon):
Enables admin users to export analytics reports for offline analysis.

#Future Plans:

- Track login/logout and page visits automatically using Django signals or middleware.

- Add frontend charts with filters for dynamic date ranges.

- Integrate real-time updates via WebSockets (Django Channels).

#Dashboard Preview

- The admin dashboard displays a 7-day activity trend line chart representing logged site events.