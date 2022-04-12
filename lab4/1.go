package main

import (
	"fmt"
	"sort"
)

//Zmienna globalna
var baza = map[int]map[string]string{
	1 : {
		"imie" : "Jan",
		"nazwisko" : "Kowalski",
	},
	2 : {
		"imie" : "Adam",
		"nazwisko" : "Nowak",
	},
}

func main(){
/*	fmt.Println(baza)

	fmt.Println(baza[1])

	fmt.Println(baza[1]["imie"])

	for klucz, wartosc := range baza {
		fmt.Println(klucz)
		fmt.Println(wartosc["nazwisko"])
	}
*/
	var opcja = 0
		//* w case korzystamy z funkcji
	for opcja != 5 {
		fmt.Println("Tu wymieniamy opcje")
		//*** zabezpieczyc Scanf przed zlymi danymi
		fmt.Scanf("%d", &opcja)
		if opcja > 0 && opcja < 5 {
			switch opcja{
			case 1:
				//**  wypisac w kolejnosci alfabetycznej
				wypis_alphabetic(baza)
			case 2:
				add(baza)
			case 3:
				Delete(baza)
			case 4:
				// w prostej wersji mozna podac "stare id" i nowe dane(calosc)
				//* modyfikacja wybranych wartosci
				mod(baza)
			case 5:
				wypis(baza)
				fmt.Println("PaPa")
			}
		}else{
			fmt.Println("Nieprawidlowy numer")
		}
	}

}

func wypis_alphabetic(baza map[int]map[string]string ){
	baza_slice := make([]string, len(baza))
	i := 0
	for _, wartosc := range baza{
		baza_slice[i] = wartosc["nazwisko"]
		i++
	}
	sort.Strings(baza_slice)
	fmt.Println(baza_slice)
}

func wypis (baza map[int]map[string]string ) {
	fmt.Println(baza)
}

func Delete (baza map[int]map[string]string ) {
	fmt.Println("Usun element")
	id := 0
	fmt.Scanf("%d", &id)
	delete(baza, id)
}

func add(baza map[int]map[string]string) {
	fmt.Println("Dodaj element")
	imie := ""
	nazwisko := ""
	id := 0
	fmt.Scan(&imie)
	fmt.Scan(&nazwisko)
	fmt.Scan(&id)
	baza[id] = make(map[string]string)
	baza[id]["imie"] = imie
	baza[id]["nazwisko"] = nazwisko
}

func mod(baza map[int]map[string]string){
	fmt.Println("Modyfikacja bazy")
	wybor := 0
	fmt.Println("Chcesz zmienic 1.imie czy 2.nazwisko")
	fmt.Scan(&wybor)
	fmt.Println("ID?")
	id := 0 
	fmt.Scan(&id)
	if wybor == 1{
		imie := ""
		fmt.Scan(&imie)
		baza[id]["imie"] = imie
	}else if wybor == 2{
		nazwisko := ""
		fmt.Scan(&nazwisko)
		baza[id]["nazwisko"] = nazwisko
	}
}