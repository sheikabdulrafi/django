from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import Service, Blog, Career
from django.core.mail import send_mail
from django.http import HttpResponse
import logging
import socket

# Set up logging
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, 'index.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def careers(request):
    careers = Career.objects.all()
    return render(request, 'career.html', {'careers': careers})


@csrf_protect
def sendRequest(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        message = request.POST.get('message')

        name = f"{first_name} {last_name}"
        subject = 'Contact Form Submission'
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                email,  # Sender email
                ['sheikabdulraffi@gmail.com'],  # Replace with the recipient's email address
            )
            logger.info("Sent mail successfully")
            return redirect('/')
        except socket.error as e:
            if e.errno == 32:  # Broken pipe error
                logger.error(f"Broken pipe error: {e}")
            else:
                logger.error(f"Socket error: {e}")
            return render(request, 'index.html', {'error': 'Failed to send your message due to a network error. Please try again later.'})
        except Exception as e:
            logger.error(f"Failed to send mail: {e}")
            return render(request, 'index.html', {'error': 'Failed to send your message. Please try again later.'})

    return render(request, 'index.html')
