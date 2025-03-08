from django.forms.widgets import RadioSelect
from django.db import models

# customn field on admin
class CustomBooleanFeild(models.BooleanField):
    def formfield(self, **kwargs):
        kwargs['widget'] = RadioSelect(choices=((True, 'Có'), (False, 'Không')))
        kwargs['initial'] = False

        return super().formfield(**kwargs)