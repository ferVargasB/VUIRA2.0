from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def about(request):
    return HttpResponse("<h2>Acerca de Nosotros</h2>");    
