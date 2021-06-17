def binary_tree_search(target, num, height):
    """ Models a binary search of the tree. If the target
    equals either viable child node number, returns the number
    of the parent node. Otherwise calls itself on the viable
    child node."""
    if height < 1:
        raise ValueError("Illegal height {}".format(height))
    if target == num - 2**(height - 1) or target == num - 1:
        return num
    elif target < num - 2**(height - 1):
        return binary_tree_search(target, num - 2**(height - 1), height-1)
    else:
        return binary_tree_search(target, num - 1, height - 1)


def solution(h, q):
    """ Given a postorder balanced binary tree of height h, find the parent
     node of each node listed in int[]q. Instead of constructing and then iterating
     over a tree with 2^30 nodes, let's use a binary search to find the answers."""
    output = list()
    for target in q:
        if target == 2**h - 1:
            output.append(-1)
        else:
            output.append(binary_tree_search(target, 2**h - 1, h))
    return output


if __name__ == '__main__':
    x = solution(3, [7, 3, 5, 1])
    y = solution(5, [19, 14, 28])
    print(x)
    print (y)
