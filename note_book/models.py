from django.db import models
from django.conf import settings
# Create your models here.
class Level(models.Model):
    level_name =models.CharField(blank=True, null=True, max_length=100)
    
    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"
        ordering = ["-level_name"]
    def __str__(self):
        return self.level_name
    
class Semester(models.Model):
    level=models.ForeignKey(Level, on_delete=models.CASCADE)
    semester_name =models.CharField(blank=True, null=True, max_length=100)
    
    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"
        ordering = ["-semester_name"]
    def __str__(self):
        return self.semester_name
    
class NoteBook(models.Model):
    file_upload=models.FileField(upload_to="note_upload/", blank=False, null=False)
    course_name=models.CharField(max_length=100)
    level_id=models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    semester_id=models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)