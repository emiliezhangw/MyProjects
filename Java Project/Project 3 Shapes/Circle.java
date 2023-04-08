
public class Circle extends Shape implements TwoDShape {

	private int radius;
	
	// Constructor
	public Circle(int radius)
	{
		this.radius = radius;
	}
	// Get radius
	public int getRadius()
	{
		return radius;
	}
	
	// Calculate the area of the circle
	@Override
	public double area() 
	{
		return Math.PI * Math.pow(radius, 2);
	}
	
	// Describe the size of the rectangle
	@Override
	public String toString() 
	{
		return "Circle  Radius: " + radius;
	}
	
	// Describe the circle
	@Override
	public String getDescription()
	{
		return "Circle: A closed plane curve every point of which is equidistant from a fixed point within the curve";
	}
	
	// Calculate the perimeter of this 2D Shape
	@Override
	public double perimeter() 
	{
		return 2 * Math.PI * radius;
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
		Circle circle = (Circle) object;
		return getDescription().equals(circle.getDescription()) && radius == circle.getRadius();
	}
	
}
