import json

from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, Resolver404, resolve
from django.views.generic import FormView, TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd


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


@login_required(login_url=reverse_lazy('login-page'))
def home(request):
    return render(request, 'home.html')


@login_required(login_url=reverse_lazy('login-page'))
def simple_upload(request):
    print(request.FILES)

    if request.method == 'POST' and request.FILES:
        for file in request.FILES.values():
            # Inserir aqui algumas validações tipo essa
            df = pd.read_csv(file)
            print(df.head())

        if file.content_type in ['text/csv',]:
            messages.success(request, 'Arquivo correto!')
        else:
            messages.error(request, 'Formato de Arquivo inválido!')

        # Aqui você faz algo com o arquivo, salva, compila, envia para outro
        # lugar, etc

        return render(request, 'upload.html', {
            'uploaded_file_url': file.name
        })
    return render(request, 'upload.html')


class Loginpage(TemplateView):
    """
    Login do sistema
    """
    template_name = 'login.html'

    def post(self, *args, **kwargs):
        print(self.request.POST)
        username = self.request.POST.get('Username', '')
        password = self.request.POST.get('Password', '')
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(self.request, user)
            return HttpResponseRedirect('/upload/')
        else:
            return HttpResponseRedirect('/')


loginpage = Loginpage.as_view()


def logout_view(request):
    logout(request)
    return redirect('login-page')

