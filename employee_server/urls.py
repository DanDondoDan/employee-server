"""employee_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from employee_server.routers import router
from employee_server import views
from employee_server import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include(router.urls)),
    url(r'^unit-detail/(?P<pk>\d+)/employeers/$',
        views.UnitDetail.as_view()),
    url(r'^sub/(?P<pk>[0-9]+)/employeers/$', views.UnitEmployeerView.as_view()),
    url(r'^sign-up/', views.CustomUser.as_view()),
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'^detail-person/', views.PersonViewSet.as_view({'get': 'list'})),
    url(r'^rest-auth/login/', views.LoginView.as_view(), name='rest_login'),
    url(r'^list/person/create', views.ListCreatePersonView.as_view()),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name="person-detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# http://qaru.site/questions/15634515/update-and-delete-in-same-api-view-without-passing-id-in-url