from django.shortcuts import render
#from django.shortcuts import redirect

# Create your views here.
def main(request):
    return render(request, 'main.html')