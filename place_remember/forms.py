from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Название места',
                           widget=forms.TextInput(attrs={'placeholder': 'Название места'})
                           )
    lat = forms.FloatField(required=True)
    lng = forms.FloatField(required=True)
    comment = forms.CharField(required=False, label='Комментарий места',
                              widget=forms.TextInput(attrs={'placeholder': 'Комментарий места'})
                              )