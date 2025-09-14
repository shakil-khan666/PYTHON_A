def vowel_positions_only(s):
    vowels = "aeiouAEIOU"
    return [i for i, ch in enumerate(s) if ch in vowels]

# টেস্ট করো
text = "Hello World"
result = vowel_positions_only(text)
print("Only vowel positions:", result)

