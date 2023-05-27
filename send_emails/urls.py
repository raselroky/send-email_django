
from django.contrib import admin
from django.urls import path,include
from .views import SendEmailApi

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('email/',SendEmailApi.as_view()),
]
