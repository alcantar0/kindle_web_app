"""Conjunto de views para o app core"""
from django.shortcuts import render, redirect


def index():
    """Função que retorna para o endereço home (default)"""
    return redirect("/home")


def upload(request):
    """Função que gera a página de envio do arquivo"""
    return render(request, "core/login.html")


def process_text(request):
    """Função que processa e retorna os highlights do arquivo"""
    if request.method == "POST":
        uploaded_file = request.FILES["documento"]
        livro_nome = request.POST.get("titulo")
        raw = uploaded_file.read().decode("UTF-8")
        raw_dividido = raw.split("==========")
        list_dicts = []
        for highlight in raw_dividido:
            if livro_nome not in highlight:
                continue
            separado = highlight.split("\n")
            ind = separado[2].find("Added on ")
            data_pronta = separado[2]
            data_pronta = data_pronta[ind + 9 :]
            # print(separado[1])
            # print(separado[2])  # Titulo livro
            # print(separado[4])  # Highlight
            dict_high = {"highlight": separado[4], "data": data_pronta}
            list_dicts.append(dict_high)
        data = {"highlights": list_dicts}
    return render(request, "core/page.html", data)
