import re


def main(src_string):
    group1_dict = re.findall(r'to[ (\n)][^ :>]*', src_string)
    group2_dict = re.findall(r'"[^"]*"', src_string)

    groups_list = list()
    for i in range(0, len(group1_dict)):
        group1_dict[i] = group1_dict[i][3:]
        group2_dict[i] = group2_dict[i][1:-1]
        groups_list.append(
            (group1_dict[i], group2_dict[i])
        )

    return dict(groups_list)
