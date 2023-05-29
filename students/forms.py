from django import forms
from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "student_number": "Student Number",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "field_of_study": "Field of Study",
            "gpa": "GPA",
        }
        widgets = {
            "student_numer": forms.NumberInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "field_of_study": forms.TextInput(attrs={"class": "form-control"}),
            "gpa": forms.NumberInput(attrs={"class": "form-control"}),
        }