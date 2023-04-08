
public class Square extends Rectangle implements TwoDShape {
	private int sideLength;
	
	// Constructor
	public Square(int sideLength) {
		super(sideLength, sideLength);
		this.sideLength = sideLength;
	}
	// Get sideLength
	public int getSideLength()
	{
		return sideLength;
	}
	
	// describe the size of the square
	@Override
	public String toString() 
	{
		return "Square  Side Length: " + sideLength;
	}
	
	// Describe the square
	@Override
	public String getDescription()
	{
		return super.getDescription() + "\nSquare: A quadrilateral with four equal sides and four equal angles";
	}

	// Calculate the perimeter of this 2D Shape
	@Override
	public double perimeter() {
		return sideLength * 4;
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
		Square square = (Square) object;
		return getDescription().equals(square.getDescription()) && sideLength == square.getSideLength();
	}

}
