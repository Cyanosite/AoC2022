score = [[4,1,7],[8,5,2],[3,9,6]]
print(sum([score[ord(item[2])-ord('X')][ord(item[0])-ord('A')] for item in open("2/input.txt", "r").read().split("\n")]))
