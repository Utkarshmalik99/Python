listNumbers = [20, 22, 24, 26, 28, 28, 20, 30, 24]
print("Original= ", listNumbers)

listNumbers = list(set(listNumbers))
print("After removing duplicate= ", listNumbers)

#Output-
#Original=  [20, 22, 24, 26, 28, 28, 20, 30, 24]
#After removing duplicate=  [20, 22, 24, 26, 28, 30]
