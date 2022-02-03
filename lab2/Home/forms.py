from django import forms
from .models import Intake
class AddUserForm(forms.Form):
    name = forms.CharField(label='USERNAME', max_length=100)
    IntakeF = forms.ChoiceField(choices=[(intake.id, intake.name) for intake in Intake.objects.all()])
    #forms.ChoiceField(choices=[(IntakeM.id, IntakeM.name) for intake in IntakeM.objects.all()])
    #forms.CharField(label='INTAKE', max_length=100)
    password = forms.CharField(label='PASSWORD', max_length=100)

class AddUserFormModel(forms.ModelForm):

    class Meta:
        fields = '__all__'  # ['fullname','trackid']#'__all__'
        # exclude=['bdate']
        model = Intake