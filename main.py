"""Python module that allows you to use a simple notebook."""

import datetime
from os import system


class Note:
    """Base class containing information
    about one note.


    Attributes
    ----------
    memo: str
    creation_date: date
    tags: str

    Methods
    -------
    match: bool
        Checks if the required tags are in the Note
    """

    def match(self, search_filter: str):
        """Checks if the required tags are in the Note.

        >>> Note('test', 'home homework').match('home')
        True

        >>> Note('test', 'home homework').match('fun')
        False
        """
        if search_filter in self.tags.split():
            return True
        return False

    def __init__(self, memo, creation_date, tags):
        self.memo = memo
        self.creation_date = creation_date
        self.tags = tags

    def __str__(self):
        return f'Note [memo: {self.memo}, creation date: {self.creation_date}, ' \
               f'tags: {self.tags}]'


class Notebook:
    """Class containing information
    about one notebook.


    Attributes
    ----------
    notes: list
        Contains 'Note' class objects

    Methods
    -------
    search(): list
        returns list of Notes satisfying the condition
    new_note()
        adds new Note to Notebook
    modify_memo()
        modifies memo by id
    modify_tags()
        modifies tags by id
    """

    def search(self, notes_filter: str):
        """Function returns list of Notes satisfying the condition."""
        return [note for note in self.notes if note.match(notes_filter)]

    def new_note(self, memo, tags=''):
        """Function adds new Note to Notebook."""
        self.notes.append(Note(memo, datetime.datetime.now().date(), tags))

    def modify_memo(self, note_id, memo):
        """Function modifies memo by id."""
        if 0 <= note_id < len(self.notes):
            self.notes[note_id].memo = memo

    def modify_tags(self, note_id, tags):
        """Function modifies tags by id."""
        if 0 <= note_id < len(self.notes):
            self.notes[note_id].tags = tags

    def __init__(self, notes: list):
        self.notes = notes


class CommandOption:
    """The class is responsible for the
    console interface and commands.


    Attributes
    ----------
    notebook: Notebook

    Methods
    -------
    open_notebook()
        Opens Notebook to work.
    commands()
        Shows all command anf get the command
    show()
        Shows all notes
    search(): list
        returns list of Notes satisfying the condition
    new_note()
        adds new Note to Notebook
    edit_memo()
        modifies memo by id
    edit_tags()
        modifies tags by id
    close_notebook()
        Stop commands()
    """

    cont = True

    def open_notebook(self, notebook: Notebook):
        """Opens Notebook to work."""
        self.notebook = notebook

    def commands(self):
        """Shows all command anf get the command."""
        # system('cls||clear')
        print('---------------------------------')
        print('Commands:')
        print('-- Show notes (1)')
        print('-- New note (2)')
        print('-- Edit note memo (3)')
        print('-- Edit note tags (4)')
        print('-- Search (5)')
        print('-- Close notebook (6)')
        command = int(input('Command: '))
        print()
        if command == 1:
            self.show()
        elif command == 2:
            self.new_note()
        elif command == 3:
            self.edit_memo()
        elif command == 4:
            self.edit_tags()
        elif command == 5:
            self.search()
        else:
            self.close_notebook()
        if self.cont:
            print('\n')
            self.commands()

    def show(self):
        """Function shows all notes in Notebook."""
        print('Notebook:')
        for note in self.notebook.notes:
            print(note)

    def new_note(self):
        """Function add new note."""
        memo = input('Enter memo: ')
        tags = input('Enter tags: ')
        self.notebook.new_note(memo, tags)

    def edit_memo(self):
        """Function modifies memo by id."""
        note_id = int(input('Enter note id: '))
        memo = input('Enter edited memo: ')
        self.notebook.modify_memo(note_id, memo)

    def edit_tags(self):
        """Function modifies tags by id."""
        note_id = int(input('Enter note id: '))
        tags = input('Enter edited tags: ')
        self.notebook.modify_memo(note_id, tags)

    def search(self):
        """Function returns list of Notes satisfying the condition
        and print it."""
        note_filter = input('Enter search filter: ')
        for note in self.notebook.search(note_filter):
            print(note)

    def close_notebook(self):
        """Stop commands() recursion."""
        self.cont = False

    def __init__(self, notebook: Notebook):
        self.notebook = notebook


note_b = Notebook([])
co = CommandOption(note_b)
co.commands()
