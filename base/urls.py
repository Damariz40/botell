"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from base.views import index_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_admin, name=""),
    path("comunidad/", include("comunidad.urls")),
    path("comunidad/api/", include("comunidad.api_urls")),
    path("servicios/", include("servicios.urls")),
    path("servicios/api/", include("servicios.api_urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
