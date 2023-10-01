#EXERCITII PYTHON
import pandas as pd
import matplotlib.pyplot as plt

#1. Sa se citeasca din csv toate produsele cu cantitatea cea mai mare vanduta, sa se afiseze inclusiv categoria din care face parte produsul, dar si produsul
#intr-un nou DataFrame

#citim datele din fisier


# Citirea datelor din fișierul CSV într-un DataFrame
df = pd.read_csv('ProduseVandute.csv')

# Găsirea maximului pentru coloana "CantitateVanduta"
max_cantitate = df['CantitateVanduta'].max()

# Filtrarea datelor pentru a obține produsele cu cantitatea maximă vândută
df_max_cantitate = df[df['CantitateVanduta'] == max_cantitate]

# Selectarea doar a coloanelor "Categorie" și "Produs" în noul DataFrame
df_result = df_max_cantitate[['Categorie', 'Produs',"CantitateVanduta"]]

# Afișarea rezultatului
print(df_result)


#2. Sa se determine valoarea totala a vanzarilor pentru fiecare judet


def valTotala(df):
    df['ValoareTotala'] = df['CantitateVanduta'] * df['PretUnitarPerReducere']
    valoare_totala_judet = df.groupby('Judet')['ValoareTotala'].sum()
    return valoare_totala_judet

# Apelarea funcției valTotala pentru a calcula valoarea totală a vânzărilor pentru fiecare județ
rezultat = valTotala(df)

# Afișarea valorii totale a vânzărilor pentru fiecare județ
print(rezultat)


#3. Calcularea valorii medii a taxei pentru fiecare categorie de produse.

# Calcularea valorii medii a taxei pentru fiecare categorie de produse
df['ValoareMedie'] = df.groupby('Categorie')['ValoareTaxe'].transform('mean')

# Selecția unice a categoriilor de produse și a valorilor medii ale taxei
valoare_medie_taxa = df[['Categorie', 'ValoareMedie']].drop_duplicates().reset_index(drop=True)

# Afișarea valorii medii a taxei pentru fiecare categorie de produse
print(valoare_medie_taxa)


#4. Găsirea orașului cu cele mai multe vânzări de produse electrocasnice.

def gaseste_orasul_max_vanzari_electrocasnice(df):
    # Filtrarea datelor pentru a include doar produsele de categorie "Electrocasnice"
    electrocasnice = df[df['Categorie'] == 'Electrocasnice']

    # Găsirea orașului cu cele mai multe vânzări de produse electrocasnice
    oras_max_vanzari = electrocasnice.groupby('Oras')['CantitateVanduta'].sum().idxmax()

    return oras_max_vanzari

# Exemplu de utilizare
oras_max_vanzari_electrocasnice = gaseste_orasul_max_vanzari_electrocasnice(df)
print("Orașul cu cele mai multe vânzări de produse electrocasnice:", oras_max_vanzari_electrocasnice)


#5. Sa se afișeze un mesaj corespunzător având în vedere că se dorește afișarea majorării cu 25% a prețului de vânzare cu taxe pentru categoria de „Electronice”
# și diminuarea cu 5% a prețului de vânzare cu taxe pentru  categoria de “Accesorii” împreună cu județul și data când a fost făcută tranzacția.

def afisare_mesaj(df):
    # Majorarea cu 25% a prețului de vânzare cu taxe pentru Electronice
    df.loc[df['Categorie'] == 'Electronice', 'PretUnitarVanzareFaraTaxe'] *= 1.25

    # Diminuarea cu 5% a prețului de vânzare cu taxe pentru Accesorii
    df.loc[df['Categorie'] == 'Accesorii', 'PretUnitarVanzareFaraTaxe'] *= 0.95

    # Afișarea mesajului corespunzător pentru fiecare tranzacție modificată
    for index, row in df.iterrows():
        if row['Categorie'] == 'Electronice':
            mesaj = f"Majorare cu 25% pentru produsele Electronice. Județ: {row['Judet']}, Data: {row['DataComandarii']}"
            print(mesaj)
        elif row['Categorie'] == 'Accesorii':
            mesaj = f"Diminuare cu 5% pentru produsele Accesorii. Județ: {row['Judet']}, Data: {row['DataComandarii']}"
            print(mesaj)

print(afisare_mesaj(df))

#6. Să se afișeze toate vanzarile din județul Bucuresti unde produsele vandute au fost „Telefon Samsung Galaxy S20”.

# Filtrarea datelor pentru județul București și produsul "Telefon Samsung Galaxy S20"
filt = (df['Judet'] == 'Bucuresti') & (df['Produs'] == 'Telefon Samsung Galaxy S20')
filtered_data = df.loc[filt, ['DataComandarii', 'Judet', 'Produs', 'PretUnitarVanzareFaraTaxe']]

# Afișarea mesajului corespunzător pentru fiecare înregistrare
for _, row in filtered_data.iterrows():
    data_comanda = row['DataComandarii']
    judet = row['Judet']
    produs = row['Produs']
    pret = row['PretUnitarVanzareFaraTaxe']
    print(f"Tranzacție înregistrată în data de {data_comanda} în județul {judet}:")
    print(f"Produs: {produs}")
    print(f"Pret cu taxa: {pret}")
    print("\n")


#7.  Să se afișeze pentru fiecare județ:
#-	cantitatea totală vândută pe categorii de produse;
#-	prețul total mediu de vânzare;

cantitate_totala = df.groupby(['Judet', 'Categorie'])['CantitateVanduta'].sum()

# Calcularea prețului total mediu de vânzare pentru fiecare județ
pret_mediu = df.groupby('Judet')['PretUnitarVanzareFaraTaxe'].mean()

# Afișarea rezultatelor
print("Cantitatea totală vândută pe categorii de produse pentru fiecare județ:")
print(cantitate_totala)
print()
print("Prețul total mediu de vânzare pentru fiecare județ:")
print(pret_mediu)


#8. Calcularea valorii totale a vânzărilor pentru fiecare lună a anului.


# Convertim coloana "DataComandarii" la tipul dată
df['DataComandarii'] = pd.to_datetime(df['DataComandarii'])

# Adăugăm o coloană pentru luna comenzii
df['Luna'] = df['DataComandarii'].dt.month

# Calculăm valoarea totală a vânzărilor pentru fiecare lună
sales_total_per_month = df.groupby('Luna')['ValoareTotala'].sum()

# Afișăm rezultatele
print("Valoarea totală a vânzărilor pentru fiecare lună a anului:")
print(sales_total_per_month)


#9. Găsirea produsului cu cea mai mare medie a prețului de vânzare pe unitate:

max_avg_price_product = df.groupby('Produs')['PretUnitarVanzareFaraTaxe'].mean().idxmax()
print("Produsul cu cea mai mare medie a prețului de vânzare pe unitate:", max_avg_price_product)

#10. Reprezentați grafic cantitățile vândute din fiecare categorie


# Calcularea sumei cantităților vândute pe categorii
category_sales = df.groupby('Categorie')['CantitateVanduta'].sum()

# Crearea graficului de bare
plt.bar(category_sales.index, category_sales.values)

# Setarea titlului și etichetelor axelor
plt.title('Cantitățile vândute pe categorii')
plt.xlabel('Categorie')
plt.ylabel('Cantitate vândută')

# Afișarea graficului
plt.show()


