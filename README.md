# Projekts - Darbības ar studentu atzīmēm matemātikā
Šī ir Python programma, kuras galvenais mērķis ir apkopot, aprēķināt, analizēt un veikt dažādas darbības ar studentu matemātikas atzīmēm.
Šādas programmas praktiskais pielietojums varētu noderēt gan skolotājiem, kas atvieglo darbu un automatizē darbu ar atzīmju aprēķināšanu, gan arī studentiem, lai uzzinātu savu līmeni starp vienaudžiem, kā arī sekotu līdzi savam progresam un plānotu savus nākamos soļus efektīvam progresam.
## Projekta uzdevums
Lai realizētu programmas mērķi tiek pievienots "atzimes.xlsx" fails, kurā ir jau esošie dati par studentiem. <br/> Kolonnās tiek dots: attiecīgi vārds, uzvārds, M, K, T, E, <br/> kur '**M**' - mājasdarbu vidējā atzīme <br/> '**K**' - kontroldarbu vidējā atzīme, <br/> '**T**' - Teorijas testu vidējā atzīme,<br/> '**E**' - Eksāmena atzīme.

Programma nodrošina dažādas funkcijas:
* print - Izdrukāt visus datus 
* final - Izdrukāt visus datus ar aprēķinātām gala atzīmēm 
* sort - Izdrukāt sakārtotus gala rezultātus 
* add - Pievienot studentu 
* delete - Dzēst studentu 
* exit - Beigt programmas darbību

### Izmantotā Python bibliotēka
Projekta izstrādes laikā tika izmantota **Pandas** bibliotēka. Izvēlējāmies lietot šo bibliotēku, jo tā spēj efektīvi un strukturēti strādāt ar tabulas veida datiem, kas mūsu programmas gadījumā ir studentu atzīmes excel failā (*atzimes.xlsx*). Tā nodrošina prasmīgas un saprotamas metodes datu ielādēšanai no excel formāta faila (*read_excel*) un to saglabāšanai (*to_excel*). 

Turklāt **Pandas** bibliotēka ļauj ērtti veik datu šķirošanu (*sort_values*), kā arī nedaudz sarežģītāku funkciju izmantošanu, kā, piemēram, pievieno katrai rindai aprēķināto gala atzīmi ar funkciju *apply*. 

Bez šīs bibliotēkas būtu ievērojami sarežģītāk nodrošināt programmas darbību, kā arī būtu nepieciešams rakstīt daudz garāku kodu un arī ar lielu kļūdu iespējamību, lai manuāli apstrādātu excel faila datus. Par cik mūsu programma ietver dažādas darbības ar datiem, kas ir skaitļi, **Pandas** ļauj veikt datu kārtošanu, skaitlisku aprēķinu veikšanu un dažādu funkciju pieprasīšanu no lietotāja puses veikt precīzi, uzskatāmi un akurāti.

### Funkciju darbību apraksts
**Izvēles funkcija - *izvele()***

Šī funkcija ir galvenais programmas vadības mehānisms pēc kā tā vadās, iesaistot lietotāja saskarsmi, ļaujot tam izvēlēties kuru apakšfunkciju izmantot vai apskatīt. Tā darbojas nepārtrauktā cilpā (*while True*), kas atkārtojas bezgalīgi, līdz lietotājs izvēlas komandu *exit*, lai pārtrauktu programmas darbību.

Tā sāk savu darbību piedāvājot lietotājam sešas izvēles iespējas - *print, add, final, sort, delete un exit*. Kad lietotājs ir ievadījis izvēlēto darbību, funkcija pārbauda ievadīto komandu un attiecīgi izsauc nākamo funkciju, kuru lietotājs ir izvēlējies. Ja ievadīta kāda cita vērtība, kas nav no piedāvātajām, tiek izvadīts kļudas paziņojums *"Nepareiza komanda. Mēģini vēlreiz."* 

Izvēles funkcija nodrošina lietotājam ērti izvēlēties vajadzīgo darbību un efektīvi iegūt rezultātus par nepieciešamo funkciju. Tā kalpo kā programmas kodols, kas garantē mijiedarbību ar citām programmas funkcijām.

**Datu nolasīšanas un saglabāšanas funkcijas - *datu_nolasīšana()* un *saglabā_datus(df)***

Funkcija *datu_nolasīšana()* ir atbildīga par datu ielādēšanu un excel faila (*atzimes.xlsx*). Izmantojot Pandas metodi *read_excel()* nolasa datus no konkrētās darba lapas *Sheet1*. Tās galvenais uzdevums ir ļaut pārējām programmas funkcijām piekļūt nolasītajiem excel datiem un strādāt ar tiem.

Funkcija *saglabā_datus(df)* saglabā izmainīto DataFrame, kurā atspoguļoti esošie un/vai mainītie dati, atpakaļ esošajā excel failā. Kā arī tiek izmantota *index=False* darbība, kas neņem vērā rindu indeksus un nepievieno tos.

**Datu drukāšanas jeb print funkcija - *izdruka_datus()***

Šī funkcija ir atbildīga par visu studentu excelī esošo datu (atzīmju) pārskatāmu un saprotamu izdrukāšanu terminālī, t.i. bez gala atzīmēm. 

Tā ielādē datus no excel faila, izmantojot funkciju *datu_nolasīšana()*, pārbauda vai eksistē kollona *Gala atzīme*, ja eksistē, tad to dzēš, lai nodrošinātu datu reālo atspoguļošanu. Kā arī tā sāk skaitīt rindas no 1 ar funkciju *df.index = range(1,len(df) + 1)* nevis no 0, ko Python programmas pēc noklusējuma dara. Un visbeidzot ar *print* darbību izdrukā datu rāmi terminālī.

**Gala atzīmes aprēķināšanas un pievienošanas funkcija - *gala_atzime(row)* un *gala()***

Funkcija *gala_atzime()* nodrošina un pievieno aprēķinus studentu gala atzīmēm, izmantojot formulu, kas balstās uz četiem iepriekšminētiem vidējo atzīmju lielumiem - M (mājasdarbiem), K(kontroldarbiem), T(testiem), E(eksāmenu).

Sākotnēji ar *pd.isna()* pārbauda vai kāds no vērtējumiem nav ievadīts kā tukšums - ja nav pieejama vērtība, programma atgriež kļūdu. Ja visas atzīmes ir pieejamas tiek veikts gala atzīmju aprēķins pēc formulas: *Gala atzīme = 0,1 * M + 0,35 * K + 0,05 * T + 0,5 * E*, kā arī ar *round(atzīme, 1)* nodrošina, ka rezultāts tiek noapaļots līdz vienam ciparam aiz komata. Ar *df['Gala atzime'] = df.apply(gala_atzime, axis=1)* tiek aprēķinātas un pievienotas gala atzīmes katram studentam jeb katrai rindiņai. Kad visu studentu gala atzīmes ir aprēķinātas, tiek rēķināts klases vidējais rezultāts.

Izvēloties *final* izvēlni programmas sākumā, tiek izvadīta funkcija *galas()*, kas izdrukā DataFrame, kurā redzamas gala atzīmes katram studentam.

**Gala atzīmju sakārtošanas funkcija - *sakartots_rezultats(df,klases_vidējaisd)***

Šīs funkcijas galvenais uzdevums ir atspoguļot sakārtotas studentu gala atzīmes, izmantojot aprēķināto klases vidējo atzīmi, parādīt, kuri studenti ir virs vidējās atzīmes un kuri - zem.

Nolasot datus no excel faila, apreķina studentu gala atzīmi un klases vidējo atzīmi. Tad tās sakārto dilstošā secībā ar *ascending= False*, lai sākotnēji atspoguļotu labākos rezultātus. Taču, lai viss būtu uzskatāmi un saprotami vajadzīgos rezultātus izdrukā vienu pēc otra, iekļaujot citādāk apzīmētu klases vidējo atzīmi, lai vizuāli labāk saprastu, kuri studenti ir zem studentu vidējās atzīmes.

**Datu pievienošanas funkcija – *add_students()***

Šī funkcija nodrošina iespēju pievienot jaunu studentu ar visām nepieciešamajām atzīmēm uz Excel datni (*atzimes.xlsx*), ievadot gan personīgu informāciju (vārds, uzvārds), gan nepieciešamās atzīmes gala vērtējuma aprēķināšanai ( ‘M’ – mājasdarbi, ‘K’ – kontroldarbi, ‘T’ – testi, ‘E’ – eksāmeni), bez ārējas failu rediģēšanas. 

Funkcija sākas ar esošo datu nolasīšanu no Excel datnes (*atzimes.xlsx*), izmantojot funkciju *datu_nolasīšana()*, kas ļauj strādāt ar jau esošu datu rāmi (DataFrame), kurā ir saglabāti jau iepriekš ievadītie studentu dati.Pēc datu nolasīšanas seko *input()* funkcijas, kuras aicina lietotājam terminālī ievadīt:
* Studenta vārdu,
* Studenta uzvārdu,
* Katru no četrām atzīmēm (M, K, T un E)

Sekojoši atzīmes, kuras tiek ievadītas tiek konvertētas uz decimālskaitļiem (*float*), izmantojot *float(input(...))* , lai pārliecinātos, ka tās ir derīgas matemātiskiem aprēķiniem. Attiecīgi, ja  ievadītās vērtības nav skaitliskas, tad tiek izvadīts kļūdas ziņojums – ‘*error*’ un funkcija tiek pārtraukta (*return*), lai novērstu nederīgu datu pievienošanu.

Turpinot ar *add_students()* funkciju, ja visi dati tika pareizi ievadīti, tad tiek veidots jauns DataFrame ieraksts ar pievienotā studenta datiem. Tālāk izmantojot (*concat*) funkciju , jaunais ieraksts tiek apvienots ar jau esošajiem datiem, kur pievienojot *ignore_index=True*, tiek nodrošināts, ka netiks pieļautas iespējamas indeksu atkārtošanās kļūdas, jo automātiski tiks veikta pārrēķināta indeksēšana.
Visbeidzot ar *saglabā_datus(df)* tiek saglabāts atjauninātais datu rāmis atpakaļ Excel failā un ar *print(“..”)* palīdzību tiek izvadīts apstiprinājuma paziņojums *"Students pievienots veiksmīgi."*

**Datu dzēšanas funkcija – *delete_students()***

Funkcija *delete_students()* garantē iespēju izdzēst konkrētu studentu no programmā izmantotās Excel datnes (*atzimes.xlsx*), pamatojoties uz lietotāja ievadīto informāciju (vārdu un uzvārdu). Attiecīgi lietotājam nav vajadzība manuāli rediģēt failu, lai izņemtu nevēlamu vai kļūdaini ievadītu ierakstu.

Funkcijas darbība sākas ar esošo datu nolasīšanu, izmantojot funkciju *datu_nolasīšana()*. Tālāk tā aicina lietotājam ievadīt studenta vārdu un uzvārdu ar *input()* darbību. Abi ievaddati tiek apstrādāti ar *.strip().lower()* metodēm, lai noņemtu liekas atstarpes un pārvērstu visu tekstu uz mazajiem burtiem, nodrošinot precīzāku salīdzinājumu. Pēc datu ievadīšanas tiek veidots filtrs *atrod = ~((df['Vārds'].str.strip().str.lower() == vards) & (df['Uzvārds'].str.strip().str.lower() == uzvārds))* ,  kas pārbauda visas rindas un atrod visus studentus, kuri neatbilst ievadītajam vārda un uzvārda salikumam (studentam, kuru vēlas dzēst) un saglabā visas šīs rindas jaunā DataFrame. Sekojoši  tiek pārbaudīts vai tika atrsts students, kuru vajag dzēst:
* Ja filtrētais rezultāts *atrod.sum()* ir tik pat garš kā sākotnējais rezultāts *len(df)* tad ir skaidrs, ka neviena rinda netika izņemta un attiecīgi students netika atrasts, par to lietotājs arī tiek informēts ar *print(“…”)* palīdzību.
* Ja filtrētais rezultāts nesakrīt ar sākotnējo rezultātu, tad ir zināms, ka students ar norādīto vārdu un uzvārdu tika atrasts. Lai šo studentu varētu izdzēst, funkcija turpinās ar jauna filtrēta datu rāmja izveidošanu *df_filtrēts = df[atrod]* , kas satur visas rindas, izņemot studentu, kuru vajadzēs dzēst. 

Pēc jaunā datu rāmja *(df_filtrets)* izveidošanas visi dati tiek pārrakstīti esošajā Excel failā (*atzimes.xlsx*) ar šādu darbību: *df_filtrets.to_excel('atzimes.xlsx', index=False)*. Šis solis aizstāj veco saturu ar jauno, kurā konkrētais students vairs neparādīsies. Parametrs *index=False* tiek izmantots, lai neiekļautu DataFrame indeksu kā papildu kolonnu failā, nodrošinot tīru un pārskatāmu rezultātu. Noslēgumā ar *print(“…”)* palīdzību lietotājs tiek informēts par veiksmīgu skolēna dzēšanu no datubāzes.

**Programmas beigšanas funkcija – *‘exit’***

Funkcija *exit* nodrošina lietotājam jebkurā brīdī pārtraukt programmas darbību un pārliecinās, ka lietotājs ir informēts par to ar paziņojumu *“Programma tiek pārtraukta”*, kas tiek īstenots ar *print(‘...’)* funkcijas palīdzību. *Exit* funkcijas beigās tiek izsaukta komanda *break*, kas pārtrauc visu *while True* ciklu, kas atrodas *izvele()* funkcijā.

## Piemērs


**Sort**

Izvēlies funkciju:
1. print - Izdrukāt visus datus
2. final - Izdrukāt visus datus ar aprēķinātām gala atzīmēm 
3. sort - Izdrukāt sakārtotus gala rezultātus
4. add - Pievienot studentu
5. delete - Dzēst studentu
6. exit - Iziet

-> sort

Elīna Bērziņa - 9.0

Kristaps Lapiņš - 8.0

-------------------Studentu vidējā atzime: 7.8

Anna Ozola - 7.1

Gusts Vītols - 7.0













**Darba autori: Paula Broliša (241RDC035) un Ketija Celma (241RDC009) 15.grupa**