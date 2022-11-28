


from django.db import models
import datetime

class Language(models.Model):
    name = models.CharField(max_length=50)
    month_to_learn = models.IntegerField()

    def __repr__(self):
        return self.name

class AbstractPerson(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __repr__(self):
        return self.name

class Student(AbstractPerson):

    work_study_place = models.CharField(max_length=100, null=True)
    has_own_notebook = models.BooleanField(default=False)
    preferred_os = models.CharField(max_length=50)

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, null=True)
    experience = models.DateField()


class Course(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    date_started = models.DateField(auto_now_add=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete =models.CASCADE)

    def __repr__(self):
        return self.name

    def get_course_end(self):
        days = Language.month_to_learn * 30
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        return date


