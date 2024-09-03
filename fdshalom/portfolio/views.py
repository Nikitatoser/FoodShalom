from django.shortcuts import render

from .models import Articles

from django.views.generic import DetailView

# Create your views here.
def portfolio(request):
    art = Articles.objects.all()
    return render(request, 'portfolio/portfolio.html', {'art': art})

class DetailView(DetailView):
	model = Articles
	template_name = 'portfolio/detail_view.html'
	
	context_object_name = 'article'
