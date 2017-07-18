from django.db import models

# Create your models here.


class Func(models.Model):
    byedited = models.ForeignKey('auth.User')
    content = models.TextField()
    modifiedtime = models.IntegerField()
    title = models.CharField(max_length=40)

    def dodaj_funkcje(self):
        self.save()
    
    def __str__(self):
        return self.title

