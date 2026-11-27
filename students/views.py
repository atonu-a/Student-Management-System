from django.shortcuts import render, redirect
from .forms import StudentForm
# Create your views here.
def home(request):
    return render(request, "base.html")

#======================
#   Creating Student
#======================

def create_student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "create-student.html", {"form": form})