from django import forms
from addcandidates_app.models import AddCandidate

class DocumentForm(forms.ModelForm):
    class Meta:
        model = AddCandidate
        fields = "__all__"
