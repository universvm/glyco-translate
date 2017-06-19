#The 14 letter code format is:
#hexose, hexnac, deoxyhexose, neuac, neugc, pentose, so3h (sulfate), po3h (phosphate), kdn, kdo, hexa #Hexuronate, methyl acetyl, other
# RULES:
# A, antennary = hexnac (glucnac)
# G, galactosylation = hexose (galactose)
# S, sialynation = neuac (or NeuGC)
# F, fucosylation = deoxyhexose (deoxygalactose)
# B, bisection = hexnac (glucnac)
# Core F = 2 hexnac (glucnac) + 3 hexose (mannose) + 1 deoxyhexose (deoxygalactose)
# Man = hexose
# Hy = 3 hexnac + 5 hexose
# M = 2 hexnac + 5 hexose
# C = 4 hexnac + 3 hexose


#keep the n-n2

# if n > 9: number with , eg 14,8888888888888
table = open('table1.csv', 'r')

def translator(oxglycan):
    "Receives glycans in Oxford Format and translates them into Glycosuite 14"
    for g in oxglycan:
        if "Man" in g: #
            print(g)
        elif "Hy" in g:
            print(g)
        elif "core F" in g:
            print(g)
        else:
            print("g")
        # if "Man" or "Hy" not in g:
        #     print(g)
        # else:
        #     print("ELSE")



for line in table:
    line = line.split(",")
    glycans = ''.join([x for x in line[7] if ord(x) < 128]) #Thanks oh kind stranger http://snipplr.com/view/57881/
    glycans = glycans.split(";")
    translator(glycans)
