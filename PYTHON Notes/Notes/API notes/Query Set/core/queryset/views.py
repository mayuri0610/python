from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.

def student_list(request):

    # posts = Student.objects.all()

    # posts = Student.objects.filter(surname__startswith='S') | Student.objects.filter(surname__startswith='E')

    # posts = Student.objects.filter(Q (surname__startswith='S') | Q(firstname__startswith='M') | Q(surname__startswith='k'))

    posts = Student.objects.filter(Q (surname__startswith='S') | Q(firstname__startswith='M') | Q(surname__startswith='k'))

    # posts = Student.objects.filter(Q (surname__startswith='S') & Q(firstname__startswith='M') )

    

    print(posts)
    print(posts.query)
    return render(request, 'output.html', {'posts': posts})



