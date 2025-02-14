from django.shortcuts import render  
from django.http import HttpResponse  
# from fileuploading.functions import handle_uploaded_file  
from fileupload.forms import StudentForm  

def handle_uploaded_file(f):  
    with open('static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})  