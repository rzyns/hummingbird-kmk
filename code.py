print("Clickity-clack!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, intify_coordinate as ic

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D6, board.D7, board.D8, board.D9, board.D10)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3, board.D4, board.D5)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

L = len(keyboard.col_pins)

P00 = 0
P01 = 1
P02 = 2
P03 = 3
P04 = 4
P05 = 5
P06 = 0
P07 = 1
P08 = 2
P09 = 3
P10 = 4

keyboard.coord_mapping = [
    ic(P00, P06, L), ic(P01, P06, L), ic(P00, P07, L), ic(P01, P07, L), ic(P00, P08, L),        ic(P01, P08, L), ic(P00, P09, L), ic(P01, P09, L), ic(P00, P10, L), ic(P01, P10, L),
    ic(P02, P06, L), ic(P03, P06, L), ic(P02, P07, L), ic(P03, P07, L), ic(P02, P08, L),        ic(P03, P08, L), ic(P02, P09, L), ic(P03, P09, L), ic(P02, P10, L), ic(P03, P10, L),
                     ic(P04, P06, L), ic(P05, P06, L), ic(P04, P07, L),                                          ic(P05, P08, L), ic(P04, P09, L), ic(P05, P09, L),
                                                       ic(P05, P07, L), ic(P04, P08, L),        ic(P05, P10, L), ic(P04, P10, L),
]

print(keyboard.coord_mapping)

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,        KC.Y,    KC.U, KC.I,     KC.O,   KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G,        KC.H,    KC.J, KC.K,     KC.L,   KC.SCOLON,
              KC.X, KC.C, KC.V,                       KC.M, KC.COMMA, KC.DOT,
                          KC.B, KC.SPC,      KC.BSPC, KC.N,
    ],
]

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
