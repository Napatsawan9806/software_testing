def funnyString(s):
    ordinals = [ord(c) for c in s]
    reverse_ordinals = ordinals[::-1]

    diffs = [abs(ordinals[i] - ordinals[i - 1]) for i in range(1, len(ordinals))]
    reverse_diffs = [
        abs(reverse_ordinals[i] - reverse_ordinals[i - 1])
        for i in range(1, len(reverse_ordinals))
    ]

    return "Funny" if diffs == reverse_diffs else "Not Funny"
