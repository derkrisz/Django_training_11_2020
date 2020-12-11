# we added this page to the polls app
# here we explain the routing for our polls app

from django.urls import path

from . import views 

# we can name our app to make code more generic/reusable

app_name = 'polls'

urlpatterns = [
    # eg /polls/
    path('', views.index, name='index'), # this is the default path ''
    # eg /polls/4/ 
    path('<int:question_id>/', views.detail, name='detail'),
    # eg /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # eg /polls/2/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]