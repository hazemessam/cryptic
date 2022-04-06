from email import header
from django import views
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class FileView(View):
    def get(self, request):
        return HttpResponse('File upload service')
