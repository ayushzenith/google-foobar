def solution(s):
     sol = 0
     length = len(s)
     sequence = ""
     for index in range(0, len(s)):
         sequence = sequence + s[index]
         if sequence * (len(s)/len(sequence)) == s:
             return len(s)/len(sequence)
