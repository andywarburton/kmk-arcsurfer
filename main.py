import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Press, Release, Tap, Macros, Delay
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes

print(dir(board))

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())


keyboard.diode_orientation = columns_to_anodes=DiodeOrientation.COL2ROW
keyboard.extensions.append(MediaKeys())


keyboard.col_pins = (board.GP29, board.GP28, board.GP27, board.GP26, board.GP15, board.GP14, board.GP13,)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.coord_mapping = [
0,  1,  2,  3,  4,  6,
7,  8,  9,  10, 11, 13,
14, 15, 16, 17, 18, 20, 19,
21, 22, 23, 24, 25, 27, 26,
]  

rgb = RGB(  pixel_pin=board.GP8,
            rgb_order=(0, 1, 2),  # GRB WS2812    
            num_pixels=75,
            val_limit=255,
            hue_default=75,
            sat_default=255,
            val_default=255,
            hue_step=5,
            sat_step=5,
            val_step=5,
            animation_speed=1,
            breathe_center=1,  # 1.0-2.7
            animation_mode=AnimationModes.STATIC,
            reverse_animation=False,
            refresh_rate=60,


    )
keyboard.extensions.append(rgb)


# transparent layer will default to layer beneath
___ = KC.TRNS 



keyboard.keymap = [
    [ # LAYER 0
    KC.ESC,    KC.N1, KC.N2, KC.N3,  KC.H, KC.M,    
    KC.TAB, KC.Q,  KC.W, KC.E, KC.R, KC.F,    
    KC.LSFT, KC.A, KC.S, KC.D, KC.V, KC.VOLU, KC.VOLD,    
    KC.LSFT, KC.X, KC.G, KC.B,       KC.LALT,  KC.SPC,  KC.C,    
    ],

]


if __name__ == '__main__':
    keyboard.go()
