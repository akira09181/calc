from django.shortcuts import render

# Create your views here.


def index(request):
    result = 0
    context = {'result': result}
    return render(request, 'calculation/index.html', context)


def calc(request):
    first = request.GET.get('first')
    second = request.GET.get('second')
    result = int(first)+int(second)
    context = {'result': result}
    return render(request, 'calculation/index.html', context)
