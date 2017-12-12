package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("december5_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	mem := make([]int, 1000)
	for scanner.Scan() {
		lineStr := scanner.Text()
		num, _ := strconv.Atoi(lineStr)
		mem = append(mem, num)
	}
	counter := 0
	for ptr := 0; ptr < len(mem); {
		counter += 1
		old_jump := mem[ptr]
		if old_jump >= 3 {
			mem[ptr] -= 1
		} else {
			mem[ptr] += 1
		}
		ptr += old_jump
	}
	fmt.Printf("%d", counter)
}
