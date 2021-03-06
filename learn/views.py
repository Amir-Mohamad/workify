from typing import List
from django.shortcuts import render
from django.views.generic import ListView



# Showing the list of availabe courses
class CourseListView(ListView):
    queryset = Course.objects.filter(is_active=True)
    template_name = 'learn/course_list.html'