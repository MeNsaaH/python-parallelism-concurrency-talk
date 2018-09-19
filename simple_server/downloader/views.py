import os

from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views import View


class ServeImage(View):
    """ Returns img requests """
    def get(self, request, img):
        """ Serve the image file on get request """
        image = f'{settings.MEDIA_ROOT}/{img}'
        if os.path.isfile(image):
            return FileResponse(open(image, 'rb'), filename='a')
        return HttpResponse(b'File not found')
