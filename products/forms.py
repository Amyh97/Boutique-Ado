from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # include all fields
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            # list comprehention, shorthand for loop to += a list
            friendly_names = [(c.id, c.get_friendly_name())
                              for c in categories]

            # to use friendly names rather than ids
            self.fields['category'].choices = friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'
