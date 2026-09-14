input = 'Nadiya'
vowels = ['a', 'i', 'o', 'e', 'u']
l_input = input.lower()
num_vowels = 0
for c in l_input:
    if c in vowels:
        num_vowels += 1

print(f"Num vowels: {num_vowels}")