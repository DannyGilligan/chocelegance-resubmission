from django import forms
from .widgets import CustomClearableFileInput
from .models import Chocolate, ChocolateCategory


class ChocolateForm(forms.ModelForm):

    # This inner Meta class defines the model and fields to use in the form
    class Meta:
        model = Chocolate
        # This dunder string will include all fields
        fields = '__all__'

    choc_image = forms.ImageField(label='Image',
                                  required=False,
                                  widget=CustomClearableFileInput)

    # Overrides the original __init__ method to make changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ChocolateCategory.objects.all()
        friendly_names = \
            [(choc.id, choc.get_choc_friendly_name()) for choc in categories]
        # Updates the form to use choc category friendly names instead of ids
        self.fields['choc_category_display'].choices = friendly_names
        # Adds classes to the fields to allow styling for consistency
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple \
border-radius-10 purple-text'
