from django.shortcuts import render
from .models import Board


def board_list(request):
    boards = Board.objects.all().order_by('-no')
    return render(request, 'stockList.html', {'boards' : boards})


# def stockList(request):
#     if request.method == 'GET':
#         return render(request, 'stockList.html')
    
#     if request.method == 'POST':
#         return render(request,'stockList.html')