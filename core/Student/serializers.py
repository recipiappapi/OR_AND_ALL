from rest_framework import serializers
class TeacherSerializer(serializers.Serializer):
    firstname  = serializers.CharField(max_length=100)
    surname    = serializers.CharField(max_length=100)


class StudentSerializer(serializers.Serializer):
    firstname =  serializers.CharField(max_length=100)
    surname   =  serializers.CharField(max_length=100)
    age       =  serializers.IntegerField()
    classroom =  serializers.IntegerField() 
