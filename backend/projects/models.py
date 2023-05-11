from django.db import models

# Create your models here.


class ProjectDetails(models.Model):
    title = models.CharField(max_length=30, blank=True)
    logo = models.ImageField(upload_to='project/images')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    projects_file = models.FileField(upload_to='project/file',)

    # assign_by = models.IntegerField()   # fk
    # assign_to = models.IntegerField()   # fk
