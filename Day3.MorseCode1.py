# MORSE_CODE was a given dictionary in "code wars."

def decodeMorse(morse_code):
    temp = morse_code.split(' ')
    spaceCounter = 0
    translation = "" 
    for x in temp:
        if x == '':
            spaceCounter +=1
            continue
        if spaceCounter >= 2:
            translation = translation + str(" ")
            spaceCounter = 0
        if spaceCounter <=2:
            spaceCounter = 0
            translation = translation + str(MORSE_CODE[x])
    return translation.strip()
