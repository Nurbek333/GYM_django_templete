from django.db import models


#Tranier

class Trainer(models.Model):
    full_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="Trainer/")
    facebook = models.CharField(max_length=70)
    intagram = models.CharField(max_length=70)
    twitter = models.CharField(max_length=70)



class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.name