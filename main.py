from pydantic import BaseModel


class Musique(BaseModel):
    titre: str
    artiste: str
    immatriculation: str

    def est_immatriculation_valide(self):
        # Vérification du format de l'immatriculation
        immatriculation_parts = self.immatriculation.split('/')
        if len(immatriculation_parts) != 4:
            return False

        # Vérification des initiales de l'artiste
        initiales_artiste = immatriculation_parts[0]
        if len(initiales_artiste) != 2 or not initiales_artiste.isalpha() or not initiales_artiste.isupper():
            return False

        # Vérification de la durée de la musique
        duree_musique = int(immatriculation_parts[1])
        if duree_musique <= 60 or duree_musique >= 300:
            return False

        # Vérification du type de musique
        type_musique = immatriculation_parts[2]
        if type_musique not in ['RAP', 'POP', 'RNB']:
            return False

        # Vérification de l'identifiant
        identifiant = immatriculation_parts[3]
        if len(identifiant) != 4 or '6' in identifiant:
            return False

        return True


class Magasin(BaseModel):
    type_musique: str
    vinyles: list[Musique] = []
    dvds: list[Musique] = []

    def ajouter_vinyle(self, titre, artiste, immatriculation):
        musique = Musique(titre=titre, artiste=artiste, immatriculation=immatriculation)
        if self.type_musique != musique.immatriculation.split('/')[2]:
            print("Erreur : Le type de musique de l'immatriculation ne correspond pas au magasin.")
            return

        if not musique.est_immatriculation_valide():
            print("Erreur : Immatriculation invalide.")
            return

        self.vinyles.append(musique)

    def ajouter_dvd(self, titre, artiste, immatriculation):
        musique = Musique(titre=titre, artiste=artiste, immatriculation=immatriculation)
        if self.type_musique != musique.immatriculation.split('/')[2]:
            print("Erreur : Le type de musique de l'immatriculation ne correspond pas au magasin.")
            return

        if not musique.est_immatriculation_valide():
            print("Erreur : Immatriculation invalide.")
            return

        self.dvds.append(musique)

    def retirer_vinyle(self, immatriculation):
        for musique in self.vinyles:
            if musique.immatriculation == immatriculation:
                self.vinyles.remove(musique)
                break

    def retirer_dvd(self, immatriculation):
        for musique in self.dvds:
            if musique.immatriculation == immatriculation:
                self.dvds.remove(musique)
                break

    def get_vinyles(self):
        return self.vinyles

    def get_dvds(self):
        return self.dvds
