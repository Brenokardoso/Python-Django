from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from .settings import *

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("auth/", include("autentication.urls")),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
