from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    
    # # ex: /myapp/
    # path("", views.index, name="index"),
    # # ex: /myapp/5/
    # path("<int:question_id>/detail", views.detail, name="detail"),
    # # ex: /myapp/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /myapp/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

]
