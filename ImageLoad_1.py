import matplotlib.pyplot as plt
import os

def main():
	img_path = '/home/miju/Image_With_Python/Favorite.jpg'
	if(os.path.exists(img.path)):
		#Load an RGB image.
		print(img_path)
		rgb = plt.imread(img_path)
		print(rgb.shape)
		
		#Split loaded RGB image into red, green and blue channel
		red = rgb[:, :, 0]
		print(red[:5, :5])
		green = green[:, :, 1]
		print(red[:5, :5])
		blue = rgb[:, :, 2]
		print(blue[:5, :5])
		
		#Display different kinds of images.
		plt.figure(figsize = (20, 20))
		
		plt.subplot(2,2,1)
		plt.title('RGB')
		plt.imshow(rgb)
		
		plt.subplot(2,2,2)
		plt.title('RGB')
		plt.imshow(rgb, cmap = 'gray')
		
		plt.subplot(2,2,3)
		plt.title('RGB')
		plt.imshow(rgb, cmap = 'gray')
		
		plt.subplot(2,2,4)
		plt.title('RGB')
		plt.imshow(rgb, cmap = 'gray')
		
		plt.show()
		
	else:
		print('{} is not valid.'.format(img_path))
		
if __name__ == '__main__':
	main()
