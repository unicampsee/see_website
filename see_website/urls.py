"""see_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from eventos import views
from parceria import views as views2
from see_profile import views as views3
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^auth/', include('maro_auth.urls', namespace='maro_auth')),
    url(r'^profile/', views3.profile, name='profile'),
    url(r'^$', RedirectView.as_view(url='/parceria/')), 
    url(r'^parceria/', views2.parceria, name='parceria'),
    url(r'^admin/', admin.site.urls),
    url(r'^palestras/$', views.PalestrasView.as_view() , name = 'palestras'),
    # url(r'^palestras/(?P<pk>[0-0]+)/$', views.PalestrasDetailView.as_view() , name = 'palestrasDetails'),
    url(r'^visitas/$', views.VisitasView.as_view(), name = 'visitas_ecnicas'),
    url(r'^minicursos/$', views.MiniCursoView.as_view(), name = 'mini_cursos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
