sentence = input("Enter a paragraph: ")

words = sentence.lower().split()

print("\nRepeated Words:")

for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count += 1

    if count > 1 and words[i] not in words[:i]:
        print(words[i], "appears", count, "times")

print("\nTotal Words:", len(words))