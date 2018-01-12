#!/usr/bin/python
import sys, os
from PIL import Image

class Map :

	def __init__( self, infile, mappings, output ) :
		self.__load_bitmap( infile )
		self.types = { 'ground' : '.', 'swamp' : 'S', 'tree' : 'T', 'water' : 'W', 'out_of_bounds' : '@' } 
		self.costs = dict( [ (name, 0) for name in self.types.keys() ] )
		self.color_table = dict()
		self.map_lines = []
		self.__load_rgb_mapping( mappings )
		self.filename = output

	def __load_bitmap( self, img_file ) :
		print >> sys.stdout, "Loading", img_file
		self.img = Image.open( img_file )
		print >> sys.stdout, self.img.getpixel( (82,85) )

	def __load_rgb_mapping( self, def_file ) :
		print >> sys.stdout, "Loading", def_file
		with open( def_file ) as instream :
			for line in instream :
				line = line.strip()
				if line[0] == ';' : continue
				rgb_tok, typename, cost = line.split(' ')
				print rgb_tok
				r, g, b = rgb_tok.split(',')
				color = ( int(r), int(g), int(b) )
				self.color_table[ color ] = self.types[typename]
				self.costs[typename] = cost
				
	def __decode_image(self) :
		w, h = self.img.size
		for y in range(0,h) :
			self.map_lines.append( ['']*w )
			for x in range(0,w) :
				rgb = tuple( list( self.img.getpixel( (x,y) )[0:3]) )
				try :
					self.map_lines[-1][x] = self.color_table[ rgb ]
				except KeyError :
					# MRJ: If the color hasn't been specified, then 
					# cell becomes out of bounds
					self.map_lines[-1][x] = '@'	
	def write_to_disk( self ) :
		print >> sys.stdout, "Writing map into file", self.filename
		self.__decode_image()
		with open( self.filename, 'w' ) as outstream :
			# Write map header
			print >> outstream, "type octile"
			w, h = self.img.size
			print >> outstream, "height", h
			print >> outstream, "width", w
			print >> outstream, "map"
			for cell_type in ['ground', 'tree', 'swamp', 'water' ] :
				print >> outstream, cell_type, self.costs[cell_type]
			for line in self.map_lines :
				print >> outstream, ''.join(line)

def process_args() :
	img_file, map_file, out_file = None, None, None

	if len(sys.argv) < 4 :
		print >> sys.stderr, "Missing program parameters!"
		print >> sys.stderr, "Usage: python img2map <image file> <mappings file> <output map>"
		print >> sys.stderr, "Bailing out!"
		sys.exit(1)

	img_file = sys.argv[1]
	if not os.path.exists( img_file ) :
		print >> sys.stderr, "Cannot find image file:", sys.argv[1]
		sys.exit(1)

	map_file = sys.argv[2]
	if not os.path.exists( map_file ) :
		print >> sys.stderr, "Cannot find file specifying RGB to cell type mapping:", map_file
		sys.exit(1)

	out_file = sys.argv[3]
	if os.path.exists( out_file ) :
		print >> sys.stdout, "WARNING! Overwriting file:", out_file

	return img_file, map_file, out_file

def main() :

	infile, mappings, outfile = process_args()

	m = Map( infile, mappings, outfile )
	m.write_to_disk()

if __name__ == '__main__' :
	main()
