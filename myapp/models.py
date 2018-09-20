from django.db import models
from django.core.validators import RegexValidator

class Users(models.Model):
    alphanumeric = RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabet characters are allowed.')
    name =models.CharField(max_length=200,validators=[alphanumeric],null=False)
    email =models.EmailField(max_length=200,null=False)

    def __str__(self):
        return  self.name+" - "+self.email