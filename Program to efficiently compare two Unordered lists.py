from collections import Counter

one = [33, 22, 11, 44,55]
two = [22, 11, 44, 55,33]

print("Are two list equal?",Counter(one) == Counter(two))

#Output-Are two list equal? True
