from fastapi import FastAPI
from pymongo import MongoClient

from database import *

app = FastAPI()

client = MongoClient(connect)
Musiques = client[db]
titres = Musiques[collectionTitres]
magasins_collection = Musiques[collectionMagasins]

# Peupler la collection "musiques" avec des données initiales
musiques = [
    {
        "titre": "Titre 1",
        "artiste": "Artiste 1",
        "immatriculation": "JH/250/POP/1234"
    },
    {
        "titre": "Titre 2",
        "artiste": "Artiste 2",
        "immatriculation": "AB/180/RAP/5678"
    },
    {
        "titre": "Titre 3",
        "artiste": "Artiste 3",
        "immatriculation": "CD/320/RNB/9012"
    }
]

# Peupler la collection "titres" avec des données initiales
titres.insert_many(musiques)

# Peupler la collection "magasins_collection" avec des données initiales
magasins_data = [
    {
        "type_musique": "POP",
        "vinyles": [
            {
                "titre": "Vinyle 1",
                "artiste": "Artiste 1",
                "immatriculation": "JH/250/POP/1234"
            },
            {
                "titre": "Vinyle 2",
                "artiste": "Artiste 2",
                "immatriculation": "AB/180/RAP/5678"
            }
        ],
        "dvds": [
            {
                "titre": "DVD 1",
                "artiste": "Artiste 3",
                "immatriculation": "CD/320/RNB/9012"
            }
        ]
    },
    {
        "type_musique": "RAP",
        "vinyles": [
            {
                "titre": "Vinyle 3",
                "artiste": "Artiste 4",
                "immatriculation": "EF/200/RAP/3456"
            }
        ],
        "dvds": []
    }
]

magasins_collection.insert_many(magasins_data)
