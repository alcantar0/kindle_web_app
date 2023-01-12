"""Conjunto de views para o app core"""
from django.shortcuts import render

from django.db import connection

from django.db import transaction

from core.utils import proccess_data

from core.models import Livro


def home(request):
    """Função que gera a página de envio do arquivo"""
    return render(request, "core/index.html")


@transaction.non_atomic_requests
def process_text(request):  # pylint: disable=R0914 R1710 R0912 R0915

    """Função que processa e retorna os highlights do arquivo"""
    if request.method == "POST":  # pylint: disable=R1710
        uploaded_file = request.FILES["documento"]
        print(request.FILES)
        raw = uploaded_file.read().decode("UTF-8")
        raw = raw.split("\n")

        raw = [element for element in raw if (element and element.strip())]

        counter = 0
        see = True
        mark = []
        titles = []

        while see is True:
            try:
                data = raw[counter + 1]
            except IndexError:
                see = False
                break
            if data[0:8] == "- Your B" or data[0:6] == "- Seu m":
                counter += 3

            elif data[0:8] == "- Your N":
                if raw[counter] not in titles:
                    titles.append(raw[counter])
                ind = raw[counter + 1].find("Added on ")
                string_data_raw = raw[counter + 1]
                string_data_raw = string_data_raw[ind + 9 :]
                print(string_data_raw)
                data = proccess_data.transform_to_list(string_data_raw)
                data_pronta = proccess_data.convert_to_string(*data)

                dicionario = {
                    "titulo": raw[counter],
                    "data": data_pronta,
                    "highlight": raw[counter + 6],
                    "anotacao": raw[counter + 2],
                }
                counter += 8
                mark.append(dicionario)
                if not Livro.objects.filter(  # pylint: disable=E1101
                    **dicionario
                ).exists():  # pylint: disable=E1101
                    Livro.objects.create(**dicionario)  # pylint: disable=E1101

            elif data[0:6] == "- Sua n":
                if raw[counter] not in titles:
                    titles.append(raw[counter])
                ind = raw[counter + 1].find("Adicionado: ")
                string_data_raw = raw[counter + 1]
                string_data_raw = string_data_raw[ind + 12 :]

                dicionario = {
                    "titulo": raw[counter],
                    "data": string_data_raw,
                    "highlight": raw[counter + 6],
                    "anotacao": raw[counter + 2],
                }
                counter += 8
                mark.append(dicionario)
                if not Livro.objects.filter(  # pylint: disable=E1101
                    **dicionario
                ).exists():  # pylint: disable=E1101
                    Livro.objects.create(**dicionario)  # pylint: disable=E1101

            elif data[0:6] == "- Seu d":
                if raw[counter] not in titles:
                    titles.append(raw[counter])
                ind = raw[counter + 1].find("Adicionado: ")
                string_data_raw = raw[counter + 1]
                string_data_raw = string_data_raw[ind + 12 :]

                dicionario = {
                    "titulo": raw[counter],
                    "data": string_data_raw,
                    "highlight": raw[counter + 2],
                    "anotacao": "0",
                }
                counter += 4
                mark.append(dicionario)
                if not Livro.objects.filter(  # pylint: disable=E1101
                    **dicionario
                ).exists():  # pylint: disable=E1101
                    Livro.objects.create(**dicionario)  # pylint: disable=E1101

            elif data[0:8] == "- Your H":
                if raw[counter] not in titles:
                    titles.append(raw[counter])
                ind = raw[counter + 1].find("Added on ")
                string_data_raw = raw[counter + 1]
                string_data_raw = string_data_raw[ind + 9 :]
                data = proccess_data.transform_to_list(string_data_raw)
                data_pronta = proccess_data.convert_to_string(*data)

                dicionario = {
                    "titulo": raw[counter],
                    "data": data_pronta,
                    "highlight": raw[counter + 2],
                    "anotacao": "0",
                }
                counter += 4
                mark.append(dicionario)
                if not Livro.objects.filter(  # pylint: disable=E1101
                    **dicionario
                ).exists():  # pylint: disable=E1101
                    Livro.objects.create(**dicionario)  # pylint: disable=E1101
            else:
                counter += 1
        titles = Livro.objects.all().distinct("titulo")  # pylint: disable=E1101
        return render(request, "core/teste.html", {"titles": titles})


@transaction.non_atomic_requests
def listar(request):  # pylint: disable=R1710
    """Lista os highlights"""
    if request.method == "POST":
        titulo = request.POST.get("nome_livro")
        titles = Livro.objects.filter(titulo__contains=titulo)  # pylint: disable=E1101
        titles = list(titles)

        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE core_livro")
        return render(request, "core/page.html", {"dados": titles})
