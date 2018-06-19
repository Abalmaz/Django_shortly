from django.forms import ModelForm
from shorten_url.models import WebUrl

class UrlForm(ModelForm):
	class Meta:
		model = WebUrl
		fields = ['url']