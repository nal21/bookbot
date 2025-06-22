def count_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}

    for character in text:
        char = character.lower()
        if char in character_counts.keys():
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def sort_on_counts(entry):
    return entry["num"]

def sort_characters(characters):
    sorted_characters = []
    for char in characters:
        sorted_characters.append({
            "char": char,
            "num": characters[char]
        })

    sorted_characters.sort(reverse=True, key=sort_on_counts)
    return sorted_characters