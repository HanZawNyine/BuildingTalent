package main

import "fmt"

type secretAgent struct {
	person
	licenseToSkill bool
}

type person struct {
	Fname string
	Lname string
}

//var x int

func (sa secretAgent) speak() {
	fmt.Println(sa.Fname, sa.Lname, `: Good Morning!,"James"`)
}
func (p person) speak() {
	fmt.Println(p.Fname, p.Lname, `: Good Morning!,"James"`)
}

type human interface {
	speak()
}

func saySomething(h human) {
	h.speak()
}

func main() {

	sa1 := secretAgent{
		person{"James", "Bond"},
		true}
	saySomething(sa1)
	//sa1.speak()
	//sa1.person.speak()

	p1 := person{"Han", "Zaw"}
	saySomething(p1)
	//p1.speak()

	//fmt.Println(p1)

	//xi := []int{1, 2, 3, 4, 5}
	//fmt.Println(xi)
	//fmt.Printf("%T\n", xi)
	//
	//m := map[string]int{"Jhon": 4, "Job": 34}
	//fmt.Println(m)
	//fmt.Printf("%T", m)

	//x = 7
	//fmt.Println(x)
	//fmt.Printf("%T", x)
}
