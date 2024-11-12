"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django import views
from django.contrib import admin
from django.urls import path
from graphviz import view
from usecase import views as usecase
from usecase import views as usecase_views

# from usecase.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usecase.UseCaseDiagram, name='UseCaseDiagram'),
    path('generate/', usecase.use_case_result, name='use_case_result'),
    path('generate_use_case/', usecase.generate_use_case_diagram, name='generate_use_case_diagram'),
    path('specification', usecase.Specification, name='Specification'),
    path('output-activity/', usecase.output_activity, name='output_activity'),
    path('inputclass/', usecase.input_class, name='input_class'),
    path('inputsequence/', usecase.input_sequence, name='input_sequence'),
    path('outputclass/', usecase.output_class, name='output_class'),
    path('outputsequence/', usecase.output_sequence, name='output_sequence'),
    path('use-case-result/', usecase.use_case_result, name='use_case_result'),
    path('serve-use-case-diagram/', usecase.serve_use_case_diagram, name='serve_use_case_diagram'),
    # path('use_case_output/', usecase_views.use_case_output, name='use_case_output'),  # Pastikan import sesuai
]
