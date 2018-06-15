from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from shorten_url.models import WebUrl



# Create your views here.
def index(request):
    urls = WebUrl.objects.order_by('-visit_count')[:5]
    return render(request, 'shorten_url/index.html', {'urls': urls})

def shorten(request):
    if request.method == 'POST':
        url = request.POST.get("url", '')
        
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError as e:
            print(e)

        try:
            get_url = WebUrl.objects.get(url=url)           
        except:

            short_url = shortened()
            new_url = WebUrl(url=url, short_url=short_url)
            new_url.save()
        
            return render(request, 'shorten_url/shortly.html', {'new_url': new_url})
        return render(request, 'shorten_url/shortly.html', {'new_url': get_url})    
    
    else:
         return render(request, 'shorten_url/shortly.html')   


def redirect_to_url(request, short_url):
    url = WebUrl.objects.get(short_url=short_url)
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
