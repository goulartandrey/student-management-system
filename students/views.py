from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from students.forms import *
from students.models import Student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'index.html', {
            'form': AuthenticationForm,
            'error': 'Usuario ou senha incorreto'
        })
    else:
        login(request, user)
        return redirect('home')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form': AuthenticationForm})
    
def home(request):
    return render(request, 'students.html', {
        'students':Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))

def add(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            new_student.save()
            return render (request, 'add.html', {
                'form':StudentForm(),
                'success':True
            })
    else:
        form = StudentForm()
    return render(request, 'add.html', {
        'form':StudentForm()
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form':form,
                'success':True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('home'))