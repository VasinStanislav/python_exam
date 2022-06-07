import re


def main(src):
    group1 = re.findall(r'\|>[ ]?[a-zA-Z_0-9]+', src)
    group2 = re.findall(r'make #\([ #\-0-9;]+\)', src)

    group = list()
    for i in range(0, len(group1)):
        el1 = re.search(r'[a-zA-Z_0-9]+', group1[i]).group(0)
        el2 = re.findall(r'[\-]?[0-9]+', group2[i])
        el2_int = list()
        for j in range(0, len(el2)):
            el2_int.append(int(el2[j]))
        group.append((el1, el2_int))
    return dict(group)


print(main('do (( make #( #1625 ; #5859 ;#1922 ; #1080 ) |> veza_194)). ((make #('
           '#-4101 ; #-9094) |> xece_826)). (( make #( #-2741 ; #-6868)'
           '|>esbi_886)). done'))
