def average_agreement(list1, list2, max_depth):

    # NEW CODE
    # Empty lists evaluate to false.
    if (not list1) or (not list2):
        return 0.0

    # NEW CODE
    # Truncate the depth
    max_list_len = max(len(list1), len(list2))
    max_depth = min(max_depth, max_list_len)

    agreements = []

    for depth in range(1, max_depth + 1):
        set1 = set(list1[:depth])
        set2 = set(list2[:depth])

        intersection = set1 & set2

        agreements.append(2 * len(intersection) / (len(set1) + len(set2)))

    return sum(agreements) / len(agreements)
