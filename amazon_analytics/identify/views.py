from django.shortcuts import render
from . import forms
from .recognize import rekognition
from .cleaner import clean
from .models import Image

# Create your views here.


def base(request):
    form = forms.ImageForm()
    if request.method == "POST":
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            img_obj = form.instance
            img = (str(data.image)).split()[0]
            res = rekognition(img)
            c = clean(res)
            return render(request, 'identify/index.html', {'form': form, 'img_obj': img_obj, 'clean_data': c})
    else:
        form = forms.ImageForm()
    return render(request, 'identify/index.html', {'form': form})
