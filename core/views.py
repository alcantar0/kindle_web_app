"""Conjunto de views para o app core"""
from django.shortcuts import render
from core.utils import proccess_data


def home(request):
    """Função que gera a página de envio do arquivo"""
    return render(request, "core/login.html")


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
                titles.append(separado[0])
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
            # Livro.objects.create(**dict_high)
            list_dicts.append(dict_high)
            counter += 1
        return render(request, "core/page.html", {"dados": list_dicts})
