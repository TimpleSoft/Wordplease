# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User



class Category (models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name



class Post (models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    abstract = models.CharField(max_length=300)
    body = models.TextField()
    imageUrl = models.URLField(blank=True, null=True)
    publication_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


