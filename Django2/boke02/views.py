from django.shortcuts import render


# Create your views here.
# 富文本
def edit(request):
    return render(request, 'edit.html')


# def kind(request):
#     return render(request, 'kindeditor.html')
