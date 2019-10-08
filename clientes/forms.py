from django.forms import ModelForm
from .models import Person

#https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','age','salary','bio','photo']