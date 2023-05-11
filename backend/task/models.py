from django.db import models
from users.models import User
from projects.models import ProjectDetails
# Create your models here.

class TaskData(models.Model):
    project_name = models.CharField(max_length=50)
    task_title = models.CharField(max_length=65)
    task_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='person_created')
    assigned_to = models.ForeignKey(User, models.DO_NOTHING, related_name='person_assigened_to')
    assigned_by = models.ForeignKey(User, models.DO_NOTHING, related_name='person_assigned_by')
    deadline = models.DateTimeField()
    updated_by = models.ForeignKey(User, models.DO_NOTHING)

    def __str__(self):
        return self.project_name
    
class TaskComment(models.Model):
    task = models.ForeignKey(TaskData, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(ProjectDetails, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment_body = models.TextField()

    def __str__(self):
        return self.project + ": " + self.task