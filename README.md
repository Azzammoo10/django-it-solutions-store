# 🛒 E-Commerce Platform - ThreeComp Company

Une plateforme e-commerce moderne et complète développée avec Django, offrant une expérience d'achat fluide avec gestion des produits, panier d'achat, système de paiement PayPal et interface d'administration avancée.

## 📋 Table des matières

- [🚀 Fonctionnalités](#-fonctionnalités)
- [🛠️ Technologies utilisées](#️-technologies-utilisées)
- [📦 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [🎯 Utilisation](#-utilisation)
- [📱 Captures d'écran](#-captures-décran)
- [🏗️ Architecture](#️-architecture)
- [🔧 API Endpoints](#-api-endpoints)
- [📊 Base de données](#-base-de-données)
- [🔒 Sécurité](#-sécurité)
- [🚀 Déploiement](#-déploiement)
- [🤝 Contribution](#-contribution)
- [📄 Licence](#-licence)

## 🚀 Fonctionnalités

### 👥 Gestion des utilisateurs
- **Inscription/Connexion** : Système d'authentification complet
- **Profils utilisateurs** : Gestion des informations personnelles et adresses de livraison
- **Sécurité** : Validation des mots de passe et protection CSRF

### 🛍️ Catalogue de produits
- **Catégories** : Organisation des produits par catégories
- **Recherche avancée** : Recherche par nom, description et catégorie
- **Images multiples** : Support jusqu'à 4 images par produit
- **Gestion des stocks** : Statuts de disponibilité (Disponible, Rupture, En solde)
- **Prix de solde** : Système de réductions intégré

### 🛒 Système de panier
- **Panier persistant** : Sauvegarde automatique pour les utilisateurs connectés
- **Gestion des quantités** : Modification et suppression d'articles
- **Calcul automatique** : Totaux avec gestion des soldes
- **Session sécurisée** : Panier sauvegardé en base de données

### 💳 Paiement et commandes
- **Intégration PayPal** : Paiement sécurisé via PayPal Sandbox
- **Gestion des commandes** : Suivi complet du cycle de vie
- **Adresses de livraison** : Gestion des adresses multiples
- **Statuts de commande** : Suivi des expéditions

### 🎨 Interface utilisateur
- **Design responsive** : Compatible mobile, tablette et desktop
- **Templates Django** : Interface moderne et intuitive
- **Messages flash** : Notifications utilisateur en temps réel
- **Navigation intuitive** : Menu et breadcrumbs optimisés

### 🔧 Administration
- **Interface Django Admin** : Gestion complète des données
- **TinyMCE** : Éditeur riche pour les descriptions de produits
- **Gestion des médias** : Upload et organisation des images
- **Statistiques** : Tableaux de bord intégrés

## 🛠️ Technologies utilisées

### Backend
- **Django 5.2.1** : Framework web Python
- **SQLite/PostgreSQL** : Base de données
- **Django Admin** : Interface d'administration
- **Django Sessions** : Gestion des sessions utilisateur

### Frontend
- **HTML5/CSS3** : Structure et style
- **JavaScript** : Interactivité client
- **Bootstrap** : Framework CSS responsive
- **FontAwesome** : Icônes modernes

### Paiement
- **PayPal SDK** : Intégration paiement sécurisé
- **Django PayPal** : Module Django pour PayPal

### Déploiement
- **Railway** : Plateforme de déploiement
- **WhiteNoise** : Gestion des fichiers statiques
- **Procfile** : Configuration de déploiement

### Outils de développement
- **Python 3.x** : Langage principal
- **pip** : Gestionnaire de paquets
- **Git** : Contrôle de version
- **Virtual Environment** : Isolation des dépendances

## 📦 Installation

### Prérequis
```bash
# Python 3.8 ou supérieur
python --version

# pip (gestionnaire de paquets Python)
pip --version

# Git (contrôle de version)
git --version
```

### Clonage du projet
```bash
# Cloner le repository
git clone https://github.com/votre-username/ecommerce-django.git
cd ecommerce-django
```

### Configuration de l'environnement virtuel
```bash
# Créer un environnement virtuel
python -m venv env

# Activer l'environnement virtuel
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

### Installation des dépendances
```bash
# Installer les dépendances
pip install -r requirements.txt
```

### Configuration de la base de données
```bash
# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser
```

### Lancement du serveur
```bash
# Démarrer le serveur de développement
python manage.py runserver

# Accéder à l'application
# http://127.0.0.1:8000/
```

## ⚙️ Configuration

### Variables d'environnement
Créer un fichier `.env` à la racine du projet :

```env
# Django Settings
SECRET_KEY=votre-clé-secrète-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optionnel pour PostgreSQL)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# PayPal Settings
PAYPAL_TEST=True
PAYPAL_RECEIVER_EMAIL=business@threecomp.com
```

### Configuration PayPal
1. Créer un compte PayPal Developer
2. Configurer les clés API dans les paramètres
3. Activer le mode sandbox pour les tests

## 🎯 Utilisation

### Pour les administrateurs
1. **Accès admin** : `http://127.0.0.1:8000/admin/`
2. **Gestion des produits** : Ajout, modification, suppression
3. **Gestion des commandes** : Suivi et mise à jour des statuts
4. **Gestion des utilisateurs** : Administration des comptes

### Pour les clients
1. **Parcourir les produits** : Navigation par catégories
2. **Recherche** : Trouver rapidement les produits
3. **Ajouter au panier** : Sélection des quantités
4. **Finaliser l'achat** : Paiement sécurisé via PayPal

## 📱 Captures d'écran

### 🏠 Page d'accueil
<!-- Ajoutez ici une capture d'écran de la page d'accueil -->
**Titre : Page d'accueil - Présentation des produits vedettes**

### 🛍️ Catalogue de produits
<!-- Ajoutez ici une capture d'écran du catalogue -->
**Titre : Catalogue - Navigation par catégories**

### 📦 Page produit détaillée
<!-- Ajoutez ici une capture d'écran d'un produit -->
**Titre : Détail produit - Images multiples et informations complètes**

### 🛒 Panier d'achat
<!-- Ajoutez ici une capture d'écran du panier -->
**Titre : Panier - Gestion des quantités et calcul des totaux**

### 💳 Processus de paiement
<!-- Ajoutez ici une capture d'écran du checkout -->
**Titre : Checkout - Intégration PayPal sécurisée**

### 👤 Espace utilisateur
<!-- Ajoutez ici une capture d'écran du profil utilisateur -->
**Titre : Profil utilisateur - Gestion des informations personnelles**

### 🔧 Interface d'administration
<!-- Ajoutez ici une capture d'écran de l'admin -->
**Titre : Dashboard admin - Gestion complète de la plateforme**

## 🏗️ Architecture

### Structure du projet
```
ecommerce-django/
├── APP_Web/                 # Configuration principale Django
│   ├── settings.py          # Paramètres de l'application
│   ├── urls.py             # URLs principales
│   └── wsgi.py             # Configuration WSGI
├── Ecommerce_Website/       # Application principale e-commerce
│   ├── models.py           # Modèles de données
│   ├── views.py            # Logique métier
│   ├── urls.py             # URLs de l'application
│   └── forms.py            # Formulaires personnalisés
├── cart/                   # Application panier d'achat
│   ├── cart.py             # Logique du panier
│   └── views.py            # Vues du panier
├── payment/                # Application paiement
│   ├── models.py           # Modèles de commande
│   ├── views.py            # Logique de paiement
│   └── forms.py            # Formulaires de livraison
├── Templates/              # Templates HTML
│   └── Ecom/              # Templates e-commerce
├── static/                 # Fichiers statiques
│   ├── css/               # Styles CSS
│   ├── js/                # Scripts JavaScript
│   └── img/               # Images et médias
└── media/                 # Fichiers uploadés
```

### Modèles de données
- **User** : Utilisateurs Django standard
- **Profile** : Informations utilisateur étendues
- **Categories** : Catégories de produits
- **Produit** : Produits avec images multiples
- **Order** : Commandes clients
- **OrderItem** : Articles de commande
- **ShippingAddress** : Adresses de livraison

## 🔧 API Endpoints

### Pages principales
- `GET /` : Page d'accueil
- `GET /base/` : Page e-commerce principale
- `GET /materiel/` : Catalogue de produits
- `GET /category/<str>/` : Produits par catégorie
- `GET /product/<int>/` : Détail d'un produit

### Authentification
- `GET /login/` : Page de connexion
- `POST /login/` : Authentification
- `GET /register/` : Page d'inscription
- `POST /register/` : Création de compte
- `GET /logout/` : Déconnexion

### Gestion du profil
- `GET /update_user/` : Modification du profil
- `GET /update_password/` : Changement de mot de passe
- `GET /update_info/` : Mise à jour des informations

### Panier et commandes
- `GET /cart/` : Affichage du panier
- `POST /cart/add/` : Ajouter au panier
- `POST /cart/update/` : Modifier le panier
- `POST /cart/delete/` : Supprimer du panier
- `GET /payment/checkout/` : Processus de paiement

## 📊 Base de données

### Schéma principal
```sql
-- Utilisateurs et profils
User (Django standard)
├── Profile (informations étendues)
└── ShippingAddress (adresses de livraison)

-- Produits et catégories
Categories
└── Produit (produits avec images multiples)

-- Commandes
Order (commandes principales)
└── OrderItem (articles de commande)
```

### Relations clés
- **User ↔ Profile** : OneToOne
- **User ↔ ShippingAddress** : OneToOne
- **Categories ↔ Produit** : OneToMany
- **Order ↔ OrderItem** : OneToMany
- **User ↔ Order** : OneToMany

## 🔒 Sécurité

### Authentification
- **Django Auth** : Système d'authentification robuste
- **Validation des mots de passe** : Règles de sécurité
- **Protection CSRF** : Protection contre les attaques CSRF
- **Sessions sécurisées** : Gestion sécurisée des sessions

### Paiement
- **PayPal Sandbox** : Environnement de test sécurisé
- **Validation des données** : Vérification des entrées
- **Chiffrement SSL** : Communication sécurisée

### Données
- **Validation des formulaires** : Contrôle des entrées
- **Échappement HTML** : Protection XSS
- **Permissions** : Contrôle d'accès granulaire

## 🚀 Déploiement

### Configuration Railway
```bash
# Variables d'environnement Railway
SECRET_KEY=votre-clé-secrète-production
DEBUG=False
ALLOWED_HOSTS=votre-domaine.railway.app
DATABASE_URL=postgresql://...
```

### Commandes de déploiement
```bash
# Collecter les fichiers statiques
python manage.py collectstatic

# Appliquer les migrations
python manage.py migrate

# Créer le superutilisateur
python manage.py createsuperuser
```

### Configuration de production
- **DEBUG=False** : Mode production
- **ALLOWED_HOSTS** : Domaines autorisés
- **STATIC_ROOT** : Chemin des fichiers statiques
- **MEDIA_ROOT** : Chemin des fichiers uploadés

## 🤝 Contribution

### Comment contribuer
1. **Fork** le projet
2. **Créer** une branche feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** les changements (`git commit -m 'Add AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir** une Pull Request

### Standards de code
- **PEP 8** : Style de code Python
- **Docstrings** : Documentation des fonctions
- **Tests** : Couverture de tests
- **Type hints** : Annotations de types

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 📞 Contact

**ThreeComp Company**
- **Email** : business@threecomp.com
- **Site web** : https://threecomp.com
- **GitHub** : [Lien vers le repository]

---

**Développé avec ❤️ par l'équipe ThreeComp**