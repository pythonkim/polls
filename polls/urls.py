from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('login/',views.mylogin, name='mylogin'),
    path('data/',views.data,name='data'),
    path('dddd/',views.dddd,name='dddd'),
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('logout/',views.mylogout,name='mylogout'),
]
