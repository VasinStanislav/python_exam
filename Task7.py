def main(a):
    str1 = "{0:b}".format(a)
    str1 = (32 - len(str1)) * "0" + str1

    arr = list(str1)

    new_arr = []
    new_arr[0:3] = arr[2:5]
    new_arr[3:10] = arr[12:19]
    new_arr[10:23] = arr[19:]
    new_arr[23:30] = arr[5:12]
    new_arr[30:] = arr[:2]

    str2 = "0b"
    for i in range(0, len(new_arr)):
        str2 += new_arr[i]

    bin_b = bin(int(str2, base=2))
    b = int(bin_b, base=2)

    return b


# print(main(177173126))
print(main(0x8fee2b8d))
# print(main(2414750605))
# 0b111100010101110001101111111010
