from django.db import models
#set status of post
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here. 
#post -> title,slug, update and created on datetimes, status
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title