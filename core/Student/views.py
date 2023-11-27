from django.shortcuts import render
from .models import Students,Teacher
from .serializers import StudentSerializer,TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
#Returnting specific id
def Student_list(request,pk):
    stu        = Students.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data  = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type= 'application/json')

#IF TO RETURN ALL RECORDS 
def Student_list_all(request):
    StudentData  =  Students.objects.all()
    print(StudentData)
    serializer   =  StudentSerializer(StudentData,many=True)
    json_data    =  JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def Teacher_list(request,pk):
    tec               = Teacher.objects.get(id=pk)
    serializer        = TeacherSerializer(tec)
    teacher_json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(teacher_json_data,content_type='application/json')

def Student_Filter(request):
    # student = Students.objects.filter(Q(surname__startswith="Gopal")) | Students.objects.filter(Q(surname__startswith="Himal"))
    student = Students.objects.filter(~Q(surname__startswith="Gopal"))

    # students = Students.objects.filter(Q(surname="Gopal") | Q(surname="Hari"))
    serializer        = StudentSerializer(student,many=True)
    return JsonResponse(serializer.data, safe=False)



def Student_Filter_And(request):
    # Student_Data = Students.objects.filter(Q(surname="Gopal")) & Students.objects.filter(Q(age=25))
    Student_Data = Students.objects.filter(Q(surname="Gopal"))  &  Students.objects.filter(Q(age=25))

    serializer = StudentSerializer(Student_Data,many=True)

    return JsonResponse(serializer.data, safe=False)


