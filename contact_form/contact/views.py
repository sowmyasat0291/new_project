from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            
            contact = form.save(commit=False)  # Create a model instance but don't save yet
            contact.save()  # Save the instance to the database
            
            # Send an email

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Render the HTML message
            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            # Define the "From" email address and recipient list
            from_email = 'noreply.271807@gmail.com'  # The desired "From" email address
            recipient_list = ['sowmyam0291@gmail.com']

            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    html_message=html
                )
                return render(request, 'contact/confirmation.html', {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message,
                })
            except Exception as e:
                print(f'Error sending email: {e}')
                # Optionally, add error handling here
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form,
    })
