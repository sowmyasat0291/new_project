from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
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
            from_email = 'your_custom_from_email@example.com'  # The desired "From" email address
            recipient_list = ['sowmyam0291@gmail.com']

            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    html_message=html
                )
                print('The form is valid and email was sent.')
                return redirect('index')
            except Exception as e:
                print(f'Error sending email: {e}')
                # Optionally, add error handling here
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form,
    })
