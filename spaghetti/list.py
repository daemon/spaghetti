import random


def split(lst, size):
    for idx in range(0, len(lst), size):
        yield lst[idx:idx + size]


def unfolded(obj):
    if not isinstance(obj, list):
        return [obj]
    unfolded_list = []
    for x in obj:
        unfolded_list.extend(unfold(x))
    return unfolded_list


def stripify(*lists):
    next_iters = list(map(iter, lists))
    while next_iters:
        for next_iter in next_iters:
            try:
                yield next(next_iter)
            except:
                next_iters.remove(next_iter)


def striped(indices, *lists):
    return [l[idx] for l, idx in zip(lists, indices)]


def cross(*lists, randomize=False):
    def increment():
        for idx, index in reversed(list(enumerate(indices))):
            if index < len(lists[idx]) - 1:
                indices[idx] += 1
                return True
            else:
                indices[idx] = 0
        return False

    if randomize:
        random_map = [list(range(len(x))) for x in lists]
        list(map(random.shuffle, random_map))

    if len(lists) == 0:
        raise StopIteration
    indices = [0] * len(lists)
    while True:
        yield striped([r[x] for r, x in zip(random_map, indices)] if randomize else indices, *lists)
        if not increment(): break

