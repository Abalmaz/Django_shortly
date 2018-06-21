from django.shortcuts import render, get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from shorten_url.models import WebUrl
from shorten_url.forms import UrlForm
from django.views.generic import View

class UrlView(View):
    
    def get(self, request, pk=None):
        
        if not pk:
            urls = WebUrl.objects.order_by('-visit_count')[:5]
            form = UrlForm()
            return render(request, 'shorten_url/index.html', {'urls': urls, 'form': form})
        
        else:
        	url=get_object_or_404(WebUrl, pk=pk)
        	redirect('detail', pk=url.pk)
            
    
    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            try:
                new_url = WebUrl.objects.get(url=form.cleaned_data['url'])           
            except:
                new_url = form.save(commit=False)
                new_url.short_url = shortened()
                new_url.save()
            
            return redirect(detail, pk=new_url.pk)

        return render(request, 'shorten_url/index.html', {'urls': urls, 'form': form})

	
def detail(request, pk):
    url = get_object_or_404(WebUrl, pk=pk)
    return render(request, 'shorten_url/detail.html', {'url': url})  	


def redirect_to_url(request, short_url):
    try:
        url = WebUrl.objects.get(short_url=short_url)
    except:
        return HttpResponse('<h1>URL was found</h1>')	
    url.visit_count += 1
    url.save()
    return HttpResponseRedirect(url.url)


def shortened():
    while True:
        short_url = 'short.url.' + get_random_string(length=12)
        try:
            temp = WebUrl.objects.get(short_url=short_url)
        except:
            return short_url
