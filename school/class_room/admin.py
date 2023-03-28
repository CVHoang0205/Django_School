from django.contrib import admin
from school.class_room.models import Student, Teacher, ClassRoom

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'teacher_course')
    search_fields=['room_name','teacher_course__teacher_name']
    list_filter=['room_name', 'teacher_course']
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ClassRoom,ClassRoomAdmin)

