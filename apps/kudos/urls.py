from django.urls import path
from .views import KudosCreateView

urlpatterns = [path("create/", view=KudosCreateView.as_view(), name="create-kudos")]
