import librosa
import numpy as np

# Load an audio file
audio_file = input("Enter audio file's name: ")

# Load the audio file using Librosa
y, sr = librosa.load(audio_file)

# Extract pitch and tempo features
pitch, _ = librosa.piptrack(y=y, sr=sr)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

# Extract notes from pitch
notes = []
for frame in pitch.T:
    for freq in frame:
        if np.isfinite(freq) and freq > 0:
            note = librosa.hz_to_note(freq)
            notes.append(note)

# Convert the list of notes into a single string with spaces
notes_string = ' '.join(notes)

# Define the output file names
output_file = input("Please enter the name for the output notes file (with extension .txt): ")
tempo_file = input("Please enter the name for the output tempo file (with extension .txt): ")

# Write the identified notes as a single string to the output file
with open(output_file, 'w') as file:
    file.write(notes_string)

# Save the tempo to a separate file
with open(tempo_file, 'w') as tempo_output:
    tempo_output.write(str(tempo))

print(f"Tempo: {tempo}")
print(f"Identified Notes saved to {output_file}")
print(f"Tempo information saved to {tempo_file}")
