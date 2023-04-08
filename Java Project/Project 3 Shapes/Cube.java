
public class Cube extends Shape implements ThreeDShape{

	private int sideLength;
	
	// Constructor
	public Cube(int sideLength)
	{
		this.sideLength = sideLength;
	}
	
	// Get sideLength
	public int getSideLength()
	{
		return sideLength;
	}
	
	// Calculate the surface area of the cube
	@Override
	public double area() 
	{
		return 6 * Math.pow(sideLength, 2) ;
	}
	
	// Describe the size of the cube
	@Override
	public String toString() 
	{
		return "Cube    Side Length: " + sideLength;
	}
	
	// Describe the cube
	@Override
	public String getDescription()
	{
		return "Cube: A three-dimensional solid object bounded by six square faces with three meeting at each vertex";
	}
	
	// Calculate the volume of this 3D Shape
	@Override
	public double volume() {
		return Math.pow(sideLength, 3);
	}
	
	// decide whether two objects are equal
	public boolean equals(Object object)
	{
		if (this == object)
		{
			return true;
		}
		if (object == null || getClass() != object.getClass())
		{
			return false;
		}
		Cube cube = (Cube) object;
		return getDescription().equals(cube.getDescription()) && sideLength == cube.getSideLength();
	}
	
	// Decide whether a square is one side of a cube
	public boolean isOneSide(Square square)
	{
		Square thisSquare = new Square(sideLength);
		return thisSquare.equals(square);
		
	}
}
