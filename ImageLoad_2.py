import matplotlib.pyplot as plt
import os


def main():
	img_path = '/home/miju/Image_With_Python/Favorite.jpg'
	if(os.path.exists(img_path)): #image is exist or not checking
		#Load an RGB image.
		img_set, title_set = prepare_img(img_path)
		
		#Display different kinds of images.
		plot_img(img_set, title_set)
		
	else:
		print('{} is not valid.'.format(img_path))
		
		
def prepare_img(img_path):
		#Load an RGB image.
		print(img_path)
		rgb = plt.imread(img_path)
		print(rgb.shape)
		
		#Split loaded RGB image int red, green, blue channel
		red = rgb[:, :, 0]
		print(red[:5, :5])
		green = rgb[:, :, 1]
		print(green[:5, :5])
		blue = rgb[:, :, 2]
		print(blue[:5, :5])
		
		#Put images and titles into lists for convenience.
		img_set = [rgb, red, green, blue]
		title_set = ['RGB', 'Red', 'Green', 'Blue']
		
		return img_set, title_set
		
def plot_img(img_set, title_set):
		plt.figure(figsize = (20, 20))
		for i in range(4):
			plt.subplot(2, 2, i + 1)
			plt.title(title_set[i])
			img = img_set[i]
			ch = len(img.shape)
			if(ch==2):
				plt.imshow(img, cmap = 'gray')
			else:
				plt.imshow(img)
				
		plt.show()

if __name__ == '__main__':
	main()
