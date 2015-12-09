
from blog.models import BlogPost
f = open("E:\\bak\\sql.txt", "r")
for line in f:
   content=line.split(",");
   print content[0],content[2]
   p1=BlogPost(title=content[0],content=content[1],timestamp=content[2])
   p1.save()
f.close()
