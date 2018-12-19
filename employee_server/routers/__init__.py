__all___ = ['router']


from rest_framework.routers import DefaultRouter


from employee_server.settings import SERVICE_VARS as cfg
from employee_server import views


_VIEWS = (
    views.GeneralManagerViewSet,
    views.SpecialistViewSet,
    views.LowLevelManagerViewSet,
    views.SeniorManagerViewSet,
    views.TopManagerViewSet,
    views.StockholderViewSet,
)



router = DefaultRouter()


for rt in _VIEWS:
    name = rt.__name__[:rt.__name__.index(cfg['viewset_suffix'])].lower() + 's'
    router.register(name, rt)