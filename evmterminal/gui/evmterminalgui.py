import PySimpleGUI as sg
from datetime import datetime
from brownie import *

class EVMTerminalGUI():
    """main window class for the terminal"""

    def __init__(self) -> None:
        sg.theme('black')   # Add a touch of color

    def create_top_input_row(self):
        return [[sg.Frame("Network", [[sg.Combo(['development', 'mainnet-fork-dev', 'mainnet'], readonly=True, expand_x = True),]], expand_x = True),
                 sg.Frame("Account", [[sg.Combo(['a1', 'a2', 'a4'], readonly=True, expand_x = True),]], expand_x = True),
                 sg.Frame("Contract", [[sg.Combo(['uniswap',], readonly=True, expand_x = True),]], expand_x = True),
                 sg.Frame("Function", [[sg.Combo(['swap',], readonly=True, expand_x = True),]], expand_x = True),
            ],
            ]
    
    def get_contract_inputs(self):
        return [sg.Input(), sg.Text('Some Text')]
    
    def create_function_input_row(self, call_params):
        # Define the JSON input
        function_params = []
        for param in call_params.keys():
            function_params.append([sg.Text(param), sg.Input(key=call_params[param]),])
        
        right_column = [[sg.Multiline(size=(None, 10), expand_x=True, expand_y=True, key='-TRANSACTION-', disabled=True, autoscroll = True, no_scrollbar=True)],]

        return [[sg.Frame('JSON Input', function_params, vertical_alignment='top'), sg.Frame('Transaction', right_column, expand_x=True, expand_y=True)], [sg.Button('Build'), sg.Button('Execute')],] 

    def create_output_row(self):
        return [[sg.Multiline(size=(None, 20), expand_x=True, expand_y=True, key='-OUTPUT-', disabled=True, autoscroll = True, no_scrollbar=True)],]



    def create_main_layout(self):
        test_input = {
            "param1": "",
            "param2": "",
            "param3": 5, 
            "param4": 12,
        }
        layout = [
                [sg.Frame('', self.create_top_input_row(), expand_x=True, border_width=0)],
                [sg.Frame('', self.create_function_input_row(test_input), border_width=0, expand_x=True, expand_y=True)],
                [sg.Frame('', self.create_output_row(),border_width=0, expand_x=True, expand_y=True)],
                [sg.Sizegrip()],
        ]
        return layout
    
    def run(self):
        window = sg.Window('EVM Terminal', 
                           self.create_main_layout(), 
                           margins=(0,0), 
                           background_color="#000000", 
                           no_titlebar=False, 
                           resizable=True, 
                           right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT
                           )

        while True:             # Event Loop
            event, values = window.read(timeout=1000,timeout_key='-timeout-')
            print(event, values)
            if event == '-timeout-':
                #window['-time-'].update(now())
                pass
            elif event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Edit Me':
                sg.execute_editor(__file__)
            elif event == 'Version':
                sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
            elif event == 'File Location':
                sg.popup_scrolled('This Python file is:', __file__)
        window.close()