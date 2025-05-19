import pandas as pd

def izvele():
    while True:
        print("\nIzvēlies funkciju:")
        print("1. print - Izdrukāt visus datus")
        print("2. final - Izdrukāt visus datus ar aprēķinātām gala atzīmēm ")
        print("3. sort - Izdrukāt sakārtotus gala rezultātus")
        print("4. add - Pievienot studentu")        
        print("5. delete - Dzēst studentu")
        print("6. exit - Iziet")

        komanda = input(">> ").strip().lower()

        if komanda == "print":
            izdruka_datus()
        elif komanda == "final":
            gala()
        elif komanda == "sort":
            sakārtots_rezultats(df, klases_vidējaisd)
        elif komanda == "add":
            add_students()
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
    
    atzīme = 0.1 * row['M'] + 0.35* row['K'] + 0.05 * row['T']+ 0.5 * row ['E'] # apreiķina gala atzīmi, katram studentam
    return round(atzīme, 1)  # noapaļo līdz vienam skaitlim aiz komata

df = datu_nolasīšana()
df['Gala atzime'] = df.apply(gala_atzime, axis=1)

klases_vidējaisd = round(df['Gala atzime'].mean(), 1) # apreķina klases vidējo ( no gala atzīmēm)

def gala ():
    df = datu_nolasīšana()
    df['Gala atzime'] = df.apply(gala_atzime, axis=1)
    print(df)


def sakārtots_rezultats(df, klases_vidējaisd):
    df= datu_nolasīšana()
    df['Gala atzime'] = df.apply(gala_atzime, axis=1)
    klases_vidējaisd = round(df['Gala atzime'].mean(), 1)
    kārto_dilstosi = df.sort_values(by = 'Gala atzime', ascending= False) #sakārtot studentus dilstošā secībā

    virs_linijas = True #atzīmē ar ---------- klases vidējo ( tā lai tiem kuriem ir augstāka par vidējo ir virs līnijas, sekojošie tiem kuriem ir zemāka, zem līnijas)
    for _, row in kārto_dilstosi.iterrows():
        if virs_linijas and row['Gala atzime'] < klases_vidējaisd:
            print (f"-------------------Studentu vidējā atzime: {klases_vidējaisd}")
            virs_linijas = False
        print(f"{row['Vārds']} {row['Uzvārds']} - {row['Gala atzime']}")
    

def add_students ():    #tiek pievienots students (excel dokumentā)- (vārds, uzvārds, visi vajadzīgie dati, lai apreķinātu gala atzīmi)
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
    print("Students pievienots veiksmīgi.")


def delete_students():  #iespējams izdzēst kādu studentu 
    df = datu_nolasīšana()
    vards = input('Ievadi vārdu: ').strip().lower()
    uzvārds = input('Ievadi uzvārdu: ').strip().lower()

    atrod = ~((df['Vārds'].str.strip().str.lower() == vards) & (df['Uzvārds'].str.strip().str.lower() == uzvārds))
    if atrod.sum() == len(df):
        print("Students netika atrasts.")
    else: 
        df_filtrets = df[atrod]
        df_filtrets.to_excel('atzimes.xlsx', index=False)
        print("Students veiksmīgi dzēsts.")

if __name__ == "__main__":
    izvele()