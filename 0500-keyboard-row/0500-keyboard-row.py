class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        lst = []

        for i in words:
            word = i.lower()

            count1 = 0
            count2 = 0
            count3 = 0

            for ch in word:
                if ch in "qwertyuiop":
                    count1 += 1

                if ch in "asdfghjkl":
                    count2 += 1

                if ch in "zxcvbnm":
                    count3 += 1

            if count1 == len(word) or count2 == len(word) or count3 == len(word):
                lst.append(i)

        return lst