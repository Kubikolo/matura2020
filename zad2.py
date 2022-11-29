def get_best_streak(s):
    best_streak = 1
    best_char = s[0]
    current_streak = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > best_streak:
            best_char = s[i]
            best_streak = current_streak

    return best_char, best_streak


file_path = r"./Dane_PR2/pary.txt"
with open(file_path, "r") as f:
    raw_data = f.readlines()

strings = [x.split(" ")[1][:-1] for x in raw_data]

for s in strings:
    char, streak = get_best_streak(s)
    print(char * streak, streak)