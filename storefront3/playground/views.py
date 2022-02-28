from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import logging

logger = logging.getLogger(__name__)


def say_hello(request):
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html', context={'name': 'rudy'})
    #     message.send(['doomdexter07@gmail.com'])
    # except BadHeaderError:
    #     pass
    try:
        logger.info('calling the webserver')
        response = requests.get('https://httpbin.org/delay/3')
        logger.info('recived reponse after a delay')
        data = response.json()
    except requests.ConnectionError:
        logger.critical('webserver is currently out-of-permisses')
    return render(request, 'hello.html', {'name': data})
