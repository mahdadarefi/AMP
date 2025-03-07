from django.urls import path
from . import views

from rest_framework.authtoken import views as auth_token




app_name='accounts'
urlpatterns=[

    path('register/',views.UserRegister.as_view(),name='register'),
    path('api-token-auth/',auth_token.obtain_auth_token),
    path('login/', views.UserLogin.as_view(), name='user_login'),

]


