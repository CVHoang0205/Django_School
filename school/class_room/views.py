from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from school.class_room.models import Student, Teacher, ClassRoom
from school.class_room.serializers import StudentSerializers, TeacherSerializers, ClassRoomSerializers

# Student Serializers View
class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()

#Teacher Serializers view
class TeacherList(generics.ListCreateAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

# Class_Room Serializers Views
class ClassRoomList(generics.ListCreateAPIView):
    serializer_class = ClassRoomSerializers
    queryset = ClassRoom.objects.all()
    
    def get(self, request, *args, **kwargs):
        params = request.query_params
        if 'teacher' in params:
            queryset = self.queryset.filter(teacher_course__teacher_name=params.get('teacher'))
        serializers = self.get_serializer(queryset, many=True)
        return Response(serializers.data)

class ClassRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomSerializers
    queryset = ClassRoom.objects.all()