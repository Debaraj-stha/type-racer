from django.urls import path
from django.contrib.auth import views as auth_views


from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("race",race,name="race"),
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_conform.html"),name="password_reset_confirm"),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('accounts/login/',login,name="login")
]

handler404='app.views.handler404'