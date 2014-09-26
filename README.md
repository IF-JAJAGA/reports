reports
=======

Rapports produits pour les différents projets, avec un outil d'exportation en PDF

Prérequis :

- python 3
- pip (https://pip.pypa.io/en/latest/installing.html)
- weasyprint (`sudo pip install WeasyPrint` sur Linux, voir [ici][WeasyPrint Windows] pour Windows.)

Utilisation :

Pour créer un nouveau rapport, exécuter `./add_project.py`. Le projet se crée avec le nom donné.

Chaque répertoire représente un rapport.
Un rapport est constitué de plusieurs fichiers HTML. Un Makefile sert à rassembler ces fichiers dans l'ordre indiqué dans le fichier `config`, puis à les compiler pour produire un fichier PDF.

`make` : fusionne et compile les fichiers HTML.
`make clean` : efface le fichier HTML fusionné et le fichier PDF.

Par défaut, un rapport contient deux fichiers HTML (header et footer) qui sont copiés depuis header.in et footer.in

[WeasyPrint Windows]: http://weasyprint.org/docs/install/#windows
