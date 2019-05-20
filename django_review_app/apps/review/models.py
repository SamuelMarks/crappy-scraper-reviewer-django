# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import models
from six import itervalues, iterkeys


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    urls = models.TextField()
    named_entities = models.TextField()
    passed_review = models.BooleanField(default=False)

    class Meta:
        ordering = 'created',

    def __str__(self):
        return 'Review({title}, "{url_name}")'.format(title=self.title,
                                                    url_name=''.join(iterkeys(json.loads(self.urls))) if self.urls.startswith('{') else self.urls)

    __unicode__ = __str__
