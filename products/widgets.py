from django.forms.widgets import ClearableFileInput
# the as _ means we can call this function with _
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    # come from Django github, overriding them here
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
