from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError


def say_hello(request):
    try:
        send_mail('subject', 'this is first plain text message',
                  'info@valorant.com', ['bob@buidler.com'])
    except:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
