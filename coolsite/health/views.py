from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


menu = ["Żywie Biełaruś!", "Sława Ukrajini!", "Niech żyje Polska"]


def index(request):
	post = Health.objects.all()
	return render(request, "health/index.html", {"menu":menu, "title":"Super usefull page"})


def about(request):
	return render(request, "health/about.html", {"title":"About you"})


def categories(request):
	if request.POST:
		print(request.POST)

	return HttpResponse("Categories of menthal disorders")