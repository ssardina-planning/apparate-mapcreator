import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;

import javax.imageio.ImageIO;


public class ApparateMapCreator {

	private final static String DEFAULT_TYPE = "octile";

	public static void main (String[] args) {
		if (args.length < 2) {
			System.out.println("Usage: java ApparateMapCreator <input.bmp> <output.map>");
		}

		String imageFileName = args[0];
		String outFileName = args[1];

		try {

			BufferedImage image = ImageIO.read(new File(imageFileName));
			PrintWriter out = new PrintWriter(outFileName);

			System.out.println("Generating map...");
			generateMap(image, out);
			out.close();
			System.out.println("...Done.");

			System.out.println("Created file '" + outFileName + "'.");

		} catch (IOException e) {
			System.err.println("Error whilst reading file '" + imageFileName +"'.");
			System.err.println(e);
		}
	}

	private static void generateMap(BufferedImage image, PrintWriter out) {
		int width = image.getWidth();
		int height = image.getHeight();

		// Add map type
		out.println("type " + DEFAULT_TYPE);

		// Add map dimensions
		out.println("width " + width);
		out.println("height " + height);

		// Add movement costs TODO: allow customization
		out.println("ground 1");
		out.println("tree +inf");
		out.println("swamp 10");
		out.println("water 20");

		// Add map
		out.println("map");

		// Create tile string
		StringBuilder sb = new StringBuilder();
		for (int y = 0; y < height; y++) {
			for (int x = 0; x < height; x++) {
				int color = image.getRGB(x, y);
				TileType tileType = TileType.forColor(color);
				char symbol;
				if (tileType == null) {
					System.out.println("Pixel color at [" + x + ',' + y +
							"] is not associated with a tile type.");
					symbol = '?';
				} else {
					symbol = tileType.getSymbol();
				}
				sb.append(symbol);
			}
			sb.append('\n');
		}
		// Add tiles to file
		out.print(sb);
	}
}
