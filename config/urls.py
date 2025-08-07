from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("apps.users.urls")),
    path("api/organizations/", include("apps.organizations.urls")),
    path("api/kudos/", include("apps.kudos.urls")),
]
