"""
Jolan ARNAUD
Executable with input/output in terminal
Rounds hex RGB colors in a 17*17*17 RGB cube 
hexcode will be thus simplified to a #aabbcc format
(maybe do that with Lab too ?)
"""

import os

clear = lambda: os.system('cls')


def channel_rounder(hex_channel:str) -> str:

    int_channel = int(hex_channel,16) + 8

    rounded_hex_channel = hex(int_channel//17 * 17)[2:]
    
    if rounded_hex_channel == "0": rounded_hex_channel = "00"
    return rounded_hex_channel
    
def convert():
    clear()
    color = input(" Couleur : ")
    if color[0] == "#" : color = color[1:]

    print("Résultat :",
          "#"+
          channel_rounder( color[:2] )+
          channel_rounder( color[2:4] )+
          channel_rounder( color[4:] ),
          "\n"
          )

convert()