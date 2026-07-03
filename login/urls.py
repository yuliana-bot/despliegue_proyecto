from django.urls import path
from login.views import LoginFormView, LogoutFormView

app_name = 'login'

urlpatterns = [
    path('', LoginFormView.as_view(), name='inicio'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
]