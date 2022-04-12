package main

import (
	"fmt"
	"strconv"
)

func main(){
	slowo := "MiZa"
	result := ""
	for i:=0; i<len(slowo); i++{
		x := int(slowo[i])
		result = result + strconv.Itoa(x)
		fmt.Println(result)
	}
	fmt.Println(result)
}