__all___ = ['router']


from rest_framework.routers import DefaultRouter, SimpleRouter


from employee_server.settings import SERVICE_VARS as cfg
from employee_server import views


_VIEWS = (
    # views.PersonViewSet,
    views.UnitViewSet,
    views.SearchPersonViewSet,
)



router = DefaultRouter()
# routerMy = MyRouter()


for rt in _VIEWS:
    name = rt.__name__[:rt.__name__.index(cfg['viewset_suffix'])].lower() + 's'
    router.register(name, rt)