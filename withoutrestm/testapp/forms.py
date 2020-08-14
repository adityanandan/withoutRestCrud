from django import forms
from testapp.models import Employee
class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        if inputsal<1000:
            raise forms.ValidationError('the minimum salary should be 1000')
        return inputsal
    class Meta:
        model=Employee
        fields='__all__'
