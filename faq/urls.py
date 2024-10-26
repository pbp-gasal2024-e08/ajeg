from django.urls import path
from faq.views import view_faq, add_question_ajax, show_json, get_questions

app_name = 'faq'

urlpatterns = [
    path('view-faq/', view_faq, name='view_faq'),
    path('view-faq/json/', show_json, name='show_json'),
    path('view-faq/create-question-ajax', add_question_ajax, name='add_question_ajax'),
    path('view-faq/get-questions/', get_questions, name="get_questions"),
]