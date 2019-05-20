# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django_review_app.apps.review.models import Review

admin.site.register(Review)
