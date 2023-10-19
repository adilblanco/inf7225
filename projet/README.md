# inf7225

## Optimisation des Installations de Fontaines dans les Parcs de Montréal

### Objectif :
Le projet vise à améliorer l'accès à l'eau potable dans les parcs de la ville de Montréal en optimisant l'emplacement des fontaines publiques. Pour ce faire, nous utiliserons des données provenant de différentes sources, en mettant particulièrement l'accent sur les données ouvertes fournies par la Ville de Montréal.
- Données sur les parcs : [Lien vers les données](https://example.com/parcs-montreal-data)
- Données sur les pistes cyclables : [Lien vers les données](https://example.com/cyclable-data)

### Méthodologie :

1. Collecte de Données : Nous collecterons des données à partir de diverses sources, notamment le site des données ouvertes de la Ville de Montréal, pour obtenir des informations sur les parcs, les pistes cyclables, les installations externes (comme les terrains de sport), les rues vertes et d'autres données pertinentes.

2. Chargement des Données : Les données collectées seront importées dans une base de données Postgres pour une gestion plus facile et une analyse ultérieure.

3. Transformation et Filtrage : Les données seront transformées pour inclure uniquement les colonnes pertinentes et pour effectuer des transformations géospatiales telles que le changement de système de coordonnées de projection (project CRS) afin de faciliter le calcul des distances entre les éléments. Aucune préoccupation ne sera accordée à la qualité des données.

4. Calcul des Distances : Nous calculerons les distances entre les emplacements des fontaines et les autres éléments tels que les pistes cyclables, les installations sportives, les rues vertes et les parcs à l'aide de techniques de géolocalisation.

5. Optimisation des Emplacements : En utilisant les distances calculées, nous développerons un algorithme d'optimisation visant à déterminer les emplacements optimaux pour les fontaines dans les parcs, en maximisant la couverture et l'accessibilité.

### Résultats Attendus :

- Une carte interactive montrant les emplacements recommandés pour les fontaines dans les parcs de Montréal.
- Des rapports détaillés sur les distances, les emplacements optimaux et l'impact attendu sur l'accès à l'eau potable.
- Des recommandations pour l'amélioration de l'infrastructure des fontaines publiques dans les parcs.

### Impact Potentiel :
Ce projet contribuera à améliorer la qualité de vie des citoyens de Montréal en facilitant l'accès à l'eau potable dans les espaces publics, tout en favorisant l'utilisation des parcs et des installations sportives.

## Installation et Configuration

Pour exécuter ce projet, vous devrez installer les dépendances suivantes :

- [Python](https://www.python.org/): Version 3.8 ou supérieure.
- [Docker](https://www.docker.com/): Pour la gestion des conteneurs (optionnel).
- ...

Vous pouvez installer les bibliothèques Python nécessaires en utilisant `pip`. Exécutez la commande suivante pour les installer :

## Références

- Données sur les parcs : [Lien vers les données](https://example.com/parcs-montreal-data)
- Données sur les pistes cyclables : [Lien vers les données](https://example.com/cyclable-data)
- Documentation de pandas : [https://pandas.pydata.org/](https://pandas.pydata.org/)
- Documentation de requests : [https://docs.python-requests.org/en/master/](https://docs.python-requests.org/en/master/)
- Site officiel de Docker : [https://www.docker.com/](https://www.docker.com/)
- ...

