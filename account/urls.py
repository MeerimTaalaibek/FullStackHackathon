# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path('register/', RegisterView.as_view()),
#     path('activate/<str:activation_code>/', ActivateView.as_view(), name='activation_code'),
#     path('login/', LoginApiView.as_view()),
#     path('logout/', LogoutView.as_view()),
#
# ]
#

from django.urls import path

from . import views
from .views import PassResetApiView, NewPasswordApiView

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view(), name='activation_code'),
    path('pass_reset/', PassResetApiView.as_view()),
    path('new_password/', NewPasswordApiView.as_view()),
]
