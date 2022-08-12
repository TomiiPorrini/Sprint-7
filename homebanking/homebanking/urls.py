"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Login import views as views_login
from Prestamos import views as views_prestamos
from Tarjetas import views as views_tarjetas
from Cuentas import views as views_cuentas
from django.urls import include
# from Login import views as views_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views_login.login, name='login'),
    path('home/', views_login.home, name="home"),
    path('register/', views_login.register, name='register'),
    path('prestamos/', views_prestamos.prestamos, name='prestamos'),
    path('tarjetas/', views_tarjetas.tarjetas, name='tarjetas'),
    path('cuentas/', views_cuentas.cuentas, name='cuentas'),
    path('accounts/',include('django.contrib.auth.urls')),
]

from django.conf import settings
if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)