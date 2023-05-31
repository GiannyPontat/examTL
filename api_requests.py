import requests

from main import Musique, Magasin


# Routes pour les Titres

def get_titres():
    response = requests.get("http://localhost:8000/titres")
    if response.status_code == 200:
        titres = response.json()
        for titre_data in titres:
            print(titre_data)
            # Traitez le titre comme vous le souhaitez
            pass
    else:
        print("Erreur lors de la récupération des titres:", response.status_code)

def create_musique(musique_data):
    # Créer une instance de la classe Musique avec les données fournies
    musique = Musique(**musique_data)

    # Vérifier si l'immatriculation est valide
    if not musique.est_immatriculation_valide():
        print("Erreur : Immatriculation invalide.")
        return

    # Envoi de la requête POST pour créer la musique
    response = requests.post("http://localhost:8000/titres", json=musique_data)
    if response.status_code == 200:
        musique = response.json()
        print("Musique créée avec succès:")
        print(musique)
    else:
        print("Erreur lors de la création de la musique:", response.status_code)


def get_musique(immatriculation):
    response = requests.get(f"http://localhost:8000/titres/{immatriculation}")
    if response.status_code == 200:
        titre = response.json()
        # Traitez le titre récupéré comme vous le souhaitez
        pass
    elif response.status_code == 404:
        print("Titre non trouvé")
    else:
        print("Erreur lors de la récupération du titre:", response.status_code)

def update_music(immatriculation, musique_data):
    response = requests.put(f"http://localhost:8000/titres/{immatriculation}", json=musique_data)
    if response.status_code == 200:
        titre = response.json()
        # Traitez le titre mis à jour comme vous le souhaitez
        pass
    elif response.status_code == 404:
        print("Titre non trouvé")
    else:
        print("Erreur lors de la mise à jour du titre:", response.status_code)

def delete_music(immatriculation):
    response = requests.delete(f"http://localhost:8000/titres/{immatriculation}")
    if response.status_code == 200:
        print("Musique supprimée avec succès")
    elif response.status_code == 404:
        print("Titre non trouvé")
    else:
        print("Erreur lors de la suppression de la musique:", response.status_code)


# Routes pour les Magasins

def get_magasins():
    response = requests.get("http://localhost:8000/magasins")
    if response.status_code == 200:
        magasins = response.json()
        for magasin_data in magasins:
            # Traitez le magasin comme vous le souhaitez
            pass
    else:
        print("Erreur lors de la récupération des magasins:", response.status_code)

def create_magasin(magasin_data):
    response = requests.post("http://localhost:8000/magasins", json=magasin_data)
    if response.status_code == 200:
        magasin = response.json()
        # Traitez le magasin créé comme vous le souhaitez
        pass
    else:
        print("Erreur lors de la création du magasin:", response.status_code)

def get_magasin(id):
    response = requests.get(f"http://localhost:8000/magasins/{id}")
    if response.status_code == 200:
        magasin = response.json()
        # Traitez le magasin récupéré comme vous le souhaitez
        pass
    elif response.status_code == 404:
        print("Magasin non trouvé")
    else:
        print("Erreur lors de la récupération du magasin:", response.status_code)

def update_magasin(id, magasin_data):
    response = requests.put(f"http://localhost:8000/magasins/{id}", json=magasin_data)
    if response.status_code == 200:
        magasin = response.json()
        # Traitez le magasin mis à jour comme vous le souhaitez
        pass
    elif response.status_code == 404:
        print("Magasin non trouvé")
    else:
        print("Erreur lors de la mise à jour du magasin:", response.status_code)

def delete_magasin(id):
    response = requests.delete(f"http://localhost:8000/magasins/{id}")
    if response.status_code == 200:
        print("Magasin supprimé avec succès")
    elif response.status_code == 404:
        print("Magasin non trouvé")
    else:
        print("Erreur lors de la suppression du magasin:", response.status_code)

# Exemples d'utilisation des fonctions

# Récupérer tous les titres
get_titres()

# Créer une nouvelle musique
nouvelle_musique = {
    "titre": "Nouvelle Musique",
    "artiste": "Artiste ABC",
    "immatriculation": "XY/300/POP/5678"
}
create_musique(nouvelle_musique)
#
## Récupérer une musique par immatriculation
#get_musique("XY/180/POP/5678")
#
## Mettre à jour une musique
#musique_mise_a_jour = {
#    "titre": "Titre mis à jour",
#    "artiste": "Artiste mis à jour",
#    "immatriculation": "XY/180/POP/5678"
#}
#update_music("XY/180/POP/5678", musique_mise_a_jour)
#
# Supprimer une musique
delete_music("AA/120/POP/1234")

## Récupérer tous les magasins
#get_magasins()
#
## Créer un nouveau magasin
#nouveau_magasin = {
#    "type_musique": "RAP",
#    "vinyles": [],
#    "dvds": []
#}
#create_magasin(nouveau_magasin)
#
## Récupérer un magasin par ID
#get_magasin("1234567890")
#
## Mettre à jour un magasin
#magasin_mis_a_jour = {
#    "type_musique": "POP",
#    "vinyles": [],
#    "dvds": []
#}
#update_magasin("1234567890", magasin_mis_a_jour)
#
## Supprimer un magasin
#delete_magasin("1234567890")
