from django.db.models import *

# Create your models here.
class Test(Model):
    title = CharField(max_length=120)

    def __str__(self) -> str:
        return self.title

class Question(Model):
    test_id = ForeignKey(Test, on_delete=CASCADE)
    title = CharField(max_length=255)
    variant_out_put_1 = CharField(max_length=255,null=False)
    variant_out_put_2 = CharField(max_length=255,null=False)
    variant_out_put_3 = CharField(max_length=255,null=True)
    variant_out_put_4 = CharField(max_length=255,null=True)
    out_put = IntegerField()

    def __str__(self) -> str:
        return self.title

