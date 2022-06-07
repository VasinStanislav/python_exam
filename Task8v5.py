import re


def main(src):
    group1 = re.findall(r'@"[a-zA-Z_0-9]+"', src)
    group2 = re.findall(r'#\([a-zA-Z_0-9 .]+\)', src)

    group = list()
    for i in range(0, len(group1)):
        el1 = group1[i][2:-1]
        el2 = re.findall(r'[a-zA-Z_0-9]+', group2[i])
        group.append((el1, el2))
    return dict(group)


print(main('<: <: glob #(ange . ongeon_967 . raered_762 ) -> @"soaner".:> <:glob#('
           'anzaat_623 . isus_938 . madi_608 ) -> @"geries_500". :> :>'))
