import java.util.HashMap;


public enum TileType {

	GROUND     (0xFFFFFFFF, '.'), // White
	OUTOFBOUND (0xFFFF0000, '@'), // Red
	SWAMP      (0xFF000000, 'S'), // Black
	TREE       (0xFF00FF00, 'T'), // Green
	WATER      (0xFF0000FF, 'W'); // Blue

	private final static HashMap<Integer, TileType> tileTypeByColor;

	static {
		tileTypeByColor = new HashMap<Integer, TileType>();
		for (TileType t : TileType.values()) {
			tileTypeByColor.put(t.getColor(), t);
		}
	}

	private int color;
	private char symbol;

	public static TileType forColor(int color) {
		return tileTypeByColor.get(color);
	}

	public int getColor() {
		return this.color;
	}

	public char getSymbol() {
		return this.symbol;
	}

	TileType(int color, char symbol) {
		this.color = color;
		this.symbol = symbol;
	}
}
