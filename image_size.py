from PIL import Image

img = Image.open("gallery/건계정 .png")
크기 = img.size # x, y 크기 튜플 (1000, 633)
img = img.resize((1000, 1000)) # x, y 크기 조절
img.show()

img.save("확대한석실.png")



# -3시간부터 보기