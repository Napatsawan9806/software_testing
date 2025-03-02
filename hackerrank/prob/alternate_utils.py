from itertools import combinations


def is_alternating(s):
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))


def alternate(s):
    unique_chars = set(s)
    max_length = 0
    for a, b in combinations(unique_chars, 2):
        filtered = [ch for ch in s if ch in (a, b)]
        if is_alternating(filtered):
            max_length = max(max_length, len(filtered))

    return max_length
