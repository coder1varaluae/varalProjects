from django.db import models


class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='Naming/files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)

# Create your models here.
class Form_Name(models.Model):
    Jurisdiction = models.CharField(max_length = 200)
    Formname = models.CharField(max_length = 200)
    #
    # def __str__(self):
    #     formName = self.Jurisdiction + "-" + self.Formname
    #     return formName
