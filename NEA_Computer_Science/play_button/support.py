import pygame
from csv import reader
from os import walk

def import_csv_layout(path):
	terrain_map = []
	with open(path) as level_map:
		# delimiter is what seperates each individual entry in the file 
		layout = reader(level_map, delimiter = ",")
		#print(layout)
		for row in layout:
			#print(row)
			terrain_map.append(list(row))
		return terrain_map

# goes through the file, gets the file + name of each file, then adds that onto the full path to complete the path
def import_folder(path):
	# so that using \ it doesnt come up as an error in line 27
	a = r'\a'
	a = a[:-1]
	surface_list = []

	# underscores as we dont want them, we only want the image files
	for _,__,img_files in walk(path):
		for image in img_files:
			#print(image)
			full_path = path + a + image
			#print(full_path)
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)
	return surface_list


#print(import_csv_layout(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\Tiled_csv_files\MAP_FOR_NEA._FloorBlocks.csv"))		
#import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\grass")
 