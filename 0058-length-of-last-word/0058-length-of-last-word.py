class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        while word_list[-1] == "":
            word_list.pop(-1)
        print(word_list[-1])
        print(word_list)
        return len(word_list[-1])
        