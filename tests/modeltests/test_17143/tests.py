from __future__ import absolute_import

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import FieldDoesNotExist
from django.test import TestCase, skipIfDBFeature, skipUnlessDBFeature

from .models import A, B, init_effect


class ModelTest(TestCase):

    def setUp(self):
        self.b = B.objects.create(foo='Y', bar='Z')

    def tearDown(self):
        init_effect[:] = []

    def test_17143_1(self):
        self.assertEqual(init_effect, ['Y'])

    def test_17143_2(self):
        a = A.objects.get()
        self.assertEqual(init_effect, ['Y'])

    def test_17143_3(self):
        a = A.objects.get()
        b = a.b
        self.assertEqual(b.foo, a.foo)
        self.assertEqual(init_effect, ['Y'])

    def test_17143_4(self):
        (a,) = A.objects.select_related('b')
        self.assertEqual(a.id, self.b.id)
        self.assertEqual(init_effect, ['Y'])
