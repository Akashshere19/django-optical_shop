from django.shortcuts import render
from frames.forms import NewForm
from django.http import HttpResponse

# Create your views here.
def optical_form(request):
    return render(request,"frames/success.html")
def InsertData(request):
    form = NewForm()
    if request.method == 'POST':
        form =NewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return optical_form(request)
        else:
            print('error')
    return render(request,"frames/optical.html",{'form':form})
