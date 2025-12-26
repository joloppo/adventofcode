package main

import "core:fmt"
import "core:strings"

import "core:os"
import "core:strconv"

main :: proc() {
	filecontents, success := os.read_entire_file("tmp/day1.txt")
	assert(success)
	inputstr := string(filecontents)

	parts := strings.split(inputstr, "\n")
	int_parts := make([]int, len(parts))
	position := 50
	counter := 0
	for line, idx in parts {
		if len(line) == 0 {
			break
		}
		value, ok := strconv.parse_int(line[1:])
		assert(ok)
		if line[0] == 'L' {
			value *= -1
		}
		int_parts[idx] = value
	}

	// part1
	for value in int_parts {
		// fmt.println(value)
		position += value
		position %%= 100

		if position == 0 {
			counter += 1
		}
	}
	fmt.println(counter)

	// part2
	position = 50
	counter = 0
	for value in int_parts {
		position += value

		counter += (abs(position - 50) + 50) / 100
		if position < 0 && position - value == 0 {
			counter -= 1
		}
		position %%= 100
	}
	fmt.println(counter)
}
