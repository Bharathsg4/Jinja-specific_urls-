from django.shortcuts import render

# Create your views here.
def Eng(request):
    E={'name':'England'}
    return render(request,'Team.html',context=E)