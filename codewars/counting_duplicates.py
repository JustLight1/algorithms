# def duplicate_count(text):
#     char_count = {}
#     for char in text.lower():
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     count = 0
#     for i in char_count.values():
#         if i > 1:
#             count += 1
#     return count

def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    print(count)


duplicate_count('Indivisibilities')
