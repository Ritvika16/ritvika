# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
USER_CHOICES = (
    ('librarian','LIBRARIAN'),
    ('student', 'STUDENT'),
)

class User(models.Model):
	Name = models.CharField(max_length=50)
	username = models.CharField(max_length=50, blank=False)
	password = models.CharField(max_length=50, blank=False)
	contact = models.CharField(max_length=50)
	user_type = models.CharField(max_length=50, choices=USER_CHOICES, default='student')

	def __str__(self):
		return self.username + " " +self.password 

class Books(models.Model):
	book_name = models.CharField(max_length=50)
	author_name = models.CharField(max_length=50)
	rating = models.CharField(max_length=50)
	summary = models.CharField(max_length=500)
	copies = models.IntegerField()

	def __str__(self):
		return self.book_name

class BookIssue(models.Model):
	BookName = models.ForeignKey(Books)
	StudentName = models.ForeignKey(User)
	Bookstatus = models.CharField(max_length=50, choices=USER_CHOICES, default='student')
	IssueDate = models.DateField(null=True)
	DaysLeft = models.IntegerField(default=0)

	def __str__(self):
		return self.BookName.book_name
