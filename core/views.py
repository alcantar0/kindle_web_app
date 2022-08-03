from django.shortcuts import render




def index(request):
    return redirect('/home')

def upload(request):
    return render(request, "core/login.html")

def process_text(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['documento']
        print(uploaded_file.read())
