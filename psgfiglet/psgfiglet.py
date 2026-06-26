'''
Copyright 2021-2024 PySimpleGUI. All rights reserved.

Licensed under LGPL3
'''

import PySimpleGUI as sg
import sys
import pyfiglet

version = '6.1.3'
__version__ = version.split()[0]

"""
Changelog since last major release

5.0.0   13-Feb-2024     Initial release with PSG 5     
6.0     9-Apr-2026      Moved to LGPL3 license    
                        Added "favorites" feature
6.0.1   10-Apr-2026     Made Font list expand/contract with window. Sort favorites.
6.0.2   15-Jun-2026     Added filtering of the font list to make finding fonts much easier.
6.1     17-Jun-2026     Preparing for PyPI release
6.1.1   25-Jun-2026     Added removing a font from the favorites list
                        Made resizing of window work better
                        Added option to prepend "#" onto front of each line with
                        Navigating with arrow keys while in font list will select fonts so that previewing can be done quickly
6.1.2   25-Jun-2026     Fixed setting an initial font                        
6.1.3   26-Jun-2026     Added use of new method Listbox.get_active_index rather than directly accessing tkinter widget. Included code
                        to fallback to use widget if the new method isn't found in PySimpleGUI.                        
"""


"""
    Demo pyfiglet integration

    '##:::::'##:'##::::'##::::'###::::'########::::'####::'######::
     ##:'##: ##: ##:::: ##:::'## ##:::... ##..:::::. ##::'##... ##:
     ##: ##: ##: ##:::: ##::'##:. ##::::: ##:::::::: ##:: ##:::..::
     ##: ##: ##: #########:'##:::. ##:::: ##:::::::: ##::. ######::
     ##: ##: ##: ##.... ##: #########:::: ##:::::::: ##:::..... ##:
     ##: ##: ##: ##:::: ##: ##.... ##:::: ##:::::::: ##::'##::: ##:
    . ###. ###:: ##:::: ##: ##:::: ##:::: ##:::::::'####:. ######::
    :...::...:::..:::::..::..:::::..:::::..::::::::....:::......:::
    :::'###:::::::'########:'####::'######:::'##:::::::'########:'########::'#######::
    ::'## ##:::::: ##.....::. ##::'##... ##:: ##::::::: ##.....::... ##..::'##.... ##:
    :'##:. ##::::: ##:::::::: ##:: ##:::..::: ##::::::: ##:::::::::: ##::::..:::: ##::
    '##:::. ##:::: ######:::: ##:: ##::'####: ##::::::: ######:::::: ##:::::::: ###:::
     #########:::: ##...::::: ##:: ##::: ##:: ##::::::: ##...::::::: ##::::::: ##.::::
     ##.... ##:::: ##:::::::: ##:: ##::: ##:: ##::::::: ##:::::::::: ##:::::::..::::::
     ##:::: ##:::: ##:::::::'####:. ######::: ########: ########:::: ##:::::::'##:::::
    ..:::::..:::::..::::::::....:::......::::........::........:::::..::::::::..::::::


    Adapted from code originally from this fantastic repository:
    https://github.com/nycynik/ascii-font-processor
    Thank you nycynik for a fantastic headstart

    If you are running PySimpleGUI before verion 4.35.0.11, then you'll get an error
    message saying there is a problem with:  bound method Multiline.__del__
    It's because a newer parm is used in this code.  It'll all still work just fine with this error.

    This demo has an interesting little trick.  If the window is resized, then it
    will use the new size of the Multiline element to compute the number of characters
    wide the Multiline has to work with.  This number is passed to the figlet renderer.


    ____________________________________
      ______                            
        /      /     ,            ,     
    ---/------/__-------__-----------__-
      /      /   ) /   (_ `     /   (_ `
    _/______/___/_/___(__)_____/___(__)_


    ___________________________________________________________
                  _____      __     __     _      _____  ______
                  /    '     /    /    )   /      /    '   /   
    ----__-------/__--------/----/--------/------/__------/----
      /   )     /          /    /  --,   /      /        /     
    _(___(_____/________ _/_ __(____/___/____/_/____ ___/______


"""




'''
M"""""`'"""`YM          oo          
M  mm.  mm.  M                      
M  MMM  MMM  M .d8888b. dP 88d888b. 
M  MMM  MMM  M 88'  `88 88 88'  `88 
M  MMM  MMM  M 88.  .88 88 88    88 
M  MMM  MMM  M `88888P8 dP dP    dP 
MMMMMMMMMMMMMM
'''
# --------------------------------- Main Program Layout ---------------------------------


DEFAULT_FONT = 'nancyj-fancy'


def change_theme(location):
    layout = [[sg.Text(f'Current theme {sg.theme()}')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True)
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
            break
    window.close()

    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    return None


def draw_text(font, text, width=80, prepend_hash=False):
    """Simple wrapper for the main draw function"""
    text = pyfiglet.Figlet(font=font, width=width).renderText(text)
    if prepend_hash:
        lines = text.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(f'#   {line}')
        text = '\n'.join(new_lines)
    return text

def make_window():
    # selected_font = DEFAULT_FONT
    LINE_LENGTH = 100
    MULTILINE_FONT = ('Courier', 12)
    fonts = pyfiglet.FigletFont.getFonts()
    favorite_fonts = sg.user_settings_get_entry('-favorites-', [''])
    last_used_font = sg.user_settings_get_entry('-FONT-NAME-', '')
    # sg.theme_background_color(sg.theme_input_background_color())
    # sg.theme_text_element_background_color(sg.theme_input_background_color())
    # column_left = [[sg.Table(headings=['Font Name'], values=fonts, key='-FONT-LIST-',
    #                          col_widths=[40], num_rows=30, enable_events=True, expand_y=True), sg.VerticalSeparator(pad=((5, 5), 0))],
    #                [sg.Input(s=20, k='-FILTER-')],[ sg.T('Filter')]]
    column_left = [[sg.Listbox(values=fonts, key='-FONT-LIST-',s=(30,30), justification='r', enable_events=True, expand_y=True, expand_x=True), sg.VerticalSeparator(pad=((5, 5), 0))],
                   [sg.Input(s=20, k='-FILTER-', enable_events=True)],[ sg.T('Filter', justification='c', k='-FILTER-')]]
    mline_input = sg.Multiline('PySimpleGUI', size=(40, 3), key='-TEXT-TO-SHOW-', enable_events=True, focus=True)

    column_right = [[sg.Combo(favorite_fonts, default_value=last_used_font, readonly=True, enable_events=True, k='-FAVORITES-', size=(max([len(f) for f in favorite_fonts]),30)), sg.Text("Font Name:", size=(10, 1)), sg.Input(setting=DEFAULT_FONT, size=(12, 1), key='-FONT-NAME-'), sg.B('Add to favorites', k='-ADD TO FAVORITES-'), sg.B('Remove from favorites', k='-REMOVE FROM FAVORITES-'), sg.B('Clear favorites', k='-CLEAR FAVORITES-')],
                    [sg.Text("Text:"), mline_input,
                     sg.Column([[sg.T('Font size for display below'), sg.Combo(list(range(4, 20)), 12, enable_events=True, k='-FONT-SIZE-')],
                                [sg.Checkbox('Prepend # onto front of each line', setting=False, k='-PREPEND COMMENT-', enable_events=True)]])],
                    [sg.Multiline(size=(LINE_LENGTH, 20), key='-OUTPUT-', border_width=0, font=MULTILINE_FONT, expand_x=True, expand_y=True, pad=(40, 40), write_only=True,)],
                    [sg.B('Copy to Clipboard'), sg.B('Change Theme')], ]

    layout = [[sg.Column(column_left, expand_y=False, expand_x=False), sg.Column(column_right, expand_x=True, expand_y=True, k='-COL R-')],
              [sg.Button('Exit', right_click_menu=sg.MENU_RIGHT_CLICK_DISABLED),
               sg.T('PySimpleGUI ver ' + sg.version.split(' ')[0] + ' tkinter ver ' + sg.tclversion_detailed + '  Python ver ' + sys.version, font='Default 8',
                    pad=(0, 0))], ]
    layout[-1].append(sg.Sizegrip())

    icon = b'iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAMAAAC5zwKfAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAH+UExURf/YAL2gAJB5AMysAP7XAG5dAAAAAAcFAEM4AHxpAPHMALKWACUfABQQAJiAAH9rAEA2AMurAO7JAFJFAMqrACQeACMdALWZAAsJAPbQAKGIAMipAKKJAJqCALebAGtaAAoIAD0zAG9eABgUAEs/AFVIAJV+AHhlAFFEABwXACchAMeoAOC9AKaMAGFSAOzHAAQDAPvUALGVAFlLANCwAN68ADAoAOfDAIl0ACojALOXALqdAGlYALibADcuAJZ/AJ6FAHZjANOyAFNGAA8MADEpAEQ5AAkHAHpnANi2AKyRAAYFAPzVAIBsAEo+AFBDAI95ABANANa1ACAbAPTOAPLMAOTBAE1BACwlABsWACskAEI3AFpMAHFfAIhzAMGjAGVVAAEAAEE3AGNTAKuQAPjSAH1pAB4ZAPPNAK2SAMCiAMWmAN27AIt1APXPACghACEbAL+hAA4LAFRHAHdkAJuDAMmqACYgAEk9AFxNAIFtAI54AI13AAwKAKqQAE9CANKxAKeNAObCAK6TAGxbANy6AHtoAMSmAD81AF1OANW0APnSAOPAAGZWAKmPAO3IAOXBAFhKADoxAOK/AO/KAGBRAIx2ABYSABEOAAUEAJJ7AGRUAHBeAHJgAJyEALmcAFdJAIZxANGxAKOKAAMCADsxACIcALaaAL6gAOG+AFD17/gAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALDSURBVFhH7df5W0xhFAfwS3VHUkpMqQYZ00Ixxq5FIYxMaLFEUhTJMhGFyDItpkRMdtm3/9Lcc78z7oy7vvc+jx/M55fe855zvs/TU93ucAkJ/8acuUk4WSI5hed527zU+ajNSlsQzhOkZ+DGnIWIE2Rm4ZLdomxkibJxzWzxEiSBHfescnIRFLUUHTZ5SJHIR4tJAUKkHOixWIaMGMvRZJC0AhkxCtFlsBIRsZzoMlglJriKiktKxSNBl8FqMWCNcC4rX+sUS34dNVm4xYD1KDnPBqo3ojRsE63zm1EKtmzdxvPbURhWIQZWooSq6h04GZYhBtagNK9WDNyJ0rxdlLcblQXqKHAPKgvspcB9qMzzUh5fhdK8/ZRXfwCleT4KbEBlgYMUeAiVBQ5ToHW/hY2U14TKpOaWliOpFBj3h8zg6LHjcf843aWtJ062nSpoL0vGjBGnkSKro6nzzNkuTOrTjVVl585jVJcibCmrxaQ+PdhSdgGT+vRiS1FJMyb1uYg1RZcwqNNlrMlIv+K08f4+DEY04quSq9iWqLvWf73CK36ffz10bvBtOMkT36IHqgdvpty67RgSila05IXfk+/cxVkbvTOoj/uFkeF7qDTQ/7tMFPLuCyNh/Q9woeYhjao/+ztpRhDw4krRCD0JR1HJG6MscKXhVl5voTA0jkrBI0qKsvuCaMSZ8FTaacKt/qSepKEY9sdTT9CNeDo1bUOXz8OdglGMxXnWXZOT9XyC40Ij+Y6ZAdwKXmBRyUvMyXv1GocozYdUHwZ1msGaijcY1eUtllS9w7AO77GioRjjmnxY0CT9FK3CwKvHbD12VPg/YFiX4DjWFH0MYVSvTzKPZYkhjBkQUvnZTH/GkDGTPunnwD8G2zHA4EvDV6RE5Lo86DHq8gS+Rd6xOr4HfuDapODPntnysV+oEhIS/jsc9xvWwm7SqLETuAAAAABJRU5ErkJggg=='



    window = sg.Window('psgfiglet', layout, resizable=True, finalize=True, right_click_menu=['_', ['Edit Me', 'Copy', 'File Location','Exit']], icon=icon, auto_save_location=True, enable_close_attempted_event=True)

    window.settings_restore()

    window['-COL R-'].expand(True, True, True)
    # window['-OUTPUT-'].expand(True, True, False)
    # window['-FONT-LIST-'].expand(False, False, False)
    initial_font = window['-FONT-NAME-'].get()
    initial_font = DEFAULT_FONT if not initial_font else initial_font   # if blank font, then use default
    window['-OUTPUT-'].update(draw_text(initial_font, 'PySimpleGUI').strip())
    window['-FONT-LIST-'].bind('<Down>', '+DOWN')
    window['-FONT-LIST-'].bind('<Up>', '+UP')
    return window

#   ███╗   ███╗ █████╗ ██╗███╗   ██╗
#   ████╗ ████║██╔══██╗██║████╗  ██║
#   ██╔████╔██║███████║██║██╔██╗ ██║
#   ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#   ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝


def main():

    sg.user_settings_filename(filename='psgfiglet.json')

    # sg.theme('Dark red')
    sg.theme(sg.user_settings_get_entry('-theme-', 'dark gray 13'))
    # sg.theme('Dark Gray 13')
    # sg.theme_input_background_color('#36393F')
    # sg.theme_background_color('#36393F')
    # sg.theme_input_text_color('white')
    window = make_window()
    MULTILINE_FONT = ('Courier', 12)
    fonts = pyfiglet.FigletFont.getFonts()
    favorite_fonts = sg.user_settings_get_entry('-favorites-', [''])
    favorite_fonts = [x for x in favorite_fonts if x.strip()]
    favorite_fonts.sort()

    while True:  # Event Loop
        event, values = window.read()
        # print(event,values)
        if event in ('Exit', sg.WIN_CLOSED, sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
            window.settings_save(values)
            break
        if event == '-FONT-SIZE-':
            MULTILINE_FONT = (MULTILINE_FONT[0], values['-FONT-SIZE-'])
            window['-OUTPUT-'].update(font=MULTILINE_FONT)
            window.refresh()
        elif event == '-FONT-LIST-':
            #first one is the selected, no multi-select allowed.
            selected_font = values['-FONT-LIST-'][0]
            window['-FONT-NAME-'].update(selected_font)
            values['-FONT-NAME-'] = selected_font
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'File Location':
            sg.popup_scrolled('This Python file is:', __file__)
        elif event == '-FAVORITES-':
            selected_font = values['-FAVORITES-']
            window['-FONT-NAME-'].update(selected_font)
            values['-FONT-NAME-'] = selected_font
        elif event.endswith(('+DOWN', '+UP')):      # if using arrow keys in the list of fonts
            try:
                index = window['-FONT-LIST-'].get_active_index()              # New method coming to PSG version 6.3
            except AttributeError:
                # print('Note - get_active_index not found. Using fallback implementation')
                index = window['-FONT-LIST-'].widget.index(sg.tk.ACTIVE)
            selected_font = fonts[index]
            window['-FONT-LIST-'].update(set_to_index=index)
            window['-FONT-NAME-'].update(selected_font)
            values['-FONT-NAME-'] = selected_font

        # Show the new figlet if something changed
        if event in ('Show', '-TEXT-TO-SHOW-', '-FONT-SIZE-', '-FONT-LIST-', '-FAVORITES-', '-PREPEND COMMENT-', '-FONT-LIST-+UP', '-FONT-LIST-+DOWN'):
            text = values['-TEXT-TO-SHOW-']
            selected_font = values['-FONT-NAME-']
            if text.strip() == '':
                text = selected_font.strip()
            if not selected_font:
                selected_font = favorite_fonts[0]
                window['-FONT-NAME-'].update(selected_font)
                values['-FONT-name-'] = selected_font
            # fancy way of detecting the size of the multiline so the window can be resized
            # line_length = window["-OUTPUT-"].get_size()[0] // sg.Text.char_width_in_pixels(MULTILINE_FONT)
            line_length = window["-OUTPUT-"].get_size()[0] // sg.tkinter.font.Font(font=MULTILINE_FONT).measure('A')
            window['-OUTPUT-'].update(draw_text(selected_font, text, line_length, prepend_hash=values['-PREPEND COMMENT-']).rstrip())
        elif event.startswith('Copy'):
            sg.clipboard_set(window['-OUTPUT-'].get())
        elif event == 'Change Theme':
            if change_theme(window.current_location()):
                window.close()
                window = make_window()
        elif event == '-ADD TO FAVORITES-':
            favorite_fonts.append(values['-FONT-NAME-'])
            favorite_fonts = list(set(favorite_fonts))  # remove dupes
            favorite_fonts.sort()
            sg.user_settings_set_entry('-favorites-', favorite_fonts)
            window['-FAVORITES-'].update(value=values['-FONT-NAME-'], values=favorite_fonts)
        elif event == '-REMOVE FROM FAVORITES-':
            favorite_fonts.remove(values['-FONT-NAME-'])
            sg.user_settings_set_entry('-favorites-', favorite_fonts)
            value = favorite_fonts[0] if len(favorite_fonts) else ''
            window['-FAVORITES-'].update(value=value, values=favorite_fonts)
        elif event == '-CLEAR FAVORITES-':
            favorite_fonts = []
            sg.user_settings_set_entry('-favorites-', favorite_fonts)
            window['-FAVORITES-'].update(values=favorite_fonts)
        elif event == '-FILTER-':
            if values[event] == '':
                font_list = fonts
            else:
                font_list = list(font for font in fonts if values[event] in font)
            window['-FONT-LIST-'].update(font_list)



    window.close()

if __name__ == '__main__':
    main()
