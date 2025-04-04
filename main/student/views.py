from django.shortcuts import render
from django.http import HttpResponse;
from .models import *
from django.core.paginator import Paginator
from django.db.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def students(request):
    queryset=  Student.objects.all()


 # for serching students 

    if request.GET.get('s-student'):
        query = request.GET.get('s-student')
        
        
        queryset= queryset.filter(Q(student_name__icontains=query) | Q(student_age__icontains=query) | 
        Q(student_email__icontains=query)| Q(department__department__icontains=query))

      

   

# for pagging 
    paginator = Paginator(queryset, 15)  # Show 25 contacts per page.

    query = request.GET.get('s-page', '')
    page_number = request.GET.get("page", query)
    page_obj = paginator.get_page(page_number)
   

    context = {"queryset": page_obj}  # Pass the students queryset, not query string
    return render(request, 'report/student.html', context)

# for see marks 

def see_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    tot_marks = queryset.aggregate(tot_marks=Sum('marks'))
 
   

# for ranking students
    crr_rank = -1
    ranks = Student.objects.annotate(marks = Sum('student_marks__marks')).order_by('-marks', '-student_age')
    i=1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            crr_rank =i
            break
        i+=1


    return render(request, 'report/see_marks.html', {'queryset': queryset, 'tot_marks': tot_marks, 'crr_rank': crr_rank})





