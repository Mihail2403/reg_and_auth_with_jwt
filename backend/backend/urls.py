"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin, staticfiles
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from account.views import RegisterAPIView, RequestForSendVerificationEmailAPIView, VerificationAPIView

urlpatterns = [
    # регистрация
    path("api/v1/reg/", RegisterAPIView.as_view(), name="reg"),

    # вход по jwt POST запросом
    # GET запрос не разрешен => страницу с формой прописывай сам на фронте
    path('api/v1/token/', TokenObtainPairView.as_view(), name='login'),

    # повторное получение refresh токена
    # страницы на фронте не должно существовать
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # страницы на фронте не должно существовать
    # проверка действителен ли access token
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # получение письма верификации
    path('get-verif-mail/', RequestForSendVerificationEmailAPIView.as_view()),

    # ссылка, которая будет помещена в письмо - по ней будет производиться верефикация
    path('verification/<uuid:uuid>/', VerificationAPIView.as_view())
]