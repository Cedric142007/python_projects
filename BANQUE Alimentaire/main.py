#nom: Cedric
#Titre: Banque Alimentaire
#Description: demande les aliments que l'utilisateur veut ajouter à la banque puis les ajoutes les affiches


#importation des modules
import os 

#definiton de la classe pour retourner les aliments
class Aliments:
    def __init__(self, nom, types, vertu):
      self._nom = nom
      self._types = types
      self._vertu=vertu
    def getNom(self):
      return self._nom

    def getTypes(self):
      return self._types
      
    def getVertu(self):
      return self._vertu

    def affiche(self):
      return f" {self._nom} : {self._types} : {self._vertu}"

#définition des fonction 
#fonction pour importer les aliments du texte vers la liste
def importation():
    #ouvrir le fichier texte
    fichier = open("listeAliments.txt", encoding="utf-8")
    lignes = fichier.readlines()
    
    if os.path.isfile("listeAliments.txt"):
      print("Le fichier existe.")
    else:
      print("Le fichier n'existe pas")
    
    for l in lignes:
          l = l.strip("\n")
          if l!="":
              information = l.split(" : ")
              aliments = Aliments(information[0], information[1], information[2])
              listeAliments.append(aliments)
    
    #fermer le fichier texte
    fichier.close()
    
    return


#fonction pour enregister les aliments dans l'éditeur de texte 
def enregistrement():
    fichier = open("listeAliments.txt", "w", encoding="utf-8")

    for c in listeAliments:
      print(f"{c.affiche()}")
      fichier.write(c.affiche() + "\n")
    
    fichier.close()
    
    return
    
#programme principale
listeAliments= []
#appele de la fonction pour importer les aliment
importation()
#demander les information à l'utilisateur
nombreAliment = int(input("Combien d'aliment veut tu ajouter à la banque? "))
for i in range(nombreAliment):
  nom = input("\nEntre le nom de l'aliment  : ")
  types = input("Entre son type (fruit, legume ...): ")
  vertu = input("Entre sa vertu : ")
  #ajouter les information entrer dans la liste d'aliment
  aliments = Aliments(nom,types,vertu)
  listeAliments.append(aliments)

print("\n--- Liste des Aliments  ---")
#fonction pour enregistrer et afficher les aliments
enregistrement ()