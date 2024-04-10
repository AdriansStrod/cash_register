#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
import json
main_saraksts = []
#Lasa čeku datus uz variables
with open('main_saraksts.json', 'r') as openfile:
    # Lasa no json faila
    main_saraksts = json.load(openfile)
    print("1. Pievieno preci")
    print("2. Čeku dati")
    print("3. Atlikums")
    print("4.Nepietiek summas lai apmaksatu preces ")
    print("5.dzes preci pec kartas numura  ")
    print("5.ievada atcelšana  ")
#While true repeat the action
while True:
    choice = input("\nChoose choice:")
    #Lietotajs ievada čeka datus 
    if choice == "1":
        Jusu_limits = input("Jusu_limits:")
        Preču_nosaukums =input("Preču nosaukums:")
        cena = (input("Preču cena:"))
        atlaide = (input("Cik procentus atlaide"))
        Vardnica={ 
        "Jusu_limits" : Jusu_limits,
        "Preču_)nosaukums": Preču_nosaukums,
        "cena": cena,
        "atlaide" : atlaide
        }
        #Izdruka čeka datus
        print(Vardnica)
        main_saraksts.append(Vardnica)
    elif choice == "2":
        answer = cena =- atlaide 
        print(answer,"Samaksaja par visu")
        #Parada lietotajam atlikumu
    elif choice == "3":
        if cena < Jusu_limits:
           atlikums == 0
           atlikums = cena =- Jusu_limits
        print(atlikums)
    #Parada lietotajam ka nav atlikuma 
    elif choice == "4":
        if cena > Jusu_limits:
            
           nepietiek_naudas = cena > Jusu_limits
        print(nepietiek_naudas)
    elif choice == "5":
        delete = ("delete prece by sequince number")
        #Atcel ievadu un apstaj kodu
    elif choice == "6":
        print("ievada atcelšana...")
        break
        
pass 