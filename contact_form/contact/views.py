from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()  # Save the instance to the database
            # Redirect to the confirmation page with the contact's ID
            return redirect('confirmation', contact_id=contact.id)
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form,
    })

def confirmation(request, contact_id):
    # Retrieve the specific contact record from the database using its ID
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact/confirmation.html', {
        'contact': contact,
    })

def all_contacts(request):
    # Retrieve all contact records from the database
    contacts = Contact.objects.all()
    return render(request, 'contact/all_contacts.html', {
        'contacts': contacts,
    })
