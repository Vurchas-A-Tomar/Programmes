def papersize(i, num, len, wid):
    if num != 0:
        print(f'A{i} => L = {int(len)} B = {int(wid)}') 
        n_wid = len / 2
        n_len = wid
        i += 1
        num -= 1

        papersize(i, num, n_len, n_wid)

papersize(0, 7, 1189, 841)