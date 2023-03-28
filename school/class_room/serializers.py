from rest_framework import serializers
from school.class_room.models import Student, Teacher, ClassRoom

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassRoomSerializers(serializers.ModelSerializer):
    # teacher_course = TeacherSerializers()
    class Meta:
        model = ClassRoom
        fields = ('id','room_name','teacher_course')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        teacher = TeacherSerializers(instance.teacher_course).data
        data['teacher_courser']=teacher
        return data
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)
