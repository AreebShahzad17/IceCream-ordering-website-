from django.db import models

# Create your models here.

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations
class Contact(models.Model):
    name = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.IntegerField()
    order = models.IntegerField(default="")
    image = models.ImageField(upload_to='pics/', default="")
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
