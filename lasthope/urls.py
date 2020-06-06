from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('checkup/', views.checkup, name='checkup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
