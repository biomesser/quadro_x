from django.shortcuts import render

# Create your views here.

def quadro_abc(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        my_x = 'Дискриминант < 0, уравнение не имеет решений'
        return my_x
    if discriminant == 0:
        my_x = -b / (2*a)
        return str('Дискриминант = 0, X =', int(my_x))
    if discriminant > 0:
        my_x_1 = (-b + discriminant) / 2*a
        my_x_2 = (-b - discriminant) / 2*a
        return str('Дискриминант > 0, уравнение имеет два решения:  ' + 'X = ' + str(int(my_x_1)) + ' и ' + 'X = ' + str(int(my_x_2)))

def about(request):
    context = {}

    if request.method == 'POST':
        try:
            int(request.POST['a']) or int(request.POST['b']) or int(request.POST['c'])
        except Exception:
            return render(request, 'quadro/page_repeat.html')
        a = request.POST['a']
        if int(a) == 0:
            return render(request, 'quadro/a_zero_page.html')
        b = request.POST['b']
        c = request.POST['c']
        res = quadro_abc(int(a), int(b), int(c))
        context = {'my_x': str(res)}
    else:
        pass
    print(context)
    return render(request, 'quadro/page.html', context)

