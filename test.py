import unittest
from main import Magasin, Musique

class TestMagasin(unittest.TestCase):
    def setUp(self):
        self.magasin = Magasin("POP")

    def test_ajouter_vinyle(self):
        self.magasin.ajouter_vinyle("Titre 1", "Artiste 1", "AR/180/POP/1234")
        vinyles = self.magasin.get_vinyles()
        self.assertEqual(len(vinyles), 1)
        self.assertEqual(vinyles[0].titre, "Titre 1")
        self.assertEqual(vinyles[0].artiste, "Artiste 1")
        self.assertEqual(vinyles[0].immatriculation, "AR/180/POP/1234")

    def test_ajouter_vinyle_invalide(self):
        self.magasin.ajouter_vinyle("Titre 2", "Artiste 2", "AB/250/POP/6666")
        vinyles = self.magasin.get_vinyles()
        self.assertEqual(len(vinyles), 0)

    def test_ajouter_dvd(self):
        self.magasin.ajouter_dvd("Titre 3", "Artiste 3", "AR/200/POP/9876")
        dvds = self.magasin.get_dvds()
        self.assertEqual(len(dvds), 1)
        self.assertEqual(dvds[0].titre, "Titre 3")
        self.assertEqual(dvds[0].artiste, "Artiste 3")
        self.assertEqual(dvds[0].immatriculation, "AR/200/POP/9876")

    def test_ajouter_dvd_invalide(self):
        self.magasin.ajouter_dvd("Titre 4", "Artiste 4", "AR/150/ROCK/4321")
        dvds = self.magasin.get_dvds()
        self.assertEqual(len(dvds), 0)

    def test_retirer_vinyle(self):
        self.magasin.ajouter_vinyle("Titre 5", "Artiste 5", "AR/180/POP/5555")
        self.magasin.retirer_vinyle("AR/180/POP/5555")
        vinyles = self.magasin.get_vinyles()
        self.assertEqual(len(vinyles), 0)

    def test_retirer_dvd(self):
        self.magasin.ajouter_dvd("Titre 6", "Artiste 6", "AR/200/POP/7777")
        self.magasin.retirer_dvd("AR/200/POP/7777")
        dvds = self.magasin.get_dvds()
        self.assertEqual(len(dvds), 0)

if __name__ == '__main__':
    unittest.main()
