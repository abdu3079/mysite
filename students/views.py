from django.shortcuts import render,get_object_or_404
import datetime
from . models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    all_students=Student.objects.all()
    current_year=datetime.datetime.now()
    context={'abc':'ABCDDDDDDD','current_year':current_year,'all_students':all_students,}
    return render(request,'students/index.html',context)

def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'students/index.html')
        else:
            context={'form':form}
            return render(request,'students/add.html', context)
    else:
        form=StudentForm()
        context={'form':form}
        return render(request,'students/add.html',context)
    
def delete(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        student.delete()
        return render(request,'students/index.html')
    context={'student':student}  
    return render(request,'students/delete.html',context)



def update(request,pk):
    student=Student.objects.get(pk=pk)
    if request.method=='POST':
        return render(request,'students/add.html')


    

