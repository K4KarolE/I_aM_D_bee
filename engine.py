from functions import messages
from functions import scraping
from functions import excel_sheet
from functions import own_language_title

def start_engine():     # executed with the "Save & Start" button click in main
    messages.message('bee_noise', 2, 'banner')

    titleRead, yearRead, directors, stars, genres, lengthHour, lengthMinute = scraping.web_driver()

    excel_sheet.write_sheet(titleRead, yearRead, directors, stars, genres, lengthHour, lengthMinute)

    own_language_title.search(titleRead, yearRead)

    messages.message('bee_noise', 1.5, 'outro')

    excel_sheet.launch_sheets()