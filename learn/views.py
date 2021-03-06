from typing import List
from django.shortcuts import render
from django.views.generic import ListView


class CourseListView(ListView):
    queryset = Course.objects.filter(is_active=True)
    template_name = 'learn/course_list.html'