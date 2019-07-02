
import math

class Q():

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
                continue
        return massiv

    def at_first(uravnenie):
        first_massiv = find_new(uravnenie, "(")
        second_massiv = find_new(uravnenie, ")")
        new_massiv = []
        new_strs = []

        for a in range(0, len(first_massiv)):
            for i in range(0, len(second_massiv)):
                new_massiv.append(math.fabs(first_massiv(a) - second_massiv(i)))
            minimal = min(new_massiv)

            for j in range(0, len(second_massiv)):
                if math.fabs(first_massiv(a) - second_massiv(j)) == minimal:
                    new_str = uravnenie[second_massiv(a):first_massiv(j)]
                    new_strs.append(new_str)

        return new_strs

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

    print(at_first('1 + 2 * (6 + 1) + (6 - 1)'))
