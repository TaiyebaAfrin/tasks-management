from django.contrib import admin
from django.urls import path, include
from tasks.views import home, contact  # Assuming your view is in tasks/views.py


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  # Make sure the URL is correct
    path("contact/", contact),

    path("tasks/", include("tasks.urls")),
]
