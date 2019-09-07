from django.urls import path, include
from django.contrib import admin
from movie.views import MovieView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movie', MovieView, basename='movie')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('app/', include(router.urls))
]


