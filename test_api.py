# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:07:31 2023

@author: alex-
"""

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'score'

    