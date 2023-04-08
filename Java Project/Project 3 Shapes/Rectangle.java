
public class Rectangle extends Shape implements TwoDShape {

	private int width, height;
	
	// Constructor
	public Rectangle(int width, int height)
	{
		this.width = width;
		this.height = height;
	}
	
	// Get width
	public int getWidth()
	{
		return width;
	}
	
	// Get height
	public int getHeight()
	{
		return height;
	}
	
	// Calculate the area of the rectangle
	@Override
	public double area() {
		return width * height;
	}

	// Describe the size of the rectangle
	@Override
	public String toString() 
	{
		return "Rectangle\tWidth: " + width + "\tHeight: " + height;
	}
	
	// Describe the rectangle
	@Override
	public String getDescription()
	{
		return "Rectangle: A quadrilateral with four right angles";
	}
	
	// Calculate the perimeter of this 2D Shape
	@Override
	public double perimeter() {
		return (width + height) * 2;
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
		Rectangle rectangle = (Rectangle) object;
		return getDescription().equals(rectangle.getDescription()) && height == rectangle.getWidth() && width == rectangle.getHeight();
	}
		
}
