from django import forms
from app1.models import Add_class,Student_registartion


class Add_classform(forms.ModelForm):
    class Meta:
        model = Add_class
        fields = "__all__"
        
class Student_registartionform(forms.ModelForm):
    sname = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    password =forms.CharField(label="Password")

    class Meta:
        model = Student_registartion
        fields = "__all__"
