from django.forms import ModelForm
from faq.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "question"]
