from django.db import models

class WorkList(models.Model):
    id = models.BigAutoField(primary_key=True)
    work = models.CharField()
    complete = models.BooleanField()
