from django import forms

class ContactForm(forms.Form):
    SERVICE_CHOICES = [
        ('', 'Select a Service'),
        ('photography', 'Photography'),
        ('videography', 'Videography'),
        ('editing', 'Post-Production / Editing'),
        ('design', 'Brand Design'),
        ('dj_services', 'DJ Services'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Full Name'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': '+61 4XX XXX XXX'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    service = forms.ChoiceField(choices=SERVICE_CHOICES, required=True)
    event_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'scheme-dark'}))
    budget = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'e.g., $2,000 - $5,000'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about your project or event visual direction...'}))