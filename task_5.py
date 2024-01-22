def read_words(file_path: str) -> list[list[str]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        result = []
        line = file.readline()
        while line != '':
            result.append(
                [word.strip() for word in line.split(",")]
            )
            line = file.readline()

        return result


def find_combo(words, first_word):
    combinations = []
    for word in words:
        for i in range(len(word), 0, -1):
            if word == first_word:
                break

            t = word[:i]
            if first_word.endswith(t):
                combinations.append(first_word + word[i:])
                break
    return combinations


file_path = 'test.txt'

words: list[list[str]] = read_words(file_path)

first_word = input("Введите первое слово: ")

combinations = []

for words_line in words:
    combinations.extend(
        find_combo(words_line, first_word)
    )

for combo in combinations:
    print(combo)
