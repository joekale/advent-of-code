project("Day 1")

file(STRINGS "input.in" EXPENSES)

set(answer "")

foreach(X IN LISTS EXPENSES)
    if(NOT ${answer} EQUAL "")
	break()
    endif()

    foreach(Y IN LISTS EXPENSES)
	if("${X}" EQUAL "${Y}")
	    continue()
	endif()
	math(EXPR added "${X} + ${Y}")
	if(${added} EQUAL "2020")
	    math(EXPR answer "${X} * ${Y}")
	    break()
	endif()
    endforeach()
endforeach()

message("Day 1 Part 1 Answer: " ${answer})

set(answer "")

foreach(X IN LISTS EXPENSES)
    if(NOT ${answer} EQUAL "")
	break()
    endif()

    foreach(Y IN LISTS EXPENSES)
	if("${X}" EQUAL "${Y}")
	    continue()
	endif()

	if(NOT ${answer} EQUAL "")
	    break()
	endif()

	foreach(Z IN LISTS EXPENSES)
	    if("${Z}" EQUAL "${X}" OR "${Z}" EQUAL "${Y}")
		continue()
	    endif()
	    math(EXPR added "${X} + ${Y} + ${Z}")
	    if(${added} EQUAL "2020")
		math(EXPR answer "${X} * ${Y} * ${Z}")
		break()
	    endif()
	endforeach()
    endforeach()
endforeach()

message("Day 1 Part 2 Answer: " ${answer})
