from django.urls import path
from tailleur_core.views import index

app_name = 'tailleur_core'

urlpatterns = [
    path('', index)
]
