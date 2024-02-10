import datetime

class Note:
    # Store the next available id for all new notes
    last_id = 0

    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        Note.last_id += 1
        self.id = Note.last_id

    def match(self, filter):
       return filter in self.memo or filter in self.tags 

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))
    
    def delete_note(self, id):
        todelete = -1
        for i in range(len(self.notes)):
            if self.notes[i].id == id:
                todelete = i
                break
        if todelete > -1:
            return self.notes.pop(todelete)                
        return None
            
    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        result=[]
        for note in self.notes:
            if note.match(filter):
                result.append(note)
        return result
    
