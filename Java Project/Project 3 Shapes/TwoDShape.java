
public interface TwoDShape {
	public double perimeter();
	
	public default boolean perimeterCanFitInside(TwoDShape first)
	{
		return this.perimeter() < first.perimeter();
	}
}
