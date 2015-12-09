
from django.conf import settings
settings.configure()

#from models import BlogPost
from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
if __name__ == "__main__":
    f = open("E:\\bak\\sql.txt", "r")
    for line in f:
       content=line.split(",");
       print content[0],content[2]
       p1=BlogPost(title=content[0],content=content[1],timestamp=content[2])
       p1.save()
    f.close()
