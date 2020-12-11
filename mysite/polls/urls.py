# django calls this the urlconf module

from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #indexview is a class, we cast to a view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'), # vote has no template
    path('child/', views.ChildView.as_view(), name='child'),
    path('get_name', views.get_name, name='get_name'),
]