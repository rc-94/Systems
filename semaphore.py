import sys
import random


""" PROJET SYSTEMES D'EXPLOITATION : SIMULATEUR DE SEMAPHORES """


""" Fonctions """

def Erreur_Remplissage(i, tmp, au_cas_ou_erreur):
    """
    Fonction qui previent d'une erreur dans le fichier lors du remplissage des dictionnaire/tableaux de la phase 1.
    Arrete le programme.
    """
    for q in range(len(au_cas_ou_erreur)):
        if tmp[i] == au_cas_ou_erreur[q]:
            print("\nERREUR. La ligne", q+1,"de votre fichier n'est pas prise en charge par le simulateur de semaphores...\n\nA bientot !\n")
    sys.exit()


def Recuperation_Donnees_Fichier(fichier): 
    """
    Fonction qui recupere les donnees du fichier soumis par l'utilisateur.
    """
    try:
        tmp = fichier.readlines()
    except UnicodeDecodeError as error:
        print("\nERREUR. Encodage de votre fichier non supporte.")
        print("Precision :", error, "\n\nA bientot !\n")
        sys.exit()
    
    # Suppression des retours a la ligne, tabulations, espaces et lignes vides
    for i in range(len(tmp)):
        tmp[i] = tmp[i].rstrip('\n\r')
        tmp[i] = tmp[i].replace(" ","")
    au_cas_ou_erreur = list(tmp) # Pour donner la ligne exacte s'il y a des lignes vides dans le fichier
    while "" in tmp:
        tmp.remove("")
        
    # Initialisation : 2 dictionnaires et 6 listes
    IN = {}
    PA = {}
    PL = []
    PE = []
    PX = []
    EL = []
    EE = []
    EX = []
    
    # Erreur potentielle : Il manque %IN, %PA ou %FI
    if "%IN" not in tmp or "%PA" not in tmp or "%FI" not in tmp:
        print("\nERREUR. Il manque une partie dans votre fichier.\n\nA bientot !\n")
        sys.exit()
    
    # Remplissage des dictionnaires et listes
    i = 0
        
    while i < len(tmp):
        
        # On ignore les '#'
        if tmp[i].find("#") == 0:
            i += 1
   
        # FI
        elif tmp[i] == "%FI":
            i += 1
        
        # IN
        elif tmp[i] == "%IN":
            i += 1
            
            while tmp[i].find("%") == -1:
                
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                        # Erreur potentielle : mauvaise syntaxe pas de "="
                        if "=" not in tmp[i]:
                            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)

                        # Erreur potentielle : semaphore negatif ou float
                        if "-" in tmp[i] or "," in tmp[i] or "." in tmp[i]:
                            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)
                        
                        semaphore = ""
                        nombre = ""
                        for j in range(len(tmp[i])):
                            if ord(tmp[i][j]) >= 65 and ord(tmp[i][j]) <= 90:
                                semaphore = semaphore + tmp[i][j]
                            elif ord(tmp[i][j]) >= 48 and ord(tmp[i][j]) <= 57:
                                nombre = nombre + tmp[i][j]
                            elif tmp[i][j] != "=":
                                Erreur_Remplissage(i,tmp,au_cas_ou_erreur)
                        
                        # Erreur potentielle : mauvaise syntaxe ou non presence de semaphore ou de valeur
                        if semaphore == "" or nombre == "" or len(semaphore) > 1 or nombre.isdigit() == False:
                            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)
                        if int(nombre) == 0:
                            print("\nERREUR. Un semaphore est initialise a 0.\n\nA bientot !\n")
                            sys.exit()
                        if semaphore in IN:
                            print("\nERREUR. Deux semaphores identiques.\n\nA bientot !\n")
                            sys.exit()
                            
                        IN[semaphore] = int(nombre)
                        i += 1
        
        # PA
        elif tmp[i] == "%PA":
            i += 1
            
            while tmp[i].find("%") == -1:

                if tmp[i].find("#") == 0:
                    i += 1
                else:
                        # Erreur potentielle : mauvaise syntaxe pas de "="
                        if "=" not in tmp[i]:
                            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)
                        
                        # Erreur potentielle : nombre de processus negatif ou float pour une instruction
                        if "-" in tmp[i] or "." in tmp[i] or "," in tmp[i]:
                            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)
                            
                        instruction = ""
                        nombre = ""
                        for j in range(len(tmp[i])):
                            if ord(tmp[i][j]) == 69 or ord(tmp[i][j]) == 76 or ord(tmp[i][j]) == 78 or ord(tmp[i][j]) == 88:
                                instruction = instruction + tmp[i][j]
                            elif ord(tmp[i][j]) >= 48 and ord(tmp[i][j]) <= 57:
                                nombre = nombre + tmp[i][j]
                            elif tmp[i][j] != "=":
                                Erreur_Remplissage(i,tmp,au_cas_ou_erreur)
                        
                        # Erreur potentielle : mauvaise syntaxe pas d'instruction ou de valeur
                        if instruction == "" or nombre == "" or len(instruction) > 1:
                            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)
                        if instruction in PA:
                            print("\nERREUR. Deux parametres identiques.\n\nA bientot !\n")
                            sys.exit()
                        
                        PA[instruction] = nombre
                        i += 1
        
        # PL
        elif tmp[i] == "%PL":
            i += 1
            
            while tmp[i].find("%") == -1:
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                    PL.append(tmp[i])
                    i += 1
        
        # PE
        elif tmp[i] == "%PE":
            i += 1
            
            while tmp[i].find("%") == -1:
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                    PE.append(tmp[i])
                    i += 1
        
        # PX
        elif tmp[i] == "%PX":
            i += 1
            
            while tmp[i].find("%") == -1:
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                    PX.append(tmp[i])
                    i += 1
        
        # EL
        elif tmp[i] == "%EL":
            i += 1
            
            while tmp[i].find("%") == -1:
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                    EL.append(tmp[i])
                    i += 1
        
        # EE
        elif tmp[i] == "%EE":
            i += 1
            
            while tmp[i].find("%") == -1:
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                    EE.append(tmp[i])
                    i += 1
        
        # EX 
        elif tmp[i] == "%EX":
            i += 1
            
            while tmp[i].find("%") == -1:
                if tmp[i].find("#") == 0:
                    i += 1
                else:
                    EX.append(tmp[i])
                    i += 1
        
        # Erreur potentielle : ligne non comprise
        else :
            Erreur_Remplissage(i, tmp, au_cas_ou_erreur)
    
    return IN, PA, PL, PE, PX, EL, EE, EX


def Dictionnaire_Vide(dico):
    """
    Fonction qui verifie si un dictionnaire est vide. Arrete le programme si c'est le cas.
    """
    if dico == {} :
        print("\nERREUR. Les parties 'initialisations' et 'paramètres' doivent etre remplies.\n\nA bientot !\n")
        sys.exit()


def Aucun_Prologue_Epilogue(PL, PE, PX, EL, EE, EX):
    """
    Fonction qui verifie s'il n'y a aucun prologue ou epilogue. Arrete le programme si c'est le cas.
    """
    if PL == [] and PE == [] and PX == [] and EL == [] and EE == [] and EX == []:
        print("\nERREUR. Aucun prologue et epilogue.\n\nA bientot !\n")
        sys.exit()


def Verification_Parametres(PA, PL, PE, PX, EL, EE, EX):
    """
    Fonction qui verifie dans les parametres que :
    - le nombre de simulations souhaitees soit donne et qu'il ne soit pas egal a 0.
    - aucun des parametres L, E ou X ne soit initialiser a 0.
    - si un parametre L, E ou X existe, il a bien un prologue et epilogue associe.
    - pour chaque prologue ou epilogue present, l'instruction associee (lecture, ecriture ou execution) est bien dans les parametres.
    """
    if "N" not in PA.keys():
        print("\nERREUR. Le simulateur aimerait prendre connaissance du nombre de simulations a effectuer.\n\nA bientot !\n")
        sys.exit()
    elif PA["N"] == '0' :
        print("\nERREUR. Il ne sert a rien d'utiliser le simulateur pour 0 simulation...\n\nA bientot !\n")
        sys.exit()
    
    for i in PA:
        
        if PA[i] == '0' and i == "L":
            print("\nERREUR. Le fait d'initialiser votre parametre de lecture L a 0 exclu lecture des solutions.\n\nA bientot !\n")
            sys.exit()
        elif PA[i] == '0' and i == "E":
            print("\nERREUR. Le fait d'initialiser votre parametre d'ecriture E a 0 exclu ecriture des solutions.\n\nA bientot !\n")
            sys.exit()
        elif PA[i] == '0' and i == "X":
            print("\nERREUR. Le fait d'initialiser votre parametre d'execution X a 0 exclu execution des solutions.\n\nA bientot !\n")
            sys.exit()
        
        if i == "L" and (PL == [] or EL == []):
            print("\nERREUR. Une lecture L est initialisee en parametre, mais elle n'a pas de prologue ou epilogue ou les deux.\n\nA bientot !\n")
            sys.exit()
        elif i == "E" and (PE == [] or EE == []):
            print("\nERREUR. Une ecriture E est initialisee en parametre, mais elle n'a pas de prologue ou epilogue ou les deux.\n\nA bientot !\n")
            sys.exit()
        elif i == "X" and (PX == [] or EX == []):
            print("\nERREUR. Une execution X est initialisee en parametre, mais elle n'a pas de prologue ou epilogue ou les deux.\n\nA bientot !\n")
            sys.exit()
    
    if (PL != [] or EL != []) and "L" not in PA:
        print("\nERREUR. Pas de parametre lecture, alors qu'il y a un prologue ou epilogue pour lecture.\n\nA bientot !\n")
        sys.exit()
    elif (PE != [] or EE != []) and "E" not in PA:
        print("\nERREUR. Pas de parametre ecriture, alors qu'il y a un prologue ou epilogue pour ecriture.\n\nA bientot !\n")
        sys.exit()
    elif (PX != [] or EX != []) and "X" not in PA:
        print("\nERREUR. Pas de parametre execution, alors qu'il y a un prologue ou epilogue pour execution.\n\nA bientot !\n")
        sys.exit()


def Initialisation_Plateau_De_Simulation(prologue, epilogue, instruction):
    """
    Fonction qui definie un tableau representant le "plateau de simulation" : prologue, instruction, epilogue.
    """
    tab = []
    for q in range(len(prologue)):
        tab.append(prologue[q])
    tab.append(instruction)
    return tab + epilogue


def Verification_Semaphore_Pris_Relache(tableau):
    """
    Fonction qui verifie le fait que chaque semaphore pris soit relache. Si ce n'est pas le cas, le programme s'arrete.
    """
    q = 0
    while q < len(tableau):
        if q != "lecture" and q != "ecriture" and q != "execution":
            if tableau[q][0] == "P":
                if tableau.count(tableau[q]) != tableau.count("V(" + tableau[q][2] + ")"):
                    print("\nERREUR dans un prologue ou epilogue. Un semaphore pris n'est pas relaché.\n\nA bientot !\n")
                    sys.exit()
            if tableau[q][0] == "V":
                if tableau.count(tableau[q]) != tableau.count("P(" + tableau[q][2] + ")"):
                    print("\nERREUR dans un prologue ou epilogue. Un semaphore pris n'est pas relaché.\n\nA bientot !\n")
                    sys.exit()
        q += 1


def Initialisation_Outils_De_Simulation(dico):
    """
    Fonction qui definie un tableau de dictionnaires.
    Chaque dictionnaire represente un processus servant a la simulation.
    """
    outils = []
    for q in dico.keys():
        if q == "L":
            for k in range(int(dico[q])):
                sous_dico = {}
                sous_dico["processus"] = "lecture"
                sous_dico["avancee"] = 0
                sous_dico["section_critique"] = False
                sous_dico["instructions"] = 40
                sous_dico["fini"] = False
                outils.append(sous_dico)
        elif q == "E":
            for k in range(int(dico[q])):
                sous_dico = {}
                sous_dico["processus"] = "ecriture"
                sous_dico["avancee"] = 0
                sous_dico["section_critique"] = False
                sous_dico["instructions"] = 40
                sous_dico["fini"] = False
                outils.append(sous_dico)
        elif q == "X":
            for k in range(int(dico[q])):
                sous_dico = {}
                sous_dico["processus"] = "execution"
                sous_dico["avancee"] = 0
                sous_dico["section_critique"] = False
                sous_dico["instructions"] = 40
                sous_dico["fini"] = False
                outils.append(sous_dico)
    return outils


def Simulation(IN, lecture, ecriture, execution, outils):
    """
    Fonction qui effectue une simulation et recupere toutes les situations autorisees.
    """
    processus_finis = 0
    
    # Initialiser de ce qui va recuperer les solutions : un tableau de dictionnaires
    solutions = []
    dico = {}
    dico["lecture"] = 0
    dico["ecriture"] = 0
    dico["execution"] = 0
   
    while processus_finis < len(outils):
        hasard = random.randint(0, len(outils)-1)
        nb_instructions = random.randint(1,7)
        
        i = 0
        
        while i < nb_instructions and outils[hasard]["fini"] == False:
            
            # Cas ou le processeur est assigne a une lecture
            if outils[hasard]["processus"] == "lecture":
                
                if outils[hasard]["section_critique"] == True:
                    
                    outils[hasard]["instructions"] -= 1
                    if outils[hasard]["instructions"] <= 0:
                        outils[hasard]["section_critique"] = False
                        outils[hasard]["avancee"] += 1
                        
                        # Recuperation des situations autorisees
                        dico["lecture"] -= 1
                        dico_tmp = dict(dico)
                        if dico_tmp not in solutions:
                            solutions.append(dico_tmp)
                        
                else :
                    if "P" in lecture[outils[hasard]["avancee"]]:
                        
                        semaphore = lecture[outils[hasard]["avancee"]][2:len(lecture[outils[hasard]["avancee"]])-1]
                        if IN[semaphore] > 0:
                            IN[semaphore] -= 1
                            outils[hasard]["avancee"] += 1
                        else :
                            break
                    
                    elif "V" in lecture[outils[hasard]["avancee"]]:
                        
                        semaphore = lecture[outils[hasard]["avancee"]][2:len(lecture[outils[hasard]["avancee"]])-1]
                        IN[semaphore] += 1
                        outils[hasard]["avancee"] += 1
                    
                    elif lecture[outils[hasard]["avancee"]] == "lecture":
                        
                        outils[hasard]["section_critique"] = True
                        
                        # Recuperation des situations autorisees
                        dico["lecture"] += 1
                        dico_tmp = dict(dico)
                        if dico_tmp not in solutions:
                            solutions.append(dico_tmp)

                    if outils[hasard]["avancee"] == len(lecture):
                        outils[hasard]["fini"] = True
            
            # Cas ou le processeur est assigne a une ecriture
            elif outils[hasard]["processus"] == "ecriture":
                
                if outils[hasard]["section_critique"] == True:
                    
                    outils[hasard]["instructions"] -= 1
                    if outils[hasard]["instructions"] <= 0:
                        outils[hasard]["section_critique"] = False
                        outils[hasard]["avancee"] += 1
                        
                        # Recuperation des situations autorisees
                        dico["ecriture"] -= 1
                        dico_tmp = dict(dico)
                        if dico_tmp not in solutions:
                            solutions.append(dico_tmp)
                else :
                    if "P" in ecriture[outils[hasard]["avancee"]]:
                        
                        semaphore = ecriture[outils[hasard]["avancee"]][2:len(ecriture[outils[hasard]["avancee"]])-1]
                        if IN[semaphore] > 0:
                            IN[semaphore] -= 1
                            outils[hasard]["avancee"] += 1
                        else :
                            break
                    
                    elif "V" in ecriture[outils[hasard]["avancee"]]:
                        
                        semaphore = ecriture[outils[hasard]["avancee"]][2:len(ecriture[outils[hasard]["avancee"]])-1]
                        IN[semaphore] += 1
                        outils[hasard]["avancee"] += 1
                    
                    elif ecriture[outils[hasard]["avancee"]] == "ecriture":
                        
                        outils[hasard]["section_critique"] = True
                        
                        # Recuperation des situations autorisees
                        dico["ecriture"] += 1
                        dico_tmp = dict(dico)
                        if dico_tmp not in solutions:
                            solutions.append(dico_tmp)

                    if outils[hasard]["avancee"] == len(ecriture):
                        outils[hasard]["fini"] = True
            
            # Cas ou le processeur est assigne a une execution
            elif outils[hasard]["processus"] == "execution":
                
                if outils[hasard]["section_critique"] == True:
                    
                    outils[hasard]["instructions"] -= 1
                    if outils[hasard]["instructions"] <= 0:
                        outils[hasard]["section_critique"] = False
                        outils[hasard]["avancee"] += 1
                        
                        # Recuperation des situations autorisees
                        dico["execution"] -= 1
                        dico_tmp = dict(dico)
                        if dico_tmp not in solutions:
                            solutions.append(dico_tmp)
                else :
                    if "P" in execution[outils[hasard]["avancee"]]:
                        
                        semaphore = execution[outils[hasard]["avancee"]][2:len(execution[outils[hasard]["avancee"]])-1]
                        if IN[semaphore] > 0:
                            IN[semaphore] -= 1
                            outils[hasard]["avancee"] += 1
                        else :
                            break
                    
                    elif "V" in execution[outils[hasard]["avancee"]]:
                        
                        semaphore = execution[outils[hasard]["avancee"]][2:len(execution[outils[hasard]["avancee"]])-1]
                        IN[semaphore] += 1
                        outils[hasard]["avancee"] += 1
                    
                    elif execution[outils[hasard]["avancee"]] == "execution":
                        
                        outils[hasard]["section_critique"] = True
                        
                        # Recuperation des situations autorisees
                        dico["execution"] += 1
                        dico_tmp = dict(dico)
                        if dico_tmp not in solutions:
                            solutions.append(dico_tmp)

                    if outils[hasard]["avancee"] == len(execution):
                        outils[hasard]["fini"] = True
                        
            if outils[hasard]["fini"] == True:
                processus_finis += 1
                
            i += 1
            
    return solutions


def Solutions_Finales(IN, PA, lecture, ecriture, execution, outils):
    """
    Fonctions qui effectue plusieurs fois une simulation.
    A chaque tour de boucle, outils est reinitialise. On part sur une base de nouveaux processeurs.
    """
    solutions_finales = []
    nb_simulations = int(PA["N"])
    
    for i in range(nb_simulations):
        outils = Initialisation_Outils_De_Simulation(PA)
        solutions = Simulation(IN, lecture, ecriture, execution, outils)
        for j in solutions:
            if j not in solutions_finales:
                solutions_finales.append(j)
    
    return solutions_finales


def Affichage_Solutions(solutions):
    """
    Fonction qui affiche les differentes solutions du fichier soumis par l'utilisateur.
    """
    ponctuation = ";"
    
    for i in range(len(solutions)):
    
        if i == len(solutions)-1:
            ponctuation = "."
        
        # il y a lecture(s), ecriture(s) et execution(s)
        if solutions[i]["lecture"] != 0 and solutions[i]["ecriture"] != 0 and solutions[i]["execution"] != 0:
            print("-", solutions[i]["lecture"], "acces en lecture(s),", solutions[i]["ecriture"], "acces en ecriture(s) et", solutions[i]["execution"],"acces en execution(s)" + ponctuation)
        
        # il y a lecture(s) et ecriture(s)
        elif solutions[i]["lecture"] != 0 and solutions[i]["ecriture"] != 0 and solutions[i]["execution"] == 0:
            print("-", solutions[i]["lecture"], "acces en lecture(s) et", solutions[i]["ecriture"], "acces en ecriture(s)"+ ponctuation)
        
        # il y a lecture(s) et execution(s)
        elif solutions[i]["lecture"] != 0 and solutions[i]["ecriture"] == 0 and solutions[i]["execution"] != 0:
            print("-", solutions[i]["lecture"], "acces en lecture(s) et", solutions[i]["execution"], "acces en execution(s)" + ponctuation)
        
        # il y a ecriture(s) et execution(s)
        elif solutions[i]["lecture"] == 0 and solutions[i]["ecriture"] != 0 and solutions[i]["execution"] != 0:
            print("-", solutions[i]["ecriture"], "acces en ecriture(s) et", solutions[i]["execution"], "acces en execution(s)" + ponctuation)
        
        # il y a lecture(s)
        elif solutions[i]["lecture"] != 0 and solutions[i]["ecriture"] == 0 and solutions[i]["execution"] == 0:
            print("-", solutions[i]["lecture"], "acces en lecture(s)" + ponctuation)
        
        # il y a ecriture(s)
        elif solutions[i]["lecture"] == 0 and solutions[i]["ecriture"] != 0 and solutions[i]["execution"] == 0:
            print("-", solutions[i]["ecriture"], "acces en ecriture(s)" + ponctuation)
        
        # il y a execution(s)
        elif solutions[i]["lecture"] == 0 and solutions[i]["ecriture"] == 0 and solutions[i]["execution"] != 0:
            print("-", solutions[i]["execution"], "acces en execution(s)" + ponctuation)
        else:
            print("- Aucun acces nulle part" + ponctuation)

""" Fin fonctions """


def main():

    # Erreur potentielle : Pas de fichier soumis
    try:
        sys.argv[1]
    except IndexError as error:
        print("\nERREUR. N'oubliez pas de rentrer un fichier !\n")
        sys.exit()
    
    # Erreur potentielle : Nom de fichier non valide
    try:
        fichier = open(sys.argv[1], "r")
    except FileNotFoundError as error:
        print("\nERREUR. Votre fichier demeure introuvable...\n")
        sys.exit()
    
    # Phrase de bienvenue
    print("\nBienvenue dans le simulateur de semaphores !\n")
    
    """ PREMIERE PHASE : Lecture du fichier """
    
    # Recuperation des donnees du fichier
    print("... Lecture de votre fichier en cours...")
    
    IN, PA, PL, PE, PX, EL, EE, EX = Recuperation_Donnees_Fichier(fichier)
    fichier.close()
    
    # Verification de la presence d'elements dans IN et PA
    Dictionnaire_Vide(IN)
    Dictionnaire_Vide(PA)
    
    # S'il n'y a aucun prologue et epilogue
    Aucun_Prologue_Epilogue(PL, PE, PX, EL, EE, EX)
        
    # Verification des parametres dans PA
    Verification_Parametres(PA, PL, PE, PX, EL, EE, EX)
    
    print("Fin de la lecture de votre fichier.\n")

    """ SECONDE PHASE : Simulation """
    
    print("... Simulation en cours, veuillez patienter...")
    
    # Initialisation de tableaux representant le "plateau de simulation"
    lecture = Initialisation_Plateau_De_Simulation(PL, EL, "lecture")
    ecriture = Initialisation_Plateau_De_Simulation(PE, EE, "ecriture")
    execution = Initialisation_Plateau_De_Simulation(PX, EX, "execution")
    
    # Verification du fait que chaque semaphore pris est relache
    Verification_Semaphore_Pris_Relache(lecture)
    Verification_Semaphore_Pris_Relache(ecriture)
    Verification_Semaphore_Pris_Relache(execution)
    
    
    # Initialisation d'un tableau representant les processus servant a la simulation
    outils = Initialisation_Outils_De_Simulation(PA)
    
    # Execution des simulations
    solutions_finales = Solutions_Finales(IN, PA, lecture, ecriture, execution, outils)
    
    print("Fin de la simulation.\n")
    
    # Affichage des solutions
    print("Voici toutes les differentes situations autorisees : ")
    Affichage_Solutions(solutions_finales)
    
    # Phrase d'au revoir
    print("\nMerci d'avoir fait appel au simulateur de semaphores !\n")


""" Appel de main() """
if __name__ == "__main__":
    main()
