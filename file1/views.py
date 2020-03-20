from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import UploadFileForm

# # Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
from django.http import HttpResponse
from file1.functions import handle_uploaded_file
from file1.forms import StudentForm
from django.contrib import messages

def index(request):
 	if request.method=="POST":
 		student=StudentForm(request.POST, request.FILES)
 		if student.is_valid():
 			handle_uploaded_file(request.FILES['file'])
 			return HttpResponse(request,"File uploaded successfully")
 	else:
 		student=StudentForm()
 		return render(request, "index.html", {'form':student})
