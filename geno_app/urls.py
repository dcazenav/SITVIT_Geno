from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns = [
                  path('geno_app/', views.index, name='index'),
                  path('', views.home, name='home'),
                  path('database_descriptions/', views.database_description, name='database_description'),
                  path('search/', views.search, name='search'),
                  path('analysis/', views.analysis, name='analysis'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
