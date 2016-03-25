listdot = ["   ", "   1", "  1 ", "  11", " 1  ", " 1 1", " 11 ", " 111", "1   ", "1  1", "1 1 ", "1 11", "11  ", "11 1", "111 ", "1111"]

data1='''
377abcaf 271c0003 0241dd5f 17000000 00000000 58000000 00000000 BAF0646A 00221bc9
C273209c aa0f0a55 3f195b82 2e8172d5 83000001 04060001 09170007 0b010001 23030101
'''

data2='''
055d0000 01000c11 00080a01 D1Da43c2 00000501 111b0064 006f006e 00740066 00750063
006b0069 00740075 00700000 00140a01 0080f1f4 ceac5ed1 01150601 00208080 81000000
'''
#
# for ch in data1 :
#     if ch == "\n" :
#         print ("")
#     elif  ch == " " :
#         continue
#     else:
#         n = int(ch.lower(), 16)
#         print(listdot[n], end="" )
#
# for ch in data2 :
#     if ch == "\n" :
#         print ("")
#     elif  ch == " " :
#         continue
#     else:
#         n = int(ch.lower(), 16)
#         print(listdot[n], end="" )
# exit()

liststrdword1 = data1.split()
liststrdword2 = data2.split()



def char44 (strdword):
    chara = chr(int(strdword[0:2],16))
    charb = chr(int(strdword[2:4],16))
    charc = chr(int(strdword[4:6],16))
    chard = chr(int(strdword[6:8],16))
    return chard + charc + charb + chara


# liststrdword1 = [ char44(aa) for aa in liststrdword1 ]
# liststrdword2 = [ char44(aa) for aa in liststrdword2 ]

listhex1 = [ int(aa,16) for aa in liststrdword1 ]
listhex2 = [ int(aa,16) for aa in liststrdword2 ]

import struct
f = open('file','wb')
s = struct.pack('B', int("ac",16) )
f.write(s)

for val in listhex1 :
    s = struct.pack('>L', val)
    f.write(s)

for val in listhex2 :
    s = struct.pack('>L', val)
    f.write(s)


# s = struct.pack('L'*len(listhex1), *listhex1)
# f.write(s)
# s = struct.pack('L'*len(listhex2), *listhex2)
# f.write(s)


f.close()