from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse
from django.conf import settings

# Define a test for our add endpoint
def test_add():
    print(settings.BASE_DIR)
    client = Client()
    response = client.post(reverse(viewname='add'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')
    #print(num01)
    print("Hi", response)
    assert response.status_code == 200 and float(response.content) == 3, settings.BASE_DIR