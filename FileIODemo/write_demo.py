# Manual Steps to write to a file
# 1. Open notepad and create file
# 2. Write in the file
# 3. Close the file
#
# Mode
# Read Mode: r
# Write mode: w
# Append mode: a
# Read/write: r+

# f = open("D:\\test date.txt", "w")
# f.write("this is first line")
# f.close()

f = open("D:\\test date.txt", "a")
l = [65,78,989,877,8789]
for items in l:
    f.write(str(items)+"\n")
f.close()
