from django.contrib import admin
from django.urls import path
from autoload.views import MainView


urlpatterns = [
    path('', MainView.as_view()),
    path('admin/', admin.site.urls),
]
