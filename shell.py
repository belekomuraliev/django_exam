import datetime
from user.models import Student, Mentor, Language,Course

languages = [
    {
        'name':'Python',
        'month_to_learn':6
    },
    {
        'name':'Java Script',
        'month_to_learn':6
    },
    {
        'name':'UX-UI',
        'month_to_learn':2
    },
]


students = [
    {
        'name':'Amanov Aman',
        'email':'aman@mail.ru',
        'phone_number':'+996700989898',
        'work_study_place':'School №13',
        'has_own_notebook':True,
        'preferred_os':'windows'
    },
    {
        'name':'Apina Alena',
        'email':'aapina@bk.ru',
        'phone_number':'0550888888',
        'work_study_place':'TV',
        'has_own_notebook':True,
        'preferred_os':'mac'
    },
    {
        'name':'Phil Spencer',
        'email':'spencer@microsoft.com',
        'phone_number':'0508312312',
        'work_study_place':'Microsoft Gaming',
        'has_own_notebook':False,
        'preferred_os':'linux'
    }
]


mentors = [
    {
        'name':'Ilona Maskova',
        'email':'imask@gmail.com',
        'phone_number':'0500545454',
        'main_work': None,
        'experience': datetime.date(year=2021, month=10, day=23)
    },
    {
        'name':'Halil Nurmuhametov',
        'email':'halil@gmail.com',
        'phone_number':'0709989876',
        'main_work':'University of Fort Collins',
        'experience':datetime.date(year=2010, month=9, day=18)
    }
]


for lan in languages:
    Language.objects.create(name=lan['name'], month_to_learn=lan['month_to_learn'] )


for st in students:
    Student.objects.create(name=st['name'], email=st['email'],
                           phone_number=st['phone_number'],
                           work_study_place=st['work_study_place'],
                           has_own_notebook=st['has_own_notebook'],
                           preferred_os=st['preferred_os'])

for ment in mentors:
    Mentor.objects.create(name=ment['name'], phone_number=ment['phone_number'],
                          main_work=ment['main_work'],experience=ment['experience'] )


