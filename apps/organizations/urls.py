from django.urls import path
from .views import OrganizationUsersView

urlpatterns = [
    path("org-users/", OrganizationUsersView.as_view(), name="organization-users"),
]
