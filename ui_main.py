
from tkinter import *
from tkinter import filedialog      # searchbox
from functions import settings

font_style = 'Georgia'
filename = None

settings_data = settings.open_settings()        # access to the saved settings (settings_db.json)

window = Tk()
window.title('I am D bee - Window')
window.geometry('600x800')

# TITLE - will be a picture
w = Label(window, text ='I am D bee',
height = 2,
font = (font_style, 20))
w.pack()

checkbox = {
    'clipboard': ['imdb_link_in_clipboard', 'clipboard_button', 'Link in clipboard' ],
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Poster in a new tab' ],
    'run': ['run_by_start', 'run_by_start_button', 'Run by start' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ]
}

searchbox = {
    'movie_new_record': ['imdb_link_in_clipboard', 'clipboard_button', 'Path to the target sheet' ],
    'movies_sheet': ['title_search', 'title_search_button', 'Path to your movie database sheet' ],

}

# CHECKBOXES
for item in checkbox.values():
    item[0] = IntVar()
    item[1] = Checkbutton(
        window,
        text = item[2],
        variable = item[0], 
        height = 2,
        font = (font_style, 12)
        )
    # item[1].pack()
checkbox['clipboard'][1].pack()
checkbox['poster'][1].pack()
checkbox['run'][1].pack()
checkbox['title'][1].pack()

## TITLE SEARCH


# TITLE SEARCH - BUTTON
title_search_options = []
for item in settings_data['title_search_links'].keys():
    title_search_options = title_search_options + [item]


title_search_clicked = StringVar()

title_search_clicked.set("Hungarian")

title_search_roll_down = OptionMenu( window, title_search_clicked, *title_search_options )

title_search_roll_down.pack()

## SEARCHBOXES

searchBox_field = Text(window, height = 1, width = 50)

searchBox_field_title = Label(window, text = "Your target sheet path")
searchBox_field_title.config(font =(font_style, 12))

searchBox_field_title.pack()
searchBox_field.pack()

def browseSheet_1():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                           ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    searchBox_field.delete('1.0', END)
    searchBox_field.insert(END,filename)

button_explore = Button(window,
text = "Browse Files",
command = browseSheet_1)


button_explore.pack()

## POSTER SIZE - ROLL DOWN MENU
poster_size_options = [
  "Small",
  "Medium",
  "Larger",
  "All sizes"
]

clicked = StringVar()

clicked.set("Small")

poster_roll_down = OptionMenu( window, clicked, *poster_size_options )
poster_roll_down.pack()

settings_data = settings.open_settings()

### SAVE SETTINGS

def save():

    settings_data['path_movie_new_record'] = searchBox_field.get("1.0", "end-1c")
    settings_data['poster_size'] = clicked.get()


    settings_data['title_search'] = checkbox['title'][0].get()      # from CHECKBOXES for loop: variable = item[0] -> item[0] = checkbox['title'][0]
    settings_data['title_search_link_selected'] = title_search_clicked.get()

    settings.save_settings(settings_data)


button_save_settings = Button(window,
text = "Save settings",
command = save)

button_save_settings.pack()


window.mainloop()

'''
Information from the user

checkbox: 4
searchbox: 2
field: 1
rolldown: 1

checkbox     "imdb_link_in_clipboard": true,     mandatory
searchbox    "path_movies_sheet": "",
searchbox    "path_movie_new_record": "",        mandatory
checkbox     "title_search": true,
field        "title_search_link": "",            if "title_search": true - mandatory // roll down menu? greyed out otherwise? - able to add new link?
checkbox     "poster_open_in_new_tab": true,
rolldown     "poster_size": "",                  small by default / medium / larger // greyed out otherwise?
checkbox     "run_by_start": false

button - save current settings - message: will load automatically with next start

'''