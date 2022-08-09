from django.test import TestCase
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
# Create your tests here.

def test_client(client, db):
    resposta = client.get(reverse('index'))
    assert resposta.status_code == 200

def test_oi():
    assert 1 == 1


def test_template_index(client, db):
    resposta = client.get(reverse('index'))
    assertTemplateUsed(resposta, 'index.html')

def test_link_pro_staff(client,db):
    resposta = client.get(reverse('index'))
    assert 'cep'.encode() in resposta.content