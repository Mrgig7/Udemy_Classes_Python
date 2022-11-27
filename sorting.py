pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)  # new list is created
print(sorted_numbers)
print(numbers)

numbers.sort()  # the existing list is sorted
print(numbers)

another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)  # None

missing_letter = sorted("The quick brown fox jumped over a lazy dog")
print(missing_letter)

missing_letter = sorted("The quick brown fox jumped over a lazy dog",
                        key=str.casefold)
print(missing_letter)

name = ["Graham",
        "John",
        "terry",
        "eric",
        "Terry",
        "michael"
        ]
name.sort(key=str.casefold)
print(name)