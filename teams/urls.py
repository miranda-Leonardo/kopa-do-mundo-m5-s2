from django.urls import path
from .views import TeamsView, TeamsFilterView

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<int:team_id>/", TeamsFilterView.as_view())
]
