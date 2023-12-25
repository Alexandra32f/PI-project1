# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:07:31 2023

@author: alex-
"""


from fastapi.testclient import TestClient
from api import app
from api import Item

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_predict():
    item = Item(context="The Universe contains everything that exists", question="What is at the center of the solar system?")
    response = client.post("/predict/", json=item.dict())
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "score" in response.json()
