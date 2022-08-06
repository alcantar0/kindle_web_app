from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return redirect("/home")


def upload(request):
    return render(request, "core/login.html")


def process_text(request):
    if request.method == "POST":
        uploaded_file = request.FILES["documento"]
        LIVRO_NOME = request.POST.get("titulo")
        raw = uploaded_file.read().decode("UTF-8")
        raw_dividido = raw.split("==========")
        
        for highlight in raw_dividido:
            if LIVRO_NOME not in highlight:
                continue
            else:
                separado = highlight.split("\n")
                ind = separado[2].find("Added on ")
                data_pronta = separado[2]
                data_pronta = data_pronta[ind + 9 :]
                print(separado[1])
                print(separado[2]) #Titulo livro
                print(separado[4]) # Highlight
    return HttpResponse("<h1>OK</h1>")

