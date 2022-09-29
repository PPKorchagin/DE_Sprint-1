x1 = "1011101"
x2 = "1101111"

x1int = [int(i) for i in x1]
x2int = [int(i) for i in x2]
x1r = x1int[::-1]
x2r = x2int[::-1]

buf_r = [0] * (len(x1) * len(x2))

for idx in range(len(x2r)):
    x2ch = x2r[idx]
    #print(f"will multiply {x1} to {x2ch}^{idx}:")
    reg = 0
    if x2ch == 1:
        el1 = x1int.copy()
        el1.extend([0] * idx)
        #print(f"will sum {buf_r} and {el1[::-1]}")
        el1r = el1[::-1]
        for eidx in range(len(el1r)):
            #print(f'{el1r[eidx]} + {buf_r[eidx]}: {int(el1r[eidx]) + int(buf_r[eidx])}')
            if int(el1r[eidx]) + int(buf_r[eidx]) != 2:
                buf_r[eidx] += int(el1r[eidx])
            else:
                fl_index = True
                buf_r[eidx] = 0
                for ri in range(eidx + 1, len(buf_r) - 1):
                    #print(f'processs idx {ri}: {buf_r[ri + 1]} + 1, flag {fl_index} ')
                    if fl_index:
                        if buf_r[ri] == 1:
                            buf_r[ri] = 0
                        else:
                            buf_r[ri] = 1
                            fl_index = False
                if fl_index:
                    buf_r[ri+1]=1

        #print("tmp", buf_r)

#print(buf_r[::-1])

b_str = ""
for b in buf_r[::-1]:
    if b == 1 or len(b_str) != 0:
        b_str += str(b)

print(b_str)
