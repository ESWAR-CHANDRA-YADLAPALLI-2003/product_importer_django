from django import forms
from .models import Webhook

class WebhookForm(forms.ModelForm):
    class Meta:
        model = Webhook
        fields = ['url', 'event_type', 'active']

# Add this
class UploadFileForm(forms.Form):
    file = forms.FileField(label="Select a CSV file")
