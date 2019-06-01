# from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def intro(request):
    return render(request, 'intro.html', {})


def intro2(request):
    return render(request, 'info.html', {})


def check(request, num):
    a = []
    for i in range(0, num):
        a.append(i)
    # print(a)
    return render(request, 'check.html', {'data': [i for i in range(num)]})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # print(request)
        # print(request.method)
        # print(request.POST)
        form = NameForm(request.POST)
        # print(form.is_valid(), form.errors)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'info.html', {'form': form})


class NameForm(forms.Form):
    your_name = forms.EmailField(label='2 + 2', label_suffix=' =', required=True)
