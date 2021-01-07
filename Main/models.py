from django.db import models


# Create your models here.

# Handles Response Message
class ResponseMessage(models.Model):
    name = models.CharField(max_length=220)
    email = models.EmailField()
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Time')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Response Message"
        verbose_name_plural = "Response Messages"
        ordering = ('-time_stamp',)


# Panel Members Post
class PanelPost(models.Model):
    post_name = models.CharField(max_length=120)

    def __str__(self):
        return self.post_name


# Panel Members
class PanelMember(models.Model):
    name = models.CharField(max_length=220)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    picture = models.ImageField(upload_to='panel/members')
    social_link = models.URLField(blank=True)
    email = models.EmailField()
    post = models.ForeignKey(to=PanelPost, null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=20)
    post_type_choice = [
        (1, 'Moderator'),
        (2, 'Administrator'),
        (3, 'Co-Administrator'),
        (4, 'General Secretary'),
        (5, "Assistant Secretary"),
        (6, "Sector Lead"),
        (6, "Sector Co Lead"),
    ]
    post_type = models.SmallIntegerField(choices=post_type_choice)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year_start', 'post_type')


# Pages
class PortfolioPage(models.Model):
    page_name = models.CharField(max_length=220, unique=True)
    title = models.CharField(max_length=220)


# Page Paragraph
class PageParagraph(models.Model):
    page = models.ForeignKey(to=PortfolioPage, on_delete=models.SET_NULL, null=True, blank=True)
    block_title = models.CharField(max_length=220, unique=True)
    heading = models.TextField()
    paragraph = models.TextField()
