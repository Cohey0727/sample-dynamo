from django.urls import path
from .views import TodoViewSet, hello
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('hello', TodoViewSet.as_view),
# ]


router = DefaultRouter()
router.register(r'hello', TodoViewSet, basename='todo')
urlpatterns = router.urls
