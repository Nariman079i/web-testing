from django.db.models import *

# Create your models here.
class Test(Model):
    title = CharField(max_length=30)
    