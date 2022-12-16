"""Conjunto de views para o app core"""
from django.shortcuts import render
from django.db import transaction

from core.utils import proccess_data

from core.models import Livro


def home(request):
    """Função que gera a página de envio do arquivo"""
    return render(request, "core/login.html")


@transaction.non_atomic_requests
def process_text(request):  # pylint: disable=R0914 R1710

    """Função que processa e retorna os highlights do arquivo"""
    if request.method == "POST":  # pylint: disable=R1710
        uploaded_file = request.FILES["documento"]
        raw = uploaded_file.read().decode("UTF-8")
        # livro_nome = "Scar Tissue"
        raw_dividido = raw.split("==========")
        list_dicts = []
        titles = []
        counter = 1
        for highlight in raw_dividido:
            highlight = highlight.strip("\r")
            highlight = highlight.strip("")
            separado = highlight.split("\n")
            if separado == [
                "",
                "",
            ]:  # Tratamento de erro para a última linha do arquivo
                continue

            titulo = ""
            highlight = ""
            if counter == 1:  # Tratamento de erro para primeira linha do arquivo
                ind = separado[1].find("Added on ")
                string_data_raw = separado[1]
                titulo = separado[0]
                highlight = separado[3]
                titles.append(f"{separado[0]}")
                print(f"{separado[0]}")
            else:
                if separado[1] not in titles:
                    titles.append(separado[1])
                ind = separado[2].find("Added on ")
                titulo = separado[1]
                highlight = separado[4]
                string_data_raw = separado[2]
            string_data_raw = string_data_raw[ind + 9 :]
            # print(string_data_raw)

            # print(titulo)  # Titulo
            # print(separado[2])  # Dados
            # print(separado[4])  # Highlight
            data = proccess_data.transform_to_list(string_data_raw)
            data_pronta = proccess_data.convert_to_string(*data)
            dict_high = {"titulo": titulo, "data": data_pronta, "highlight": highlight}
            if not Livro.objects.filter(**dict_high).exists():  # pylint: disable=E1101
                Livro.objects.create(**dict_high)  # pylint: disable=E1101
            list_dicts.append(dict_high)
            counter += 1
        titles = Livro.objects.all().distinct("titulo")  # pylint: disable=E1101
        return render(request, "core/teste.html", {"titles": titles})


def listar(request):  # pylint: disable=R1710
    """Lista os highlights"""
    if request.method == "POST":
        titulo = request.POST.get("nome_livro")
        titles = Livro.objects.filter(titulo__contains=titulo)  # pylint: disable=E1101
        return render(request, "core/page.html", {"dados": titles})
