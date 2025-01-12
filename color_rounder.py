"""
Rounds color in the 16*16*16 RGB cube (maybe do that with Lab ?)
"""

def ColorConv(s):
    R = int(s,16)
    if R%17 > 8:
        R+=8
    R = hex(R//17 * 17)
    
    
    if R == "0x0":
        R = "0x00"

    return R[2]+R[3]
    
def Convert():
    color =  []
    while len(color)!=6 :
        color = input(" Couleur : ")
    print("Résultat :",
          ColorConv( color[0]+color[1] )+
          ColorConv( color[2]+color[3] )+
          ColorConv( color[4]+color[5] ),
          "\n"
          )

Convert()