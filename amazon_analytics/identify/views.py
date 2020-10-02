from django.shortcuts import render
from . import forms

# Create your views here.
def base(request):
    # form = forms.ImageForm()
    if request.method == "POST":
        form = forms.ImageForm(request.POST,request.FILES)
        if form.is_valid():
            # form.instance.title = "image" + str(counter)
            # print(form.instance.title)
            # counter = counter + 1
            form.save()
            img_obj = form.instance
            return render(request, 'identify/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = forms.ImageForm()
    return render(request,'identify/index.html',{'form':form})