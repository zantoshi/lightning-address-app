from django.shortcuts import render
from django.views import View
import requests, json
from django.http import JsonResponse
import zebedee
import environ

env = environ.Env()
lightning_address_project = zebedee.Project(env('ZEBEDEE_API_KEY'))

def index(request):
    lightning_address = env('LIGHTNING_ADDRESS')
    static_charge = env('STATIC_CHARGE')
    ctx = {"lightning_address": lightning_address, "static_charge": static_charge}
    return render(request, "staticcharges/index.html", ctx)

def get_lightning_address(request, username):
    sc = lightning_address_project.get_static_charge_metadata(env('STATIC_CHARGE_ID'))
    return JsonResponse(sc)