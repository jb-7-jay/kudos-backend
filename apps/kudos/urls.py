from django.urls import path
from .views import KudosCreateView, KudosActivityView

urlpatterns = [
    path("create/", view=KudosCreateView.as_view(), name="create-kudos"),
    path("activity/", view=KudosActivityView.as_view(), name="kudos-activity"),
]
