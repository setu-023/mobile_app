from django.db import models

class Mobile(models.Model):

    brand_name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    jan_code = models.IntegerField(unique=True)
    image      = models.ImageField(null=True,upload_to='media')

    status     = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        data = str(self.jan_code) + " " + self.model + " " + self.brand_name
        return (data)