from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('customer_email')
        message = cleaned_data.get('message')

        # Ejemplo de validación no asociada a un campo específico
        if email and "example.com" in email and message and "test" in message:
            self.add_error(None, "No puedes usar 'example.com' en el correo electrónico si el mensaje contiene 'test'.")

        return cleaned_data
