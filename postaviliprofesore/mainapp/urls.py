from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.apiView, name='apiView'),
    path('api/detail-view/<path:webtag>', views.detailView, name='detailView'),
    path('api/fakultet-view/', views.fakultetView, name='fakultetView'),
    path('result/<path:webtag>', views.resultView, name='resultView'),
    path('searchResult/', views.searchResult, name="searchResult")
]
