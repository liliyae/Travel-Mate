from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path("helloApi", views.hello, name='hello'),
    path("registerPage", views.registerPage, name='registerPage'),
    path("jquery-3.4.1.min.js", views.Jquery, name="JQuery"),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]