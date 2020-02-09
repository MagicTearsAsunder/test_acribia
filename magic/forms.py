from django import forms
from .models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = '__all__'

    def clean(self):
        url = self.cleaned_data.get('url')
        if not url.endswith('/'):
            url += '/'
            self.cleaned_data['url'] = url
        return self.cleaned_data
