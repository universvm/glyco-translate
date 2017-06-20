#The 14 letter code format is:
#hexose, hexnac, deoxyhexose, neuac, neugc, pentose, so3h (sulfate), po3h (phosphate), kdn, kdo, hexa #Hexuronate, methyl acetyl, other
# RULES:
# A, antennary = hexnac (glucnac)
# G, galactosylation = hexose (galactose)
# S, sialynation = neuac (or NeuGC)
# F, fucosylation = deoxyhexose (deoxygalactose)
# B, bisection = hexnac (glucnac)
# core = 2 hexnac (glucnac) + 3 hexose (mannose)
# Core F = 2 hexnac (glucnac) + 3 hexose (mannose) + 1 deoxyhexose (deoxygalactose)
# Man = hexoses
# Hy = 3 hexnac + 5 hexose
# M = 2 hexnac + 5 hexose
# C = 4 hexnac + 3 hexose


#keep the n-n2

# if n > 9: number with , eg 14,8888888888888

table = open('table1.csv', 'r')
glycosuite = ""
def translator(oxglycan):
    "Receives glycans in Oxford Format and translates them into Glycosuite 14"
    for g in oxglycan:
        if "core F" in g: #otherwise it will be split
            g = "32100000000000"
            print(g)
        else:
            g1 = g.rsplit(' ', 1)
            print(g1)
            if "Man" in g1[0]:
                man = g1[0].split("Man") #splitting by Man to get a list
                # print(man)
                if "-" in man[1]: # if there is a range
                    num = man[1].split("-")
                    num[0] += "0" *(14 -len(num[0]))
                    num[1] += "0" *(14 -len(num[1]))
                    print(num[0]);print(num[1])
                else: #else man[1] is a single integer
                    man[1] += "0" *(14 -len(man[1]))
                    print(man[1])
            # elif "M" in g:
                #
            elif "Hy" in g:
                print("53000000000000")
            else:
                print(g1[0])
        # if "Man" or "Hy" not in g:
        #     print(g)
        # else:
        #     print("ELSE")



for line in table:
    line = line.split(",")
    glycans = ''.join([x for x in line[7] if ord(x) < 128]) #Thanks to: http://snipplr.com/view/57881/
    glycans = glycans.split("; ")
    translator(glycans)
