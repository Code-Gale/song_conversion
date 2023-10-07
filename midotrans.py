import pretty_midi
from collections import defaultdict

# Load the identified notes from the text file
with open(input("Please input the note file's name here: "), 'r') as file:
    identified_notes = file.read().split()

# Load the tempo from the tempo.txt file (assuming it was saved in a previous step)
with open(input("Please input the tempo file's name here: "), 'r') as tempo_file:
    tempo = float(tempo_file.read())

# Automatically generate a note-to-MIDI mapping
note_to_midi = defaultdict(lambda: len(note_to_midi) + 60)

# Create a PrettyMIDI object and specify the tempo
midi_data = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Create an Instrument instance
instrument = pretty_midi.Instrument(program=0)

# Add notes to the Instrument instance
for note_name in identified_notes:
    note_number = note_to_midi[note_name]
    note = pretty_midi.Note(
        velocity=64,
        pitch=note_number,
        start=0,
        end=0.480,  
    )
    instrument.notes.append(note)

# Add the Instrument to the PrettyMIDI object
midi_data.instruments.append(instrument)

# Write the MIDI data to a file
midi_data.write(input("Enter name for output midi file: "))

print("MIDI file generated and saved as 'output_song.mid'")
