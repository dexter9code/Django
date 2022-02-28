from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page


@cache_page(5*60)
def say_hello(request):
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html', context={'name': 'rudy'})
    #     message.send(['doomdexter07@gmail.com'])
    # except BadHeaderError:
    #     pass
    response = requests.get('https://httpbin.org/delay/3')
    data = response.json()
    return render(request, 'hello.html', {'name': data})
