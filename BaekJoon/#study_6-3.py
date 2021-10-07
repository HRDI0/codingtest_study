#study_6-3
word = input()
count_list = []
ascii_word = []
for i in range(26):
    count_list.append(-1)
for i in range(len(word)):
    if count_list[ord(word[i]) % 97] == -1:
        count_list[ord(word[i]) % 97] = i
for i in range(len(count_list)):
    print(count_list[i],end=' ')