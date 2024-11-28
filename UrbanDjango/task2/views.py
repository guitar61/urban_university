from django.shortcuts import render
from django.views.generic import TemplateView

# Function-Based View
def function_view(request):
    return render(request, 'second_task/function_template.html')

# Class-Based View
class ClassView(TemplateView):
    template_name = 'second_task/class_template.html'
