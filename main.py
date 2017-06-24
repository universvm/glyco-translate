#The 14 letter code format is:
#hexose, hexnac, deoxyhexose, neuac, neugc, pentose, so3h (sulfate), po3h (phosphate), kdn, kdo, hexa #Hexuronate, methyl acetyl, other
# RULES:
# A, antennary = hexnac (glucnac)
# B, bisection = hexnac (glucnac)
# G, galactosylation = hexose (galactose)
# S, sialynation = neuac (or NeuGC)
# F, fucosylation = deoxyhexose (deoxygalactose)
# core = 2 hexnac (glucnac) + 3 hexose (mannose)
# Core F = 2 hexnac (glucnac) + 3 hexose (mannose) + 1 deoxyhexose (deoxygalactose)
# Man = X hexoses +2 HEXNAC
# Hy = 3 hexnac + 5 hexose
# M = 2 hexnac + X hexose
# C = 4 hexnac + 3 hexose
import re

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
            if "Man" in g1[0]:
                man = g1[0].split("Man") #splitting by Man to get a list
                # print(man)
                if "-" in man[1]: # if there is a range
                    num = man[1].split("-")
                    num[0] += "2"
                    num[0] += "0" *(14 -len(num[0]))
                    num[1] += "2"
                    num[1] += "0" *(14 -len(num[1]))
                    print(num[0]);print(num[1])
                else: #else man[1] is a single integer
                    man[1] += "2"
                    man[1] += "0" *(14 -len(man[1]))
                    print(man[1])
            elif "M" in g1[0]:
                ma = g1[0].split("M") #splitting by M to get a list
                if "-" in ma[1]: # if there is a range
                    num = ma[1].split("-")
                    num[0] += "2"
                    num[0] += "0" *(14 -len(num[0]))
                    num[1] += "2"
                    num[1] += "0" *(14 -len(num[1]))
                    print(num[0]);print(num[1])
                else: #else there is no range
                    ma[1] += "0" *(14 -len(ma[1]))
                    print(ma[1])
            elif "Hy" in g:
                print("53000000000000")
            else:
                gly = re.split(r'([A-Z][a-z]*\d *)', g1[0])
                translated = ""
                #In every glycan, there's a core composed of  2 hexnac (glucnac) + 3 hexose (mannose)
                G = 3 #Hexose
                AB = 2 #Hexnac
                F = 0 #Deoxyhexose
                S = 0 #NeuAC
                for gls in gly:
                    if "G" in gls:
                        g = gls.split("G")
                        if g[1] == "":
                            G += 1
                        else:
                            G += int(g[1])
                    elif "A" in gls:
                        a = gls.split("A")
                        AB += int(a[1])
                    elif "B" in gls:
                        b = gls.split("B")
                        if b[1] == "":
                            AB += 1
                        else:
                            AB += int(b[1])
                    elif "F" in gls:
                        f = gls.split("F")
                        if f[1] == "":
                            F += 1
                        else:
                            F += int(f[1])
                    elif "S" in gls:
                        s = gls.split("S")
                        S += int(s[1])
                #out of the loop, do the conversion:
                translated += ''.join([str(G), str(AB),str(F), str(S)])
                translated += "0" * (14 -len(translated))
                print(translated)

table.readline()#Skipping the header
for line in table:
    line = line.split(",")
    glycans = ''.join([x for x in line[7] if ord(x) < 128]) #Thanks to: http://snipplr.com/view/57881/
    glycans = glycans.split("; ")
    print(glycans)
    translator(glycans)
