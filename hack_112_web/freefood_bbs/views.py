from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import datetime

# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'index.html', {'current_time': datetime.datetime.now()})