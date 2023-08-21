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
                  path('ajax1/', views.ajax_1, name='phylogene_ajax1'),
                  path('analysis/', views.analysis, name='analysis'),
                  path('refseq/', views.refseq, name='refseq'),
                  path('run_algo/', views.run_algo, name='phylogene_run_algo'),
                  path('online_tools/', views.online_tools, name='online_tools'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
