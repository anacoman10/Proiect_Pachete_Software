/*1. Să se importe datele referitoare la produsele vandute din Excel în SAS Studio 
și să se creeze un set de date persistent pe baza acesteia.*/

libname proiect '/home/u63378497/ProiectPacheteSoftware';
FILENAME REFFILE '/home/u63378497/ProiectPacheteSoftware/ProduseVandute.xlsx';
PROC IMPORT DATAFILE=REFFILE
	DBMS=XLSX
	OUT=proiect.baza_date replace;
	SHEET='Sheet1';
	GETNAMES=YES;
RUN;
TITLE "Vanzari de produse electronice, electrocasnice si accesorii";
PROC CONTENTS DATA=proiect.baza_date


/*2. Să se definească un format care să transforme numele județelor în codurile lor corespunzătoare 
(Constanța - CT, București - B, Cluj - CJ, Iasi - IS) 
și apoi să se verifice câte comenzi sunt înregistrate pentru fiecare județ în parte.*/

proc format;
value $judet 'Constanta' = 'CT'
'Bucuresti' = 'B'
'Cluj' = 'CJ' 'Iasi' = 'IS';
run;


proc print data=proiect.baza_date; 
format Judet $judet. ;
run;
title "Frecventa de aparitie pentru fiecare judet"; 
proc FREQ data=proiect.baza_date;
       TABLES Judet /nocum nopercent; 
       FORMAT Judet $judet.;
run;


/*3. Utilizând setul de date importat, să se afișeze toate produsele 
din categoria „Electronice” care au cantitatea vândută cuprinsă între 2 și 2 bucăți.*/


title "Achizitii de produse electronice care au cantitatea vândută cuprinsă între 2 și 3 bucăți.";
proc print data=proiect.baza_date;
where Categorie eq 'Electronice' and (CantitateVanduta between 2 and 3);
var DataComandarii Categorie Produs CantitateVanduta;
run;



/*4. Directorul firmei de aprovizionări dorește să analizeze datele înregistrate pentru fiecare oraș în parte din anul 2023.*/
DATA proiect.bucuresti; SET proiect.baza_date;
WHERE Oras eq 'Bucuresti' AND YEAR(DataComandarii) eq 2023;
RUN;
DATA proiect.iasi; SET proiect.baza_date;
WHERE Oras eq 'Iasi' AND YEAR(DataComandarii) eq 2023;
RUN;
DATA proiect.constanta; SET proiect.baza_date;
WHERE Oras eq 'Constanta' AND YEAR(DataComandarii) eq 2023;
RUN;
DATA proiect.cluj; SET proiect.baza_date;
WHERE Oras eq 'Cluj' AND YEAR(DataComandarii) eq 2023;
RUN;


/*5. Să se realizeze un raport privind totalul de produse vândute în fiecare județ, totodată, afișând și cât însumează acesta.*/

PROC SORT DATA = proiect.baza_date; BY judet;
PROC PRINT DATA = proiect.baza_date sumlabel = 'Total #byval(judet)' grandtotal_label = 'Total';
BY judet;
SUM CantitateVanduta;
TITLE 'Numarul de produse vandute in fiecare judet'; RUN;


/*6. Să se realizeze un raport privind cantitatea vândută din fiecare 
produs care face parte din categoria Accesorii, precum și totalul de bucăți de produse vândute din această  categorie.*/


proc sort data=proiect.baza_date; where Categorie eq 'Accesorii'; by Produs;
proc print data=proiect.baza_date
sumlabel="Total #byval(Produs)" grandtotal_label="Total";
by Produs;
sum CantitateVanduta;
title "Total cantitati de accesorii vandute";
run;



/*7. Să se identifice cele mai mici 
și cele mai mari 5 valori extreme distincte
pentru cantitatea de produse vândute.*/

PROC UNIVARIATE DATA=proiect.baza_date NEXTRVAL=5 NEXTROBS=0; VAR CantitateVanduta;
Title "Indicatori statistici cu valori limita distincte pentru cantitatile de produse vandute";
RUN;


/*8. Folosind subseturile de date generate anterior pentru fiecare oraș să se deseneze
 grafice care să ne arate cantitatea vândută din fiecare produs pentru a putea analiza cererea din fiecare oraș.*/

TITLE "Distributia produselor vandute in Bucuresti"; 
PATTERN value = solid
PROC GCHART data=proiect.bucuresti;
VBAR Produs / sumvar=CantitateVanduta
type=sum;
RUN;
QUIT;
TITLE "Distributia produselor vandute in Iasi"; 
PATTERN value = solid;
PROC GCHART data=proiect.iasi;
VBAR Produs / sumvar=CantitateVanduta
type=sum;
RUN;
QUIT;
TITLE "Distributia produselor vandute in Constanta"; 
PATTERN value = solid;
PROC GCHART data=proiect.constanta;
VBAR Produs / sumvar=CantitateVanduta
type=sum;
RUN;
QUIT;



/*Să se afișeze toate produsele din categoria "Accesorii" 
cu un preț unitar mai mic de 100 de unități monetare*/
/* PROC PRINT DATA=proiect.baza_date; */
/*    WHERE Categorie = 'Accesorii' AND PretUnitarPerReducere < 100; */
/*    VAR Produs Categorie PretUnitarPerReducere; */
/*    TITLE "Accesorii cu PretUnitar < 100"; */
/* RUN; */




title "Achizitii de accesorii care au pretul unitar cuprins între 100 și 500 unitati monetare ";
proc print data=proiect.baza_date;
where Categorie eq 'Accesorii' and (PretUnitarPerReducere between 100 and 500);
var DataComandarii Categorie Produs CantitateVanduta PretUnitarPerReducere;
run;






