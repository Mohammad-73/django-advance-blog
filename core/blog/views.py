from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404

# def indexView(request):
#     '''
#     A function based view to show index page
#     '''
#     name = 'ali'
#     context = {"name":name}
#     return render(request, "index.html",context)

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
    
# from django.shourtcuts import redirect
# def redirectToMaktab(request):
#     return redirect('https://maktabkhooneh.com')

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostList(ListView):
    # model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts