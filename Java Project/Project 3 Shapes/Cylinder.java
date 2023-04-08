
public class Cylinder extends Shape implements ThreeDShape{
	
	private int radius, height;
	
	// Constructor
	public Cylinder(int radius, int height)
	{
		this.radius = radius;
		this.height = height;
	}
	
	// Get radius
	public int getRadius()
	{
		return radius;
	}
	// Get height
	public int getHeight()
	{
		return height;
	}
	
	// Calculate the surface area of the cylinder
	@Override
	public double area() 
	{
		return 2 * Math.PI * Math.pow(radius, 2) + 2 * Math.PI * radius * height;
	}
	
	// Describe the size of the cylinder
	@Override
	public String toString() 
	{
		return "Cynlinder\tRadius: " + radius + "\tHeight: " + height;
	}
	
	// Describe the cylinder
	@Override
	public String getDescription()
	{
		return "Cylinder: A solid geometric figure with straight parallel sides and a circular or oval cross section";
	}
	
	// Calculate the volume of this 3D Shape
	@Override
	public double volume() {
		return Math.PI * Math.pow(radius, 2) * height;
	}

	// Decide whether two objects are equal
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
		Cylinder cylinder = (Cylinder) object;
		return getDescription().equals(cylinder.getDescription()) && radius == cylinder.getRadius() && height == cylinder.getHeight();
	}
	
	// Decide whether a circle is a top/bottom of a cylinder
	public boolean isTopOrBottom(Circle circle)
	{
		Circle thisCircle = new Circle(radius);
		return thisCircle.equals(circle);
		
	}
}
