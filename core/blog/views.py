from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post

def indexView(request):
    '''
    A function based view to show index page
    '''
    name = 'ali'
    context = {"name":name}
    return render(request, "index.html",context)

class IndexView(TemplateView):
    '''
    A class base view to show index page
    '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["post"] = Post.object.all()
        return context