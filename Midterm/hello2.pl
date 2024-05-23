main :-
    write('Enter name: '),
    read_line_to_string(user_input, UserInput),
    format('Hello ~w', [UserInput]), nl.


