# projet7

[![Generic badge](https://img.shields.io/badge/MADE_WITH-PYTHON-orange.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/APPROVED_BY-AURELIE_BERNICHE-blueviolet.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/FOR-startup_LitReview-green.svg)](https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png)


## Introduction

Ce projet a été réalisé pour la société financière AlgoInvest&Trade dans le but d'optimiser leur stratégie d'investissement à l'aide d'algorithmes. Ils souhaitaient maximiser le profit au bout de 2 ans. Quelques contraintes étaient imposées : chaque action ne devait être achetée qu'une seule fois et entière et le portefeuille était de 500€ max par client. Dans un but de transparence vis à vis du client, ils voulaient dans un premier temps, essayer toutes les combinaisons pour obtenir le meilleur investissement. Se rendant compte de l'augmentation exponentielle du temps de cette stratégie avec un nombre d'actions important, ils ont souhaité se diriger vers une solution optimisée qui ne testerait plus toutes les combinaison mais rendrait une réponse en moins d'une seconde et fournirait ainsi la meilleure stratégie d'investissement.

### Pré-requis

- Editeur de texte [Download VS Code](https://code.visualstudio.com/) 
- Langage de programmation [Download Python](https://www.python.org/downloads/)

### Installation
Création de l'environnement virtuel ``` pipenv shell```

### Démarrage
Pour l'algorithme de Force Brute:
$ python bruteforce.py
Pour la solution optimisée:
$ python optimized.py