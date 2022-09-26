print("Clickity-clack!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, intify_coordinate as ic

from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot

keyboard = KMKKeyboard()

oneshot = OneShot()
oneshot.tap_time = 1500

keyboard.modules.append(Layers()) 
keyboard.modules.append(oneshot)

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
                     ic(P01, P06, L), ic(P00, P07, L), ic(P01, P07, L), ic(P00, P08, L),        ic(P01, P08, L), ic(P00, P09, L), ic(P01, P09, L), ic(P00, P10, L),
    ic(P00, P06, L), ic(P03, P06, L), ic(P02, P07, L), ic(P03, P07, L), ic(P02, P08, L),        ic(P03, P08, L), ic(P02, P09, L), ic(P03, P09, L), ic(P02, P10, L), ic(P01, P10, L),
    ic(P02, P06, L), ic(P04, P06, L), ic(P05, P06, L), ic(P04, P07, L),                                          ic(P05, P08, L), ic(P04, P09, L), ic(P05, P09, L), ic(P03, P10, L),
                                                       ic(P05, P07, L), ic(P04, P08, L),        ic(P05, P10, L), ic(P04, P10, L),
]

ALPHA = 0
SYM = 1
NUM = 2
NAV = 3
RFN = 4
LFN = 5

keyboard.keymap = [
    # ALPHA
    [
              KC.W, KC.E, KC.R,             KC.T,                                  KC.Y,    KC.U,    KC.I,     KC.O,
        KC.A, KC.S, KC.D, KC.F,             KC.G,                                  KC.H,    KC.J,    KC.K,     KC.L,   KC.SCOLON,
        KC.Z, KC.X, KC.C, KC.V,                                                             KC.M,    KC.COMMA, KC.DOT, KC.SLASH,
                          KC.LT(SYM, KC.B), KC.SPC,                                KC.BSPC, KC.LT(NUM, KC.N),
    ],

    # SYM
    [
                  KC.AT,    KC.HASH, KC.DLR,     KC.PERC,                          KC.CIRC,    KC.AMPR,          KC.ASTR,     KC.UNDS,
        KC.TAB,   KC.MINS,  KC.EQL,  KC.EXLM,    KC.SCOLON,                        KC.BSLS,    KC.GRAVE,         KC.LPRN,     KC.RPRN,  KC.ENT,
        KC.COMMA, KC.DOT,   KC.BSLS, KC.QUOT,                                                  KC.LBRC,          KC.RBRC,     KC.LCBR,  KC.RCBR,
                                     KC.NO,      KC.SPC,                           KC.BSPC,    KC.MO(NAV),
    ],

    # NUM
    [
                  KC.LPRN,  KC.LCBR, KC.LBRC,    KC.NO,                            KC.EQL,     KC.N7,            KC.N8,       KC.N9,
        KC.TAB,   KC.UNDS,  KC.PLUS, KC.RPRN,    KC.COLON,                         KC.N0,      KC.N4,            KC.N5,       KC.N6,    KC.ENT,
        KC.LABK,  KC.RABK,  KC.BSLS, KC.DQUO,                                                  KC.N1,            KC.N2,       KC.N3,    KC.QUES,
                                     KC.MO(NAV), KC.SPC,                           KC.BSPC,    KC.NO,
    ],

    # NAV
    [
                           KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                    KC.HOME,    KC.NO,            KC.NO,       KC.NO,
        KC.TRNS,           KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.LEFT,  KC.ENT,
        KC.OS(KC.MO(RFN)), KC.TRNS,  KC.TRNS, KC.TRNS,                                         KC.PGDN,          KC.PGUP,     KC.END,   KC.OS(KC.MO(LFN)),
                                     KC.NO,   KC.SPC,                              KC.BSPC,    KC.NO,
    ],

    # RFN
    [
                  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                             KC.F11,   KC.F7, KC.F8, KC.F9,
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                             KC.F10,   KC.F4, KC.F5, KC.F6, KC.NO,
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,                                                KC.F1, KC.F2, KC.F3, KC.NO,
                                     KC.NO,   KC.SPC,                              KC.BSPC,  KC.NO,
    ],

    # LFN
    [
                KC.F7,  KC.F8, KC.F9, KC.F11,                                      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.NO,  KC.F4,  KC.F5, KC.F6, KC.F10,                                      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.NO,  KC.F1,  KC.F2, KC.F3,                                                       KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                               KC.NO, KC.SPC,                                      KC.BSPC, KC.NO,
    ],
]

# keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
