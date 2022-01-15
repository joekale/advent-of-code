project("Day 2")

file(STRINGS "input.in" LINES)

set(answer 0)

foreach(LINE IN LISTS LINES)
    separate_arguments(args UNIX_COMMAND ${LINE})
    list(GET args 0 rule)
    list(GET args 1 letter)
    list(GET args 2 password)

    string(LENGTH ${rule} rule_length)
    string(LENGTH ${password} password_length)
    string(FIND ${rule} "-" min_end)
    string(SUBSTRING ${rule} 0 ${min_end} min)
    math(EXPR min_end "${min_end} + 1")
    string(SUBSTRING ${rule} ${min_end} -1 max)

    string(SUBSTRING ${letter} 0 1 letter)

    set(count 0)
    set(start 0)
    while(${start} LESS ${password_length})
	string(SUBSTRING ${password} ${start} 1 char)
	string(COMPARE EQUAL ${char} ${letter} matches)
	if(${matches})
	    math(EXPR count "${count} + 1")
	endif()
	math(EXPR start "${start} + 1")
    endwhile()

    if(${count} GREATER_EQUAL ${min} AND ${count} LESS_EQUAL ${max})
	math(EXPR answer "${answer} + 1")
    endif()
endforeach()

message("Day 2 Part 1 Answer: " ${answer})

set(answer 0)

foreach(LINE IN LISTS LINES)
    separate_arguments(args UNIX_COMMAND ${LINE})
    list(GET args 0 rule)
    list(GET args 1 letter)
    list(GET args 2 password)

    string(LENGTH ${rule} rule_length)
    string(LENGTH ${password} password_length)
    string(FIND ${rule} "-" pos_first_end)
    string(SUBSTRING ${rule} 0 ${pos_first_end} pos_first)
    math(EXPR pos_first "${pos_first} - 1")
    math(EXPR pos_first_end "${pos_first_end} + 1")
    string(SUBSTRING ${rule} ${pos_first_end} -1 pos_second)
    math(EXPR pos_second "${pos_second} - 1")

    string(SUBSTRING ${letter} 0 1 letter)

    set(count 0)
    set(start 0)
    string(SUBSTRING ${password} ${pos_first} 1 char)
    string(COMPARE EQUAL ${char} ${letter} first_matches)
    string(SUBSTRING ${password} ${pos_second} 1 char_second)
    string(COMPARE EQUAL ${char_second} ${letter} second_matches)
    set(first FALSE)
    set(second FALSE)
    if(${first_matches} AND NOT ${second_matches})
	set(first TRUE)
    endif()

    if(NOT ${first_matches} AND ${second_matches})
	set(second TRUE)
    endif()

    if(${first} OR ${second})
	math(EXPR answer "${answer} + 1")
    endif()
endforeach()

message("Day 2 Part 2 Answer: " ${answer})
