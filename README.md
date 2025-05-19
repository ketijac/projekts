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






















**Darba autori: Paula Broliša (241RDC035) un Ketija Celma (241RDC009) 15.grupa**