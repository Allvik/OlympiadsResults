from django.contrib import admin
from django.urls import path
import flex.views

urlpatterns = [
    path('', flex.views.select_year),
    path('<year>/', flex.views.select_subject),
    path('<year>/<subject>/', flex.views.select_type),
    path('<year>/<subject>/<type>/', flex.views.select_stage),
    path('<year>/<subject>/<type>/<stage>/', flex.views.get_results),
    path('test', flex.views.test)
]
