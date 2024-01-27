l1 = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
l2 = [('a', 'c'), ('d', 'a')]
l3 = [] 

# if len(l1) == 0:
#     l3.append(l2[0])
# else:
#     for pair in l1:
#         skip_pair = False
#         for p_pair in l2:
#             if pair[0] in p_pair or pair[1] in p_pair:
#                 skip_pair = True
#                 break
#         if not skip_pair:
#             l3.append(pair)



if len(l1) == 0:
    l3.append(l2[0])
else:
    for pair in l1:
        skip_pair = False
        for p_pair in l2:
            if pair[0] in p_pair or pair[1] in p_pair:
                skip_pair = True
                break
        if not skip_pair:
            l3.append(pair)