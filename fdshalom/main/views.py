from django.shortcuts import render

from .models import Person

def index(request):
    return render(request, 'main/index.html')

def about(request):
    man = Person.objects.first()
    return render(request, 'main/about.html', {'man': man})


from django.shortcuts import render, redirect
from .models import Articles, Rates
from .forms import RatesForm

def rate(request):
    form = RatesForm()  # Виправлення: виклик форми з дужками

    error = ''
    if request.method == 'POST':
        form = RatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
        else:
            error = 'Form is incorect'  # Виправлено текст повідомлення

    data = {
        'form': form,
        'error': error  # Передаємо повідомлення про помилку в шаблон
    }
    
    return render(request, 'main/rate.html', data)
