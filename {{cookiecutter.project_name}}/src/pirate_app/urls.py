from django.urls import path
from .views import tell_joke

urlpatterns = [
    path("joke/", tell_joke, name="tell_joke"),
]