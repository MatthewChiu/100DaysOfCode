# For the Metric Type neural network model that I've been working on with Jason (Yust), since the YCAC is made of salami slices, the weights take pitches into account twice!
# To get around that, pitches that are repeated between chords are removed: [{C4, G4}, {E4, G4}, {E4, G4, A4}] would be filtered to: [{C4, G4}, {E4}, {A4}]

# Though it doesn't make sense out of context, I've attached the function.

def commontoneNoteFilterer (piece):
    newPiece = []
    for index, chord in enumerate(piece):
        if index == 0:
            newPiece.append(chord)
        if index > 0:
            temporaryChord = []
            temporaryChord.append(chord[0])
            temporaryChord.append([])
            previousChord = [p.midi for p in piece[index-1][1].pitches]
            midiForm = [p.midi for p in chord[1].pitches] 
  
            for currentNote in midiForm:
                if currentNote in previousChord:
                    continue
                else:
                    temporaryChord[1].append(currentNote)
            if not temporaryChord[1]:
                continue
            else:
                newChord = m21.chord.Chord(temporaryChord[1])
                temporaryChord[1] = newChord
                newPiece.append(temporaryChord)
    return newPiece
