from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'NeoTRAN',
            'year': 20,
            'codes': ['Python', 'Django', 'React'],
            'token': 'saodihaljkfhdaksdfhqpe8ur189y407328yr013243848'
        }
        return render(request, 'hello_world.html', context=data)