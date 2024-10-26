from django.urls import path
from .views import create_announcement_ajax, delete_announcement, edit_announcement, get_announcement_by_id, get_announcements_by_store

app_name = 'announcement'

urlpatterns = [
  path('create', create_announcement_ajax, name='create_announcement_ajax'),
  path('<str:id>', get_announcement_by_id, name='get_announcement_by_id'),
  path('store/<str:store_id>', get_announcements_by_store, name='get_announcements_by_store'),
  path('edit/<uuid:id>', edit_announcement, name='edit_announcement'),
  path('delete/<uuid:id>', delete_announcement, name='delete_announcement'),
]