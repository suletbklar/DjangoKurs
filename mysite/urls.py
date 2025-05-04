from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("polls/", permanent=True)),  # Ana sayfayı polls'a yönlendir
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]