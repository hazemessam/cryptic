from django.views import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        ctx = {'text': 'Hello Django'}
        return render(request, 'home.html', ctx)
