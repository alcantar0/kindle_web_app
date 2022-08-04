from django.shortcuts import render, redirect, HttpResponse



def index(request):
    return redirect('home')

def upload(request):
    return render(request, "core/login.html")

def process_text(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['documento']
        a = uploaded_file.read().decode('UTF-8')
        print(a)
        return HttpResponse('<h1> OK </h1>')
