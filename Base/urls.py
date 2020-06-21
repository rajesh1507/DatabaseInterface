"""Base URL Configuration"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', GetTableData.as_view(), name = "getTableData"),
    path('template/', GetTableTemplate.as_view(), name = "getTableTemplate"),
    path('import/', ImportExcelData.as_view(), name = "ImportTableData"),
]
