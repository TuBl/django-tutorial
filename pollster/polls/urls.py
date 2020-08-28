from django.urls import path
from . import views
app_name = 'polls'  # namespace


urlpatterns = [
    path('', views.index, name='index'),  # /polls
    # will pass question_id to our views rendering method for detail
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
