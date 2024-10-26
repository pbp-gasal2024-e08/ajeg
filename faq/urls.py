from django.urls import path
from faq.views import view_faq, add_question_ajax, show_json

app_name = 'faq'

urlpatterns = [
    path('view-faq/', view_faq, name='view_faq'),
    path('json/', show_json, name='show_json'),
    path('create-question-ajax', add_question_ajax, name='add_question_ajax'),
]