from django import forms
from .models import Profile, Medicine, Collection


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['BioText', 'City', 'DateOfBirth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['Medicine', 'user', 'Date', 'Collected', 'CollectedApproved', 'CollectedApprovedBy']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'})
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['Name', 'Manufacturer', 'Cures', 'SideEffects']
