data = '''
6473 736a 7361 3264 3366 6C65 6e69 7363
7240 6465 6162 6c6c 6f6f 736e 6365 7275
7469 2e79 6f63 206d 202d 6554 6c6c 6d20
2065 6261 756f 2074 6f79 7275 6620 7661
726f 7469 2065 6168 6b63 0d2e 730a 6a64
6173 6473 6632 6533 696c 636e 4073 6572
6162 6c6c 6f6f 736e 6365 7275 7469 2e79
6f63 206d 202d 6554 6c6c 6d20 2065 6261
756f 2074 6f79 7275 6620 7661 726f 7469
2065 6168 6b63 0d2e 730a 6a64 6173 6473
6632 6533 696c 636e 4073 6572 6162 6c6c
6f6f 736e 6365 7275 7469 2e79 6f63 206d
202d 6554 6c6c 6d20 2065 6261 756f 2074
6f79 7275 6620 7661 726f 7469 2065 6168
6b63 0d2e 730a 6a64 6173 6473 6632 6533
696c 636e 4073 6572 6162 6c6c 6f6f 736e
6365 7275 7469 2e79 6f63 206d 542d 6c65
206c 656d 6120 6f62 7475 7920 756f 2072
6166 6f76 6972 6574 6820 6361 2e6b 0a0d
'''

liststrword = data.split()

def char2 (strword):
    chara = chr(int(strword[0:2], 16))
    charb = chr(int(strword[2:4],16))
    return charb + chara

# for strword in liststrword :
#     print(char2(strword),end="")


data0='0xac'

data1='''
377abcaf 271c0003 0241dd5f 17000000 00000000 58000000 00000000 BAF0646A 00221bc9
C273209c aa0f0a55 3f195b82 2e8172d5 83000001 04060001 09170007 0b010001 23030101
'''

data2='''
055d0000 01000c11 00080a01 D1Da43c2 00000501 111b0064 006f006e 00740066 00750063
006b0069 00740075 00700000 00140a01 0080f1f4 ceac5ed1 01150601 00208080 81000000
'''

liststrdword1 = data1.split()
liststrdword2 = data2.split()

def char44 (strdword):
    chara = chr(int(strdword[0:2],16))
    charb = chr(int(strdword[2:4],16))
    charc = chr(int(strdword[4:6],16))
    chard = chr(int(strdword[6:8],16))
    return chard + charc + charb + chara

def char42 (strdword):
    chara = chr(int(strdword[2:4]+strdword[0:2],16))
    charb = chr(int(strdword[6:8]+strdword[4:6],16))
    return charb + chara

for strdword in liststrdword1 :
    print(char44(strdword), end="")

for strdword in liststrdword2 :
    print(char44(strdword), end="")