from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    """ A view to return the contact us page """

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
    
        if form.is_valid():
            messages.success(request, 'Successfully sent message, we will be in touch with you soon!')
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')

    contact_form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)