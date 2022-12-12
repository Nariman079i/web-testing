from rest_framework.serializers import *
from main.models import *
class TestSerialisers(ModelSerializer):
    
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    test_id = TestSerialisers(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
    