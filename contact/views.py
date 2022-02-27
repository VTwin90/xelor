from django.shortcuts import (
    render, redirect, reverse
)

from django.contrib import messages
from profiles.models import UserProfile
from .forms import ContactForm


def contact(request):
    """ A view to return the contact us page """

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            form.save()
            request.session['save_info'] = 'save-info' in request.POST
            messages.success(request, 'Successfully sent message,'
                             'we will be in touch with you soon!')
        else:
            messages.error(request, 'Failed to send message.'
                           'Please ensure the form is valid.')

    if request.user.is_authenticated:
        contact_form = ContactForm(initial={
            'full_name': request.user.username,
            'email': request.user.email,
        })
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
