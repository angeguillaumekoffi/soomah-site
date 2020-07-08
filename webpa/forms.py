from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from Infos import models

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.fields['email'].required = True
        self.fields['message'].required = True
        self.helper.layout = Layout(
            Field("nom"),
            Field("email"),
            Field("objet"),
            Field("message"),
            Submit("update", "Envoyer", css_class="btn-danger"),
        )

    class Meta:
        model = models.Contacts
        fields = ["nom", "email", "objet", "message"]