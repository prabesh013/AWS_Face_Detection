from django.db import models
import os


# counter = 1
def content_file_name(instance, filename):
    # print(instance.pk)
    # print(help(instance))
    # ext = filename.split('.')[-1]
    # global counter
    # filename = "%s.%s" % (str(instance.id), ext)
    # counter = counter + 1
    return os.path.join('images', filename)

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to=content_file_name)
