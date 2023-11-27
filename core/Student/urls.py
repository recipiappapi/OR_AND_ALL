from django.urls import path
from . import views


urlpatterns = [
    path('stu/<int:pk>',views.Student_list,name='student_data'),
    path('stu/',views.Student_list_all,name='student_data_all'),
    path('tec/<int:pk>',views.Teacher_list,name='teacher_data'),
    path('fil/',views.Student_Filter,name='StudentFilterData'),
]