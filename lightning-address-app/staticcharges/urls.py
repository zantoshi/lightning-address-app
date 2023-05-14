from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('.well-known/lnurlp/<username>', views.get_lightning_address, name='user_lightning_address')
]