from rest_framework.generics import *
from django.shortcuts import render
from main.serializers import *

class TestApi(ListAPIView):
    serializer_class = TestSerialisers
    queryset = Test.objects.all()

class QuetionApi(ListAPIView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Question.objects.filter(test_id=pk)

    serializer_class = QuestionSerializer

def TestView(request):
    context = {

    }
    test = Test.objects.all()
    context['test'] = test
    temp = 'main/index.html'
    return render(request, temp, context=context)

def QuestionView(request, id):
    context = {

    }
    test = Question.objects.filter(test_id=id)
    context['quetions'] = test
    context['test_title'] = Test.objects.get(id=id)
    temp = 'main/quetion.html'
    
    return render(request, temp, context=context)