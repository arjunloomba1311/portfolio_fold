from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date_time = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.pub_date_time.strftime('%b %e %Y')
