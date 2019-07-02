def reshenie(uravnenie):
    int(uravnenie)
    return uravnenie


def print_resh():
    reshenie((10 + 18) * 6)


def find_new(uravnenie, obj):
    massiv = []
    q = -1
    for i in uravnenie:
        q += 1
        if uravnenie[q] == obj:
            massiv.append(q)
            print(massiv)
            continue
    return massiv


def at_first(uravnenie):
    first_massiv = find_new(uravnenie, "(")
    second_massiv = find_new(uravnenie, ")")


def procedure(struravnenie):
    for i in struravnenie:
        if i == ")":
            mark = struravnenie.index(i)
            for j in struravnenie:
                if j == "(":
                    nstr = struravnenie[struravnenie.index(j):struravnenie.index(i)]
                    newstr = nstr.replace("(", "")
                    print(newstr)
                    continue
                    
  #пока только наброски

