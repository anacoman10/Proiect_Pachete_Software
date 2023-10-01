#Programare Python - prima parte a proiectului de Pachete Software

#utilizarea listelor si a dictionarelor + metode specifice acestora
#LISTE
listProgrammingLanguage=["C++","Java","Python","Flutter","Swift"]
print("Primul element din lista: ",listProgrammingLanguage[0])

listProgrammingLanguage.append("Kotlin")
print(listProgrammingLanguage)

print(listProgrammingLanguage[::-1])
print(listProgrammingLanguage[:])
print(listProgrammingLanguage[1:5])

listProgrammingLanguage[1]="C"
print(listProgrammingLanguage)


print("Lungime lista: " + str(len(listProgrammingLanguage)) + " elemente.")

listProgrammingLanguage.insert(1,"Ruby")
print(listProgrammingLanguage)

listProgrammingLanguage.remove("Ruby")
print(listProgrammingLanguage)

listProgrammingLanguage.pop()
print(listProgrammingLanguage)
listProgrammingLanguage.insert(5,"Kotlin")
print(listProgrammingLanguage)

del listProgrammingLanguage[0]
print(listProgrammingLanguage)

listProgrammingLanguage.clear()
print(listProgrammingLanguage)

listProgrammingLanguage=["C++","Java","Python","Flutter","Swift"]
print(listProgrammingLanguage)

listProgrammingLanguage.copy()
print(listProgrammingLanguage)

print(listProgrammingLanguage.count("C++"))

listPopularLanguages=["JavaScript","Carbon","Go"]
listProgrammingLanguage.extend(listPopularLanguages)
print(listProgrammingLanguage)

print(listProgrammingLanguage.index("C++"))
listProgrammingLanguage.reverse()
print(listProgrammingLanguage)

listProgrammingLanguage.sort()
print(listProgrammingLanguage)

#DICTIONARE
dictProgrammingLanguage={"C++":2344338.4,"Carbon":36335.5,"Flutter":73746.6,"Go":37356.4,"Java":23736784,"Python":8747822.3}
print(dictProgrammingLanguage)
for i in dictProgrammingLanguage:
    print(dictProgrammingLanguage[i])

print("Gasire valoare cheie: ",dictProgrammingLanguage.get("C++"))
dictProgrammingLanguage["Python"]=1234.345
print(dictProgrammingLanguage)

dict_clear=dictProgrammingLanguage.clear()
print(dict_clear)

copy=dictProgrammingLanguage.copy()
print(copy)

dict_from=dictProgrammingLanguage.fromkeys("Python")
print(dict_from)

#Utilizare set si tupluri + metode specifice acestora
#SET
setProgrammingLanguage={"C++","Java","Python","Flutter","Carbon","Go"}

setProgrammingLanguage.add("Ruby")
print(setProgrammingLanguage)

copySet=setProgrammingLanguage.copy()
print(copySet)

clearSet=setProgrammingLanguage.clear()
print(clearSet)

setProgrammingLanguage=copySet
print(setProgrammingLanguage)

setPopularProgramming={"Java","Python","Kotlin"}
diff=setProgrammingLanguage.difference(setPopularProgramming)
print("Diferentele intre tupluri sunt: ",diff)

diffUpdate=setProgrammingLanguage.difference_update(setPopularProgramming)
print(diffUpdate)

print(setProgrammingLanguage.discard("C++"))

#TUPLU

tupleProgrammingLanguage=("C++","Java","Python","Flutter","Carbon","Go")
print(tupleProgrammingLanguage)

print(len(tupleProgrammingLanguage))
print(max(tupleProgrammingLanguage))
print(min(tupleProgrammingLanguage))
print(tupleProgrammingLanguage.index("Python"))

#FUNCTII

dictProgrammingLanguage = {"C++":2344338.4,"Carbon":36335.5,"Flutter":73746.6,"Go":37356.4,"Java":23736784,"Python":8747822.3}
def afisare_top_3():
    top_3 = sorted(dictProgrammingLanguage.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 limbaje de programare:")
    for i, (limbaj, popularitate) in enumerate(top_3):
        print(f"{i + 1}. {limbaj}: {popularitate}")


afisare_top_3()

def cautare_limbaj(limbaj):
    if limbaj in dictProgrammingLanguage:
        popularitate=dictProgrammingLanguage[limbaj]
        print(f"Popularitatea limbajului {limbaj} este: {popularitate}")
    else:
        print(f"Limbajul {limbaj} nu există în dicționar.")

cautare_limbaj("C++")

def adaugare_limbaj(limbaj, popularitate):
    dictProgrammingLanguage[limbaj] = popularitate
    print(f"Limbajul {limbaj} a fost adăugat cu popularitatea {popularitate}.")

adaugare_limbaj("Assembly",1345.5)

#Utilizare structura conditionala

salarii = {"Ana":10000, "Maria":4789, "Popescu":1345}

def marireSalarii(dict):
    for i in dict:
        if dict[i] < 2000:
            dict[i] *= 1.5
            print("Salariu marit pentru", i, "este", dict[i])
        else:
            print("Nu exista niciun salariu sub 2000")
    return dict

marireSalarii(salarii)

#Utilizare structura repetitiva
# valoare_valida = False
# while not valoare_valida:
#     input_utilizator = input("Introduceti o valoare intreaga: ")
#     if input_utilizator.isdigit():
#         valoare_valida = True
#     else:
#         print("Valoarea introdusa nu este un numar intreg.")
#


#import date din Csv, afișarea unor informații despre DataFrame
import pandas as pd
freelancer=pd.read_csv("FreeLancer.csv")
teritorial=pd.read_csv("Teritorial.csv")

etichete_freelancer=freelancer.index
print(etichete_freelancer)
etichete_teritorial=teritorial.index
print(etichete_teritorial)
print(freelancer.columns.values)
print(teritorial.columns.values)

#Accesarea datelor cu loc si iloc
print(freelancer.loc[1])
print(teritorial.loc[1])
print(freelancer.iloc[[1,2,5]])
print(teritorial.iloc[[1,2,5]])
print(freelancer.loc[:,"C"])

#Modificarea datelor in pachetul Pandas
print(freelancer.loc[0,"Java"])
freelancer.loc[0,"Java"]=10
print(freelancer.loc[0,"Java"])

#Utilizare functii de grup - groupby
print(freelancer.groupby(['Java']).groups.keys())
print(teritorial.groupby(['Regiunea']).groups.keys())

#Tratare valori lipsa
#Valorile lipsa pot fi de 3 tipuri - None, 0 sau NaN (Not a Number)

mean_php=int(freelancer['PHP'].mean())
valLipsa=freelancer['PHP'].fillna(value=mean_php)
print("Valori lipsa inlocuite: \n",valLipsa)

#Stergerea de coloane si de inregistrari
teritorial1=teritorial.drop("PAAnim",axis=1)
print(teritorial1)

teritorial1=teritorial.drop([3,4,5])
print("Au fost sterse inregistrarile cu index 3,4,5: \n",teritorial1)

#Prelucrari statistice, gruparea si agregarea datelor in Pandas
print(teritorial.groupby(['Judet', 'SalNet']).agg({'Regiunea': 'count'}))
print(teritorial.describe())
print(freelancer.describe())
