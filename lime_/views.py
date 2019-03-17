from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, FormView
from django.urls import reverse

from .forms import DocumentForm, FeatureForm, ClassNameForm, ParameterForm
# Views here
feature = list()
class_name = list()
parameter = list()

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feature')
    else:
        form = DocumentForm()
    return render(request, 'lime_/upload.html', {
        'form': form
    })

def feature_form(request):
    if request.method == 'POST':
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            feature = request.POST['feature']
            return redirect('classname')
    else:
        form = FeatureForm()
    return render(request, 'lime_/features.html', {
        'form': form
    })

def class_name_form(request):
    if request.method == 'POST':
        form = ClassNameForm(request.POST, request.FILES)
        if form.is_valid():
            # request.session['feature'] = request.POST['feature']
            class_name = request.POST['class_name']
            form.save()
            return redirect('parameter')
    else:
        form = ClassNameForm()
    return render(request, 'lime_/class_name.html', {
        'form': form
    })

def parameter_form(request):
    if request.method == 'POST':
        form = ParameterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = ParameterForm()
    return render(request, 'lime_/parameter.html', {
        'form': form
    })

# def result_display(request):