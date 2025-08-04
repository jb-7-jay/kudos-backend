from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


from .views import RegisterView, UserDetailsView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", UserDetailsView.as_view(), name="user-details"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
