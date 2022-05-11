# YOU NEED THE 'simfile' LIBRARY TO USE THIS SCRIPT!!!
# INSTALL IT WITH 'pip install simfile'
import simfile
from simfile.notes import Note, NoteData

file_path = input("Path to Simfile to convert: ")

with simfile.mutate(
    file_path,
    backup_filename=f'{file_path}.old',
) as file:
    for chart in file.charts:
        if chart.stepstype != 'dance-double':
            print("Error: Chart " + str(chart.difficulty) + " isn't dance-double, it's " + str(chart.stepstype) + " instead!")
        else:
            note_data = NoteData(chart)

            if note_data.columns == 8:
                new_notes = []

                for note in note_data:
                    new_notes.append(Note(note.beat, note.column % 4, note.note_type))
                
                note_data = NoteData.from_notes(new_notes, 4)
            
                chart.stepstype = 'dance-single'
                chart.notes = str(note_data)
            else:
                print("Error: Chart " + str(chart.difficulty) + " doesn't have 8 columns, it has " + str(note_data.columns) + " instead!")