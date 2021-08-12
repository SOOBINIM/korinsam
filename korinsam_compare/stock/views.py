from django.http import HttpResponse
from django.shortcuts import render
import openpyxl
from .models import Product


def stockList(request):
    if request.method == 'GET':
        return render(request, 'stockList.html')
    
    if request.method == 'POST':
        return render(request,'stockList.html')



# def excel_crawling(reqeust):
    # data = openpyxl.load_workbook('C:\Program Files\dev\korinsam\korinsam_compare\stock\korinsam_insert_data_200921.xlsx')
    # sheet1 = data.get_sheet_by_name('Sheet1')
    # product_name_rows = sheet1['B2':'B26']
    # product_subject_rows = sheet1['C2':'C26']
    # print(product_name_rows)
    # return render(reqeust, 'stockList1.html', {'product_name_rows': product_name_rows})
# for row in rows:
#     for cell in row:
#         product = Product.objects.create(product_name = cell.value)
#         # product.save()
#         # print(cell.value)
    

