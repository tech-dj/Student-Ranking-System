from django.db import models



# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

# StudentID Model
class StudentID(models.Model):
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.student_id

    
# Subject Model

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    

# Student Model
class Student(models.Model):  # Added missing inheritance
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)  # Fixed on_delete
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)  # Fixed spelling
    student_age = models.IntegerField(default=18)
    student_address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"  # Fixed incorrect tuple format

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="student_marks", on_delete=models.CASCADE)  
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self)->str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
        unique_together = ['student', 'subject']
     

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name = "studentreportcard", on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_reportCard = models.DateField(auto_created=True)

    class Meta:
        unique_together = ['student_rank', 'date_of_reportCard']

