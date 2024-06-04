from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Allows for the customisation of the image input field in
    the form by overriding the original options
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'chocolates/custom_widget_templates/custom_clearable_file_input.html'