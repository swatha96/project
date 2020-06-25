from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("empaddapp.urls")),
    path("empadd/",include("empaddapp.urls")),
]
