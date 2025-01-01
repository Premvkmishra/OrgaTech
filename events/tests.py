from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(name="Sample Event", address="123 Sample St", date="2023-10-01", time="12:00", phone="1234567890")

    def test_event_content(self):
        event = Event.objects.get(id=1)
        expected_object_name = f'{event.name}'
        self.assertEqual(expected_object_name, 'Sample Event')