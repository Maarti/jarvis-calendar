## Dependance

Ce plugin � besoin de la librairie Google client
Executez la commande suivante pour installer la librairie
sudo pip install --upgrade google-api-python-client

## Description

Ce plugin permet de g�rer son agenda "Google Calendar"

Vous pouvez :
- consulter les prochains �v�nements,
- consulter les �v�nements du jour,
- consulter les �v�nements du lendemain,
- demander quand aura lieu un �v�nement pr�cis,
- creer un �v�nement.

Lors de la cr�ation de l'�v�nement, plusieurs questions seront demand�es � l'utilisateur.

Concernant la date, il est possible de donner une date sous la forme :
- jour mois ann�e ex : 10 aout 2017,
- Aujourd'hui,
- Demain.


## Usage
```
You: Quel sont les �v�nements � venir ?
Jarvis: Je regarde.
Jarvis: Vos 3 prochains �v�nements sont :
Jarvis: Aujoud'hui � 19 heure, Repas chez la belle-m�re.
Jarvis: Demain � 9 heure, Rendez vous chez le dentiste.
Jarvis: Le 23 septembre � 16 heure, F�te d'anniverssaire d'Emilie

You: Ajoute-moi un �v�nement
Jarvis: Oui bien s�r, quel est le titre de l'�v�nement � ajouter?
You: Aller chercher des fleurs pour la st-Valentin
Jarvis: O� doit se d�rouler l'�v�nement?
You: A la boutique de fleurs
Jarvis: Donnez moi une description petite description de l'�v�nement
You: Petite pens�e pour ma femme pour la St-Valentin
Jarvis: Quel jour aura lieu l'�v�nement?
You: 14 f�vrier 2017
Jarvis: A quelle heure ?
You: 10 heure
Jarvis: Quel jour prendra fin l'�v�nement
You: 14 f�vrier 2017
Jarvis: Quelle heure?
You: 10 heure 30
Jarvis: L'�v�nement vient d'�tre ajout� au calendrier.
```

## Author
[RobyBioloid](https://github.com/RobyBioloid/jarvis-calendar)
