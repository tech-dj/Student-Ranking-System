from django.contrib import admin
from django.db.models import *
from student.models import *
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register (Department)
admin.site.register(StudentID)
admin.site.register(Subject)

# list display
class StudentMarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks'  )
    search_fields = ('student_name', 'student_email')

admin.site.register(SubjectMarks, StudentMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank', 'total_marks', 'date_of_reportCard']

    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student= obj.student)
        print(subject_marks.aggregate(marks = Sum('marks')))
        return 0
    

admin.site.register(ReportCard, ReportCardAdmin)