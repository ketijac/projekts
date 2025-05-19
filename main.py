import pandas as pd

def izvele():
    while True:
        print("\nIzvēlies funkciju:")
        print("1. print - Izdrukāt visus datus")
        print("2. add - Pievienot skolēnu")
        print("3. final - Izdrukāt visus datus ar aprēķinātām gala atzīmēm ")
        print("4. sort - Izdrukāt sakārtotus gala rezultātus")
        print("5. delete - Dzēst skolēnu")
        print("6. exit - Iziet")

        komanda = input(">> ").strip().lower()

        if komanda == "print":
            izdruka_datus()
        elif komanda == "add":
            add_students()
        elif komanda == "final":
            galas()
        elif komanda == "sort":
            sakārtots_rezultats(df, klases_vidējaisd)
        elif komanda == "delete":
            delete_students()
        elif komanda == "exit":
            print("Programma beidzas.")
            break
        else:
            print("Nepareiza komanda. Mēģini vēlreiz.")
            

def datu_nolasīšana():
    return pd.read_excel("atzimes.xlsx", sheet_name= "Sheet1") #nolasa excel file


def saglabā_datus(df):
    df.to_excel("atzimes.xlsx", sheet_name="Sheet1", index = False)

def izdruka_datus():
    df = datu_nolasīšana()
    if 'Gala atzime' in df.columns:
        df = df.drop(columns=['Gala atzime'])
    df.index = range(1, len(df) + 1)
    print(df)

def gala_atzime(row):
    if pd.isna(row['M']) or pd.isna(row['K']) or pd.isna(row['T']) or pd.isna(row['E']): # pārbauda vai nav tukšu kopu/vai visi ir skaitļi
        return f"Error: trūkst datu {row['Vārds']} {row['Uzvārds']}"
    
    atzīme = 0.1 * row['M'] + 0.35* row['K'] + 0.05 * row['T']+ 0.5 * row ['E'] # apreiķina gala atzīmi, katram skolēnam
    return round(atzīme, 1)  # noapaļo līdz vienam skaitlim aiz komata

df = datu_nolasīšana()
df['Gala atzime'] = df.apply(gala_atzime, axis=1)

klases_vidējaisd = round(df['Gala atzime'].mean(), 1) # apreiķina klases vidējo ( no gala atzīmēm)

def galas ():
    df = datu_nolasīšana()
    df['Gala atzime'] = df.apply(gala_atzime, axis=1)
    print(df)


def sakārtots_rezultats(df, klases_vidējaisd):
    df= datu_nolasīšana()
    df['Gala atzime'] = df.apply(gala_atzime, axis=1)
    klases_vidējaisd = round(df['Gala atzime'].mean(), 1)
    kārto_dilstosi = df.sort_values(by = 'Gala atzime', ascending= False) #sakārtot studentus dilstošā secībā

    virs_linijas = True #atzīmēt ar ---------- klases vidējo ( tā lai tiem kuriem ir augstāka par vidējo ir virs līnijas, sekojošie tiem kuriem ir zemāka, zem līnijas)
    for _, row in kārto_dilstosi.iterrows():
        if virs_linijas and row['Gala atzime'] < klases_vidējaisd:
            print (f"-------------------Studentu vidējā atzime: {klases_vidējaisd}")
            virs_linijas = False
        print(f"{row['Vārds']} {row['Uzvārds']} - {row['Gala atzime']}")
    

#pievienot funkciju 'add' ,  kur var pievienot studentu (excel dokumentā)- (vārdu, uzvārdu visus vajadzīgos datus, lai apreiķinātu gala atzīmi)
def add_students ():
    df = datu_nolasīšana()
    vards = input('Ievadi vārdu: ')
    uzvārds = input('Ievadi uzvārdu: ')
    try:
        M = float(input('Ievadi M: '))
        K = float(input('Ievadi K: '))
        T = float(input('Ievadi T: '))
        E = float(input('Ievadi E: '))
    except ValueError:
        print('erorr')
        return

    jauns = pd.DataFrame ([{'Vārds': vards, 'Uzvārds': uzvārds, 'M' : M, 'K': K, 'T': T, 'E': E}])
    df = pd.concat([df, jauns], ignore_index=True)
    saglabā_datus(df)
    print("Skolēns pievienots veiksmīgi.")



#Pievienot funkciju 'delete', kur ir iespējams izdzēst kādu studentu 

def delete_students():
    df = datu_nolasīšana()
    vards = input('Ievadi vārdu: ').strip().lower()
    uzvārds = input('Ievadi uzvārdu: ').strip().lower()

    atrod = ~((df['Vārds'].str.strip().str.lower() == vards) & (df['Uzvārds'].str.strip().str.lower() == uzvārds))
    if atrod.sum() == len(df):
        print("Skolēns netika atrasts.")
    else: 
        df_filtrets = df[atrod]
        df_filtrets.to_excel('atzimes.xlsx', index=False)
        print("Skolēns veiksmīgi dzēsts.")

if __name__ == "__main__":
    izvele()