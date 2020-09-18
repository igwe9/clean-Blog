from django.urls import reverse
from django.utils.text import slugify
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(blank=True)
    def __str__(self):
        return self.name

class picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name



class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ForeignKey(picture, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(default="Type your message Here...", blank=True)
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = "Entries"

class post(models.Model):
    image = models.ImageField(blank=True, upload_to='pics')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=900)
    highlight = models.CharField(max_length=900, blank=True, default='')
    body = models.TextField(default="Type your message Here...")
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(post, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = "Post"
        ordering = ['-pub_date','id']
