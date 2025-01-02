from PIL import Image


image = Image.new('RGBA', (600, 600), color='blue')

b = 200
h = 100
q = 150

for i in range(600):
	for j in range(600):
		image.putpixel((i,j), (0,0,0,0))

with open('font_data.txt','r') as f:
	d = f.readlines()

dd = ['']
for l in d:
	t = l.strip()
	if t == '':
		dd.append('')
	else:
		dd[-1] += t


print(len(dd))
print(dd)

pallet = []

pallet.append((h,h,h,255))
pallet.append((q,q,q,255))
pallet.append((b,b,b,255))
pallet.append((b,h,h,255))
pallet.append((b,q,h,255))
pallet.append((b,b,0,255))
pallet.append((0,b,0,255))
pallet.append((0,q,b,255))
pallet.append((q,q,b,255))
pallet.append((b,h,b,255))

for k in range(len(pallet)):
	for i in range(len(dd)):
		for j in range(len(dd[i])):
			# print(i, j)
			xx = 1 + i * 6 + j % 5
			yy = 1 + k * 10 + j // 5
			if dd[i][j] == '#':
				image.putpixel((xx,yy),pallet[k])


image.save('bitmap_font.png')


