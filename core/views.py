"""Conjunto de views para o app core"""
from django.shortcuts import render

from core.utils import proccess_data


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def home(request):
    """Função que gera a página de envio do arquivo"""
    return render(request, "core/index.html")


def process_text(request):  # pylint: disable=R0914 R1710 R0912 R0915
    """simsim"""
    if request.method == "POST":  # pylint: disable=R1710
        uploaded_file = request.FILES["documento"]
        raw = uploaded_file.read().decode("UTF-8")
        raw = raw.split("\n")

        raw = [element for element in raw if (element and element.strip())]

        counter = 0
        see = True
        mark = []
        titles = []
        dicionario = {}
        while see is True:
            try:
                data = raw[counter + 1]
            except IndexError:
                see = False
                break
            if data[0:7] == "- Seu m" or data[0:8] == "- Your B":
                counter += 3

            elif data[0:7] == "- Sua n":
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
            elif data[0:7] == "- Seu d":
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
            elif data[0:8] == "- Your N":
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
                    "highlight": raw[counter + 6],
                    "anotacao": raw[counter + 2],
                }
                counter += 8
                mark.append(dicionario)

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
            else:
                counter += 1

        request.session["livros"] = mark

        return render(request, "core/teste.html", {"titles": titles})


def listar(request):  # pylint: disable=R1710
    """Lista os highlights"""
    if request.method == "POST":
        raw = request.session.get("livros")
        titulo = request.POST.get("nome_livro")

        titles = [element for element in raw if titulo in element["titulo"]]

        return render(request, "core/page.html", {"dados": titles})
