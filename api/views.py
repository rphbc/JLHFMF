import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class Return1(APIView):

    def get(self, request):
        return Response({'resultado': 1})

    def post(self, request):
        dados = request  # recebe os dados que o cara enviou
        json_data = json.loads(
            dados.data)  # faz o parse de json para dicionario
        # Aqui você pode fazer algo interessante com o dado, tipo salvar no db
        return Response({'resultado': json_data})


return1 = Return1.as_view()


class Return2(APIView):

    def get(self, request):
        return Response({'resultado': 2})

    def post(self, request):
        dados = request  # recebe os dados que o cara enviou
        json_data = json.loads(
            dados.data)  # faz o parse de json para dicionario
        # Aqui você pode fazer algo interessante com o dado, tipo salvar no db
        return Response({'resultado': json_data})


return2 = Return2.as_view()


def home(request):
    return render(request, 'home.html')
