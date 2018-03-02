from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def form_view(request):
    form = forms.FormName()
    
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VAlidation Success!")
            print(form.cleaned_data['name'])

    return render(request, 'formapp/formpage.html', {'form': form} )