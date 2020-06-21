import csv

from django.shortcuts import render
from django.views.generic import View
from django.db import connection
from django.apps import apps
from django.http import HttpResponse
from django.conf import settings
from .databaseInterpreter import select_all_tasks, insert_data_into_table, TruncateTableData

import pandas as pd

# Create your views here.

class GetTableData(View):
    def get(self,request):
        table_info = []
        tables = connection.introspection.table_names()
        for model in apps.get_models():
            if model._meta.proxy: continue

            table = model._meta.db_table
            if table not in tables: continue

            columns = [field.column for field in model._meta.fields]
            table_info.append((table, columns))

        return render(
            request=request,
            template_name="homepage.html",
            context={
                "tableNames": tables,
            }
        )

    def post(self,request):
        table_name = request.POST.get('tableName')
        rows = select_all_tasks("SELECT * FROM {}".format(table_name))

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(table_name)

        writer = csv.writer(response)
        writer.writerow(rows[0])

        for row in rows[1:]:
            writer.writerow(row)

        return response

class GetTableTemplate(View):
    def post(self,request):
        table_name = request.POST.get('tableName')
        rows = select_all_tasks("SELECT * FROM {}".format(table_name))

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}_Template.csv"'.format(table_name)

        writer = csv.writer(response)
        writer.writerow(rows[0])

        return response

class ImportExcelData(View):
    def post(self, request):
        table_name = request.POST.get('tableName')
        truncate = request.POST.get('truncate')

        global temp_msg
        temp_msg = ''
        if truncate == 'on':
            state = TruncateTableData(table_name)
            if state: temp_msg = 'Table truncate done. '
            else: 'Table truncate Failed'
        excel_file = request.FILES['myfile']
        data = pd.read_csv(excel_file)
        values = []
        for row in data.values:
            values.append(tuple(row))

        try:
            rows_affected = insert_data_into_table(
                table_name= table_name,
                column_names=tuple(data),
                values=values
            )
            message = temp_msg+"{} rows has been affected on {} table.".format(rows_affected,table_name)
        except Exception as e:
            message = temp_msg+"ERROR: {}".format(e)

        tables = connection.introspection.table_names()
        return render(
            request=request,
            template_name="homepage.html",
            context={
                "tableNames": tables,
                "message": message,
            }
        )
