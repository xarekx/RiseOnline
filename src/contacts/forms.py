from django import forms
from contacts.models import Contact


class ContactForm(forms.ModelForm):

    msg_title = forms.CharField(max_length=64, required=True, help_text='Type your message title', label="Title",widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'flex text-2xs md:text-xs h-fit w-full'}))
    msg_type = forms.CharField(max_length=16, required=True, help_text='Choose your message subject', widget=forms.Select(choices=Contact.MSG_TYPE_CHOICES, attrs={'class': 'flex text-2xs md:text-xs h-fit w-full'}), label="Subject")
    msg_description = forms.CharField(max_length=500, help_text='Type what you want to tell me', label="Description",widget=forms.Textarea(attrs={'class': 'text-2xs md:text-xs w-full'}))


    class Meta:
        model = Contact
        fields = [ 
                  'msg_title',
                  'msg_type',
                  'msg_description'
        ]