from django.urls import path

from . import views

app_name = 'downloader'

urlpatterns = [
    path('<str:img>', views.ServeImage.as_view(), name='serve_image')
]
