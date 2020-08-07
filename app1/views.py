from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from app1.models import Student_registartion,Add_class
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from app1.forms import Add_classform,Student_registartionform
# Create your views here.
def ShowIndex(request):
    schedule = Add_class.objects.all()
    return render(request,"main.html",{"schedule":schedule})


class Stu_registration(CreateView):
    template_name = "student_registration.html"
    model = Student_registartion
    fields = ('sname','email','password')
    success_url = '/Student_welcome_page/'


def Student_welcome_page(request):

    return render(request,)


def stu_Login(request):
    us = request.POST.get("s1")
    password = request.POST.get("s2")

def admin_login(request):
    return render(request,"admin_login_page.html")

def admin_login_check(request):
    us = request.POST.get("ad1")
    paswd = request.POST.get("paswd")
    if us == "Bhanu" and paswd == "Bhanu3210":
       print(us,paswd)
       return redirect('admin_welcome_page')
    else:
        messages.error(request,"invalid username or Password")
        return redirect('admin_login')
def admin_welcome_page(request):
       data = Student_registartion.objects.all()
       return render(request,"admin_welcome_page.html", {"data": data})


class Add_new_class(CreateView):
      template_name = "Schedule_new_class.html"
      model = Add_class
      fields = "__all__"
      success_url = '/View_all_scheduled_classes/'


def View_all_scheduled_classes(request):
    schedule = Add_class.objects.all()
    return render(request,"View_all_scheduled_classes.html",{"schedule":schedule})



def edit(request,id):
  add_class = Add_class.objects.get(fno = id)
  return render(request,"edit.html",{"add_class":add_class})


def update_class(request,id):
    add_class = Add_class.objects.get(fno=id)
    form = Add_classform(request.POST,instance=add_class)
    if form.is_valid():
       form.save()
       return redirect('/View_all_scheduled_classes')
    return render(request,"edit.html",{"add_class":add_class})


def delete_class(request,id):
    remove = Add_class.objects.get(fno = id)
    remove.delete()
    return redirect('/View_all_scheduled_classes')