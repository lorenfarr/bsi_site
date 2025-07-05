# Views for main app
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """Home page view"""
    context = {
        'title': 'Bright Stead Insurance - Protecting Your Future',
        'description': 'Comprehensive life and health insurance solutions for you and your family.',
    }
    return render(request, 'main/home.html', context)

def life_insurance(request):
    """Life insurance page view"""
    context = {
        'title': 'Life Insurance - Bright Stead Insurance',
        'description': 'Protect your family\'s future with our comprehensive life insurance coverage.',
    }
    return render(request, 'main/life_insurance.html', context)

def health_insurance(request):
    """Health insurance page view"""
    context = {
        'title': 'Health Insurance - Bright Stead Insurance',
        'description': 'Secure your health with our comprehensive health insurance plans.',
    }
    return render(request, 'main/health_insurance.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Send email (configure email settings in production)
        try:
            send_mail(
                f'Contact Form - {name}',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                ['info@brightsteadinsurance.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your message! We\'ll get back to you soon.')
        except Exception as e:
            messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
    
    context = {
        'title': 'Contact Us - Bright Stead Insurance',
        'description': 'Get in touch with Bright Stead Insurance for all your insurance needs.',
    }
    return render(request, 'main/contact.html', context)

def privacy_policy(request):
    """Privacy policy page view"""
    context = {
        'title': 'Privacy Policy - Bright Stead Insurance',
    }
    return render(request, 'main/privacy_policy.html', context)

def terms_of_use(request):
    """Terms of use page view"""
    context = {
        'title': 'Terms of Use - Bright Stead Insurance',
    }
    return render(request, 'main/terms_of_use.html', context)

def quote(request):
    """Quote request page view"""
    if request.method == 'POST':
        # Handle quote form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        insurance_type = request.POST.get('insurance_type')
        coverage_amount = request.POST.get('coverage_amount')
        
        # Process quote request (save to database, send email, etc.)
        messages.success(request, 'Quote request submitted! We\'ll contact you within 24 hours.')
    
    context = {
        'title': 'Get a Quote - Bright Stead Insurance',
        'description': 'Get a personalized insurance quote tailored to your needs.',
    }
    return render(request, 'main/quote.html', context)