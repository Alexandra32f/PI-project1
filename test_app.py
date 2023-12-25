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
    item = Item(context="The Universe contains everything that exists – not only the Earth and everything on it, but also all the planets, stars, and galaxies, and the space in between them. The sun, at the center of the solar system, is just one of about 100 billion stars in our galaxy, or collection of stars, called the Milky Way. Astronomers have estimated that there are about 100 billion other galaxies in the universe. Most scientists think that the universe formed about 15 billion years ago in an enormous explosion called the big bang. They also think that the universe is expanding.", question="What is at the center of the solar system?")
    
    response = client.post("/predict/", json=item.dict())
    
    assert response.status_code == 200
    
    response_json = response.json()

    print("Response JSON:", response_json)
    
    assert "answer" in response_json



