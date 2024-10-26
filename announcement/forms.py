from django.forms import ModelForm
from .models import Announcement
from django.utils.html import strip_tags

class AnnouncementForm(ModelForm):
  class Meta:
    model = Announcement
    fields = ['title', 'description']
  
  def clean_title(self):
    title = self.cleaned_data['title']
    return strip_tags(title)

  def clean_description(self):
    description = self.cleaned_data['description']
    return strip_tags(description)