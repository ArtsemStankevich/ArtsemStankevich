package main
import (
	"fmt"
	"math/big"
)

func main(){
	a:= big.NewInt(20000)
	//fmt.Printf("%T", a)
	//fmt.Print(Fib(a))
	i:= big.NewInt(0)
	dwa := big.NewInt(2)
	jeden := big.NewInt(1)
	fib_sum := big.NewInt(0)
	fib1 := big.NewInt(1)
	fib2 := big.NewInt(1)
	b:= a.Sub(a, dwa)
	for i.Cmp(b)==-1{
		fib_sum= big.NewInt(0)
		fib_sum.Add(fib1, fib2)
		fib1 = fib2
		fib2 = fib_sum
		i.Add(i, jeden)
		//fmt.Println(fib_sum)

	}
	fmt.Println(fib_sum)

}
/*
func Fib(a *big.Int) (answ *big.Int){
	c:=big.NewInt(2)
	d:=big.NewInt(1)
	if a.Cmp(c)==1{
		return big.NewInt(0)
	}
	return a.Add(Fib(a.Sub(a, d)), Fib(a.Sub(a, c)))



}
*/