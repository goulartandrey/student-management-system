from django.urls import path
from students.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('login', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('student/<int:id>', view_student, name='view_student'),
    path('student/add', add, name='add'),
    path('student/<int:id>/edit', edit, name='edit'),
    path('student/<int:id>/delete', delete, name='delete')
]
