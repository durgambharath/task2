from django import forms
from funds.models import task2_funds
class task2_fundsForm(forms.ModelForm):
    class Meta:
        model = task2_funds
        fields = "__all__"
