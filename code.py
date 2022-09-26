print("Clickity-clack!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D6, board.D7, board.D8, board.D9, board.D10)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3, board.D4, board.D5)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [KC.Q, KC.Q, KC.Q, KC.Q, KC.Q],
    [KC.Q, KC.Q, KC.Q, KC.Q, KC.Q],
    [KC.Q, KC.Q, KC.Q, KC.Q, KC.Q],
    [KC.Q, KC.Q, KC.Q, KC.Q, KC.Q],
    [KC.Q, KC.Q, KC.Q, KC.Q, KC.Q],
    [KC.Q, KC.Q, KC.Q, KC.Q, KC.Q],
]

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
