print("********** BIENVENUE DANS NOTRE PROGRAMME **********")
print("VOULEZ VOUS VOUS ENREGISTRER OU AFFICHER LA LISTE ?")
print("TAPEZ [oui] POUR VOUS ENREGISTRER")
print("TAPEZ [non] POUR AFFICHER LA LISTE DES INSCRITS")
#code ajouter par koumare
user_choice = "oui"

user_choice = input("oui ou non :")
print("VOTRE CHOIX EST NON :", user_choice,"\n")


if user_choice == "oui":
    nom = input("Entrer votre nom :")
    print("VOTRE NOM EST : ", nom)
   
    prenom = input("Entrer votre prenom :")
    print("VOTRE PRENOM EST : ", prenom)

    email = input("Entrer votre email :")
    print("VOTRE EMAIL EST : ", email)

    telephone = input("Entrer votre telephone :")
    print("VOTRE TELEPHONE EST : ", telephone)

    infos = f"{nom}  {prenom}  {email}  {telephone}"
    f = open('userlist.txt','a')
    with open('userlist.txt',"a") as f:
        f.write("\n"+infos)
        f.close()
        print("ENREGISTREMENT SUCCES","\n")

else:
    print("NOUS VOUS AFFICHONS LA LISTE DES INSCRITS","\n")
    
    
