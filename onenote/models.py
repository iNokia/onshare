# coding: UTF-8
from django.contrib.auth.models import User
from django.db import models

# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     avatar = models.ImageField()
#     name = models.CharField()
#     description = models.TextField()

class BlogPost(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
    )
    title = models.CharField(max_length=150)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    def __str__(self):
        return '%s, %s' % (self.user.username, self.title)

class Collection(models.Model):
    name = models.CharField(max_length=150, unique=True)
    desc = models.TextField()
    user = models.ForeignKey(User)
    def __str__(self):
        return '%s, %s' % (self.user.username, self.name)

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    blogposts = models.ManyToManyField(BlogPost)
    collections = models.ManyToManyField(Collection)
    def __str__(self):
        return self.name

class Followingship(models.Model):
    following = models.ForeignKey(
        User, related_name='following_set'
        )
    followers = models.ForeignKey(
        User, related_name='followers_set')
    def __unicode__(self):
        return u'%s, %s' % (self.following.username,
            self.followers.username)
    class Meta:
        unique_together = (('followers', 'following'), )
