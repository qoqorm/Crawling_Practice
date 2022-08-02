f = open("files.txt", "w")

# open(A, B)
# A : 경로를 포함한 파일 이름
# B : 권한

# 절대경로 : 드라이브부터로의 경로(윈도우)
# c:\sdf\sdf\

# 상대경로 : 현재 경로로부터의 경로(코드 연 곳)

# f = open("test1/a.txt", "w")
# f = open("test1/test2/b.png", "w")
# f = open("test1/test2/test3/c.py", "w")

f = open("test1/a.txt", "w")
f.write("hello world")