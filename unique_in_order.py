"""
    This function, named unique_in_order, takes a sequence (such as a string or a list)
    and returns a new sequence containing only unique and consecutive elements
    from the original sequence, preserving their order.
"""
def unique_in_order(sequence):
    new_array = []

    for item in sequence:
        if not new_array or item != new_array[-1]:
            new_array.append(item)

    return new_array