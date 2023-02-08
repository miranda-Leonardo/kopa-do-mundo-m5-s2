from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
from .utils import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError, data_processing


# Create your views here.
class TeamsView(APIView):
    def get(self, request: Request) -> Response:
        teams_response: list[dict] = []

        teams = Team.objects.all()
        for team in teams:
            i = model_to_dict(team)
            teams_response.append(i)

        return Response(teams_response)

    def post(self, request: Request) -> Response:
        data = request.data
        try:
            data_processing(data)
        except NegativeTitlesError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)

        team_response = Team.objects.create(**data)

        return Response(team_response, status.HTTP_201_CREATED)


class TeamsFilterView(APIView):
    def get(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_response = model_to_dict(team)

        return Response(team_response, status.HTTP_200_OK)

    def patch(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        data = request.data

        for chave, valor in data.items:
            setattr(team, chave, valor)

        team.save()
        team_response = model_to_dict(team)

        return Response(team_response, status.HTTP_200_OK)

    def delete(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)
