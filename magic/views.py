import asyncio
from rest_framework import viewsets
from django.shortcuts import render
from .forms import UrlForm
from .models import Response, Url
from . import exists_directory
from .serializers import ResponseSerializer, UrlSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


def index(request):
    form = UrlForm(request.POST or None)

    if form.is_valid():
        form.save()
        url = form.cleaned_data.get('url')
        asyncio.run(exists_directory.main(url))

    return render(request, 'magic/index.html', context={'form': form})
