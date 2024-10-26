from django.shortcuts import render  
from django.http import HttpResponse 
from MyWebsite.forms import NameForm
# Create your views here.

def home(request):
    return render(request, "index.html")
def get_details(request):
    form = NameForm()
    print("Form Calling")
    return render(request, "index.html", {"form": form})
    