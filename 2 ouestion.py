# Write a program to fill in a letter template given below with name and date.
letter = ''' dear <|NAME|>,
             you are seleted !
                <|DATE|> '''

print(letter.replace("<|NAME|>","bishab kumar").replace("<|DATE|>","21 november 2025"))