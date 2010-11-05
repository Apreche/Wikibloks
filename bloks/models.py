from django.db import models
from django.contrib.auth.models import User
from markitup.fields import MarkupField

class Blok(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='blok_owner')
    editors = models.ManyToManyField(User, related_name='blok_editors')
    create_time = models.DateTimeField()
    active = models.BooleanField()

class Revision(models.Model):
    blok = models.ForeignKey(Blok)
    number = models.PositiveIntegerField()
    time = models.DateTimeField()
    content = MarkupField()
    editor = models.ForeignKey(User, related_name='revision_editor')
    active = models.BooleanField()
