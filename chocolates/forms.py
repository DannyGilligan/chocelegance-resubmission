from django import forms
from .models import Chocolate, ChocolateCategory


class ChocolateForm(forms.ModelForm):

    # This inner Meta class defines the model and fields to use in the form
    class Meta:
        model = Chocolate
        # This dunder string will include all fields
        fields = '__all__'

    # Overrides the original __init__ method to make changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ChocolateCategory.objects.all()
        friendly_names = [(choc.id, choc.get_choc_friendly_name()) for choc in categories]
        # Updates the form to use the choc category friendly names instead of ids
        self.fields['category'].choices = friendly_names
        # Adds classes to the fields to allow styling for consistency
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded'