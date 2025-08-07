from django.urls import path
from .views import RegisterView, UserDetailsView, CustomTokenObtainPairView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", UserDetailsView.as_view(), name="user-details"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
