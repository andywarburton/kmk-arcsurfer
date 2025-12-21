import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Press, Release, Tap, Macros, Delay

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())


keyboard.diode_orientation = columns_to_anodes=DiodeOrientation.COL2ROW
keyboard.extensions.append(MediaKeys())


keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6,)
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D7,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.coord_mapping = [
0,  1,  2,  3,  4,5,
7,  8,  9,  10, 11, 12,
14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27,
]  



# transparent layer will default to layer beneath
___ = KC.TRNS 



keyboard.keymap = [
    [ # LAYER 0
    KC.ESC,    KC.N1, KC.N2, KC.N3,  KC.H, KC.X,    
    KC.TAB, KC.Q,    KC.W,    KC.E, KC.R,     KC.F,    
    KC.LSFT,      KC.A, KC.S, KC.D,    KC.V,     KC.VOLU, KC.VOLD,    
    KC.M, KC.G, KC.TRNS, KC.B,          KC.LALT,  KC.SPC,  KC.C,    
    ],

]


if __name__ == '__main__':
    keyboard.go()
