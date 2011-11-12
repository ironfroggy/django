# coding: utf-8
"""
1. Bare-bones model

This is a basic model with only two non-primary-key fields.
"""
from django.db import models


init_effect = []


class A(models.Model):
    foo = models.CharField(max_length=1, default='N')
    
    def __init__(self, *args, **kwargs):
        super(A, self).__init__(*args, **kwargs)
        
        init_effect.append(self.foo)
    
class B(A):
    bar = models.CharField(max_length=1, default='X')
