import matplotlib.pyplot as plt

# plt.subplot(2, 5, 1)
x_axis_1 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_1 = [0.06312817238, 0.05325700233, 0.04180973118, 0.04822073234]
plt.ylabel('Normalized Topic Contribution')
plt.title('Topic_1')
plt.plot(x_axis_1, y_axis_1, 'b')
plt.plot(x_axis_1, y_axis_1, 'ro')
plt.xticks([], rotation=45)

# plt.subplot(2, 5, 2)
x_axis_2 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_2 = [0.05838851726, 0.04742130885, 0.0474101834, 0.04483754513]
plt.title('Topic_2')
plt.plot(x_axis_2, y_axis_2, 'r')
plt.plot(x_axis_2, y_axis_2, 'ro')
plt.xticks([], rotation=45)

# plt.subplot(2, 5, 3)
x_axis_3 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_3 = [0.04711642968, 0.06944374452, 0.05185914078, 0.05394533265]
plt.title('Topic_3')
plt.plot(x_axis_3, y_axis_3, 'g')
plt.plot(x_axis_3, y_axis_3, 'ro')
plt.xticks([], rotation=45)

# plt.subplot(2, 5, 4)
x_axis_4 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_4 = [0.05287572692, 0.04247256015, 0.04770329118, 0.0495719443]
plt.title('Topic_4')
plt.plot(x_axis_4, y_axis_4, 'y')
plt.plot(x_axis_4, y_axis_4, 'ro')
plt.xticks([], rotation=45)

# plt.subplot(2, 5, 5)
x_axis_5 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_5 = [0.04616401672, 0.03987219932, 0.055365966, 0.04365136668]
plt.title('Topic_5')
plt.plot(x_axis_5, y_axis_5, 'p')
plt.plot(x_axis_5, y_axis_5, 'ro')
plt.xticks([], rotation=45)

# plt.subplot(2, 5, 6)
x_axis_6 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_6 = [0.04868510986, 0.04842920064, 0.0457038774, 0.04969571944]
plt.xlabel('Biodiversity Hotspot')
plt.ylabel('Normalized Topic Contribution')
plt.title('Topic_6')
plt.plot(x_axis_6, y_axis_6, 'o')
plt.plot(x_axis_6, y_axis_6, 'ro')
plt.xticks(x_axis_6, rotation=45)

# plt.subplot(2, 5, 7)
x_axis_7 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_7 = [0.05173283136, 0.05289416128, 0.07030399464, 0.05925734915]
plt.xlabel('Biodiversity Hotspot')
plt.title('Topic_7')
plt.plot(x_axis_7, y_axis_7)
plt.plot(x_axis_7, y_axis_7, 'ro')
plt.xticks(x_axis_7, rotation=45)

# plt.subplot(2, 5, 8)
x_axis_8 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_8 = [0.02924468049, 0.04362155679, 0.04825810234, 0.06096957194]
plt.xlabel('Biodiversity Hotspot')
plt.title('Topic_8')
plt.plot(x_axis_8, y_axis_8)
plt.plot(x_axis_8, y_axis_8, 'ro')
plt.xticks(x_axis_8, rotation=45)

# plt.subplot(2, 5, 9)
x_axis_9 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_9 = [0.0410209867, 0.0414344316, 0.06009756302, 0.04580711707]
plt.xlabel('Biodiversity Hotspot')
plt.title('Topic_9')
plt.plot(x_axis_9, y_axis_9)
plt.plot(x_axis_9, y_axis_9, 'ro')
plt.xticks(x_axis_9, rotation=45)

# plt.subplot(2, 5, 10)
x_axis_10 = ['Master Corpus', 'Eastern Himalayas', 'Melanasian Islands', 'Western Ghats']
y_axis_10 = [0.04509955517, 0.04405495026, 0.02601331547, 0.06841670964]
plt.xlabel('Biodiversity Hotspot')
plt.title('Topic_10')
plt.plot(x_axis_10, y_axis_10)
plt.plot(x_axis_10, y_axis_10, 'ro')
plt.xticks(x_axis_10, rotation=45)

plt.legend()

plt.show()