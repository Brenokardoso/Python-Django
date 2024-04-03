from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include(arg="index.urls")),
    path('admin/', admin.site.urls),
    path('autentication/',include('autentication.urls'))
]
