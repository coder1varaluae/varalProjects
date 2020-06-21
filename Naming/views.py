from django.shortcuts import render, redirect
from .models import Form_Name, File
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
import os
# Create your views here.
def name(request):
    unnamedfile = File.objects.last()
    # path="/files/files/Emaillogic.png"  # insert the path to your directory
    # lastfile= File.objects.last()
        # filepath= lastfile.filepath .os.getcwd()
    path='C:\\Users\\Varal Consultancy\\Desktop\\doc_naming\\doc_naming/apps/' +str(unnamedfile.filepath)
    img_list =os.listdir(path)
    if request.method == "POST":
        Jurisdiction = request.POST["Jurisdiction"]
        Formname = request.POST["Form"]
        formname = Form_Name.objects.create(Jurisdiction=Jurisdiction,Formname=Formname)
        formname.save()
        count=Form_Name.objects.all().count()
        print(count)
        if count >= 1:
            return render(request, "NameFormTemplate/formNaming.html", {'images': img_list})
        else :
             return redirect("www.google.com")
    else:
        return render(request, "NameFormTemplate/formNaming.html", {'images': img_list})

    #     form = RegisterForm()
    # documentID =   .object.fetchone()
    # return render(request,'Naming/formNaming.html',{'document':documentID})

# def upload(request):
#     if request.method == 'POST':
#         upload_file = request.FILES['document']
#         folder_id = '1KRH3uGLCfBHhI54tO1ydhCAKGoJvBlvS'
#         gupload(upload_file.name)
#
#
#         # fs = FileSystemStorage()
#         # fs.save(upload_file.name,upload_file)
#         # print(upload_file.name)
#         # print(upload_file.size)
#     return render(request, 'upload.html')


filepath = []
filename = []
def showfile(request):

    lastfile= File.objects.last()

    # filepath= lastfile.filepath .os.getcwd()
    filepath= lastfile.filepath

    filename= lastfile.name


    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form['filepath'].value()
        print(type(str(form['filepath'].value())))
        extension = []
        extension = str(form['filepath'].value()).split('.')
        file_ext = extension[1]
        print(extension[1])
        # print(form.data['filepath'])

        # form.save(update_fields=['name'])
        upload = form.save(commit = False)
        upload.name = file_ext
        upload.save()


    context= {'filepath': filepath,
              'form': form,
              'filename': filename
              }


    return render(request, 'files.html', context)
