from django.db import models
from django.conf import settings


# Create your models here.
class CollegeDetail(models.Model):
    picture =models.ImageField(upload_to="college_picture/", blank=False, null=False)
    college_name = models.CharField(max_length=250, blank=False, null=False )
    address = models.CharField(max_length=100, blank=True, null=True )
    contact = models.CharField(max_length=100, blank=True, null=True )
    website = models.CharField(max_length=100, blank=True, null=True )
    program = models.CharField(max_length=250, blank=False, null=False )
    description = models.TextField(max_length=250, blank=False, null=False )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )