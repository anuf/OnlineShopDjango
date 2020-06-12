from django.db import models

# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=30, verbose_name="The Name")  # Change the name to be seen on admin panel
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)  # Make field not required
    phone = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Articles(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return("The name is: {}:: Section: {} :: Price: {}".format(self.name,
                                                                 self.section,
                                                                 self.price))


class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()

    def __str__(self):
        return str(self.number)