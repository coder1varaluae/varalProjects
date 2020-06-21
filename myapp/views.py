from django.shortcuts import render, redirect

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from myapp.models import Document
from myapp.forms import DocumentForm

# Create your views here.
def docupload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            # messages.success(request, 'File upload successful')


            # Redirect to the document list after POST
            return redirect('list.html')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': documents, 'form': form})
