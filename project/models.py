from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from chat.models import Room
import haikunator
from django.db import transaction


class Project(models.Model):
    owners = models.ForeignKey(User, related_name="Owner")
    projectManager = models.ForeignKey(User, related_name="Project_Manager")
    projectName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    room = models.OneToOneField(Room,related_name="Chat_room",null=True,blank=True)

    def save(self, *args, **kwargs):

        room = self.createChatRoom()
        self.room = room
        print(self.room.label)
        super(Project, self).save(*args, **kwargs)


    def createChatRoom(self):
        new_room = None
        while not new_room:
            with transaction.atomic():
                import random
                import  string
                label = "".join( [random.choice(string.letters) for i in xrange(15)] )
                if Room.objects.filter(label=label).exists():
                    continue
                new_room = Room.objects.create(label=label)
        return new_room