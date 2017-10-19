from django import forms

class NewSession(forms.Form):
    response = forms.BooleanField(initial=False, required=False)

    def clean_response(self):
        data = self.cleaned_data['response']

        return data
