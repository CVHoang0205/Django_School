from django.contrib import admin
from django.urls import path
from school.class_room.views import StudentList, StudentDetail, TeacherList, TeacherDetail, ClassRoomList, ClassRoomDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/', TeacherDetail.as_view()),
    path('classroom/', ClassRoomList.as_view()),
    path('classroom/<int:pk>/', ClassRoomDetail.as_view()),
]
