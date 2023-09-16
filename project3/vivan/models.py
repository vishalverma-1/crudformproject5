from django.db import models
class mahak(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    def __str__(self):
        return self.name

