package main

import "fmt"

// Check if a given positive number is prime
func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	if num == 2 {
		return true
	}
	for i := 2; i < num/2; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	for i := 0; i < 1000; i++ {
		fmt.Println(i, " - ", isPrime(i))
	}

}
