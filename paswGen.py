#On importe le module itertools, ce module contient des outils pour créer des combinaisons, permutations,...
import itertools;

#Chaîne de caractères utilisée pour générer les mots de passe
#Chaque caractère sera combiné avec les autres
characters = "abcd123'";
#Longueur min des MP générés
min_length = 2;
#Longueur max des MP générés
max_length = 4;
#Nom du fichier ds lequel on va enregistrer la wordlist
filename = "wordlist.txt";

#Ouverture du fichier en mode écriture ("w")
#'with' garantit que le fichier sera bien fermé automatiquement
with open(filename, "w") as file:
    #Boucle sur les longueurs possibles 
    #max_length + 1 car exclut la borne supérieure
    for length in range(min_length, max_length + 1):
        #itertools génère toutes les combinaisons possibles
        #des caractères pour une longueur donnée
        #repeat=length indique le nb de caractères par combinaison
        for combo in itertools.product(characters, repeat=length):
            #combo est un tuple, par ex :('a', '1', 'b')
            #join() permet de transformer ce tuple en une chaîne de caractère
            password = "" .join(combo);
            #On écrit le MP ds un fichier
            file.write(password + "\n");

print("wordlist générée avec succès !");
