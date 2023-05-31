FROM python:3.9

# Installation de uvicorn
RUN pip install uvicorn

# Copie des fichiers de l'application
COPY . /app

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances de l'application
RUN pip install -r requirements.txt

# Exécution du fichier seeder.py pour peupler la base de données
RUN python seeder.py

# Commande d'exécution de l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
