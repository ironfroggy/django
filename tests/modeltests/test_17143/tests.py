from __future__ import absolute_import

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import FieldDoesNotExist
from django.test import TestCase, skipIfDBFeature, skipUnlessDBFeature

from .models import A, B, init_effect


class ModelTest(TestCase):

    def _clear_init_effect(self):
        init_effect[:] = []

    def test_17143(self):
        b = B.objects.create(foo='Y', bar='Z')
        self.assertEqual(init_effect, ['Y'])
        self._clear_init_effect()

        (a,) = A.objects.select_related('b')
        self.assertEqual(a.id, b.id)
        self.assertEqual(init_effect, ['Y'])
        self._clear_init_effect()
