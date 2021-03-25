from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('napravi-svoj/', views.napravisvoj, name='napraviSvoj'),
    path('uputstvo/', views.uputstvo, name='uputstvo'),
    path('api/', views.apiView, name='apiView'),
    path('api/detail-view/<path:webtag>', views.detailView, name='detailView'),
    path('api/semestar-view/', views.semestarapiView, name='semestarView'),
    path('api/fakultet-view/', views.fakultetView, name='fakultetView'),
    path('result/<path:webtag>', views.resultView, name='resultView'),
    path('searchResult/', views.searchResult, name="searchResult"),
    path('test/', views.test, name='test'),
]
