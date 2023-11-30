from PIL import Image

def ImageToStr(filename, minimum_luminance = 128, foreground_char = '#', background_char = ' ', line_separator = "\n"):
	with Image.open(filename) as im:
		im.load()

		da = list(im.getdata()) # data
		dp = 0 # data pointer
		re = "" # return value

		for y in range(im.height):
			for x in range(im.width):
				re += (foreground_char if (sum(da[dp])/3) >= minimum_luminance else background_char) # '#' if pixel above minimum luminance, ' ' otherwise
				dp += 1 # increment data pointer (get next pixel next iteration)
			re += line_separator # next line hit
	return re

if __name__ == "__main__":
	print(ImageToStr(input("Enter the file path of your image\n>")), end="")
