from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #form.save()
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            messages.success(request, 'Submitted Successfully')

            try:
                send_mail(subject, message, 'adeyeye1034@gmail.com', ['adeyeye1034@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("base:home")
    form = ContactForm()
    return render(request, "base/contact.html", {'form':form})
