import java.util.*;

public class ShapeTester {

	public static void main(String[] args) {

		Rectangle rectangle1 = new Rectangle(3,4);
		Rectangle rectangle2 = new Rectangle(4,3);
		Rectangle rectangle3 = new Rectangle(5,6);
		Square square1 = new Square(2);
		Square square2 = new Square(4);
		Square square3 = new Square(4);
		Circle circle1 = new Circle(3);
		Circle circle2 = new Circle(5);
		Cylinder cylinder1 = new Cylinder(3, 5);
		Cylinder cylinder2 = new Cylinder(4, 6);
		Cylinder cylinder3 = new Cylinder(6, 4);
		Cube cube1 = new Cube(2);
		Cube cube2 = new Cube(3);
		
		List<Shape> shapeList = new ArrayList<>();
		shapeList.add(rectangle1);
		shapeList.add(rectangle2);
		shapeList.add(rectangle3);
		shapeList.add(square1);
		shapeList.add(square2);
		shapeList.add(square3);
		shapeList.add(circle1);
		shapeList.add(circle2);
		shapeList.add(cylinder1);
		shapeList.add(cylinder2);
		shapeList.add(cylinder3);
		shapeList.add(cube1);
		shapeList.add(cube2);

		System.out.println("*****PRINTING OUT THE TEXT REPRESENTATION, DESCRIPTION, AREA, AND PERIMETER/VOLUME OF EACH SHAPE");
		for(Shape shape : shapeList) {
			System.out.println(shape);
			System.out.println(shape.getDescription());
			System.out.println("\tArea: " + shape.area());
			
			// CODE MISSING: PRINT THE PERIMETER OF TWO-DIMENSIONAL SHAPES
			if (shape instanceof TwoDShape)
			{
				System.out.println("\tPerimeter: " + ((TwoDShape) shape).perimeter());
			}
			// CODE MISSING: PRINT THE VOLUME OF THREE-DIMENSIONAL SHAPES
			else if (shape instanceof ThreeDShape)
			{
				System.out.println("\tVolume: " + ((ThreeDShape) shape).volume());
			}
			System.out.println("");
		}

		System.out.println("\n*****PRINTING ALL EQUAL, NON-ALIAS SHAPES");
		for(Shape firstShape : shapeList) {
			for(Shape secondShape : shapeList) {
				// CODE MISSING: TEST IF THE TWO SHAPES ARE EQUAL (BUT NOT ALIASES!) PRINT THE SHAPES
				if (firstShape.equals(secondShape) && firstShape != secondShape)
				{
					System.out.println("Equal shapes found:");
					System.out.println("\t" + firstShape);
					System.out.println("\t" + secondShape + "\n");
				}
			}
		}

		System.out.println("\n*****PRINTING ALL CYLINDER/CIRCLE COMBINATIONS WHERE THE CIRCLE IS A TOP/BOTTOM OF THE CYLINDER");
		for(Shape firstShape : shapeList) {
			for(Shape secondShape : shapeList) {
				// CODE MISSING: TEST THE isTopOrBottom METHOD FOR CYLINDER/CIRCLE COMBINATIONS. PRINT ANY MATCHES FOUND.
				if (firstShape instanceof Circle && secondShape instanceof Cylinder)
				{
					if (((Cylinder)secondShape).isTopOrBottom((Circle)firstShape))
					{
						System.out.println("Circle-Cylinder Match Found:");
						System.out.println("\t" + firstShape);
						System.out.println("\t" + secondShape + "\n");
					}
				}
			}
		}
		
		System.out.println("\n*****PRINTING ALL CUBE/SQUARE COMBINATIONS WHERE THE SQUARE IS A SIDE FOR THE CUBE");
		for(Shape firstShape : shapeList) {
			for(Shape secondShape : shapeList) {
				// CODE MISSING: TEST THE isOneSide METHOD FOR SQUARE/CUBE COMBINATIONS. PRINT ANY MATCHES FOUND.
				if (firstShape instanceof Square && secondShape instanceof Cube)
				{
					if (((Cube)secondShape).isOneSide((Square)firstShape))
					{
						System.out.println("Square-Cube Match Found:");
						System.out.println("\t" + firstShape);
						System.out.println("\t" + secondShape + "\n");
					}
				}
			}
		}

		System.out.println("\n*****PRINTING ALL COMBINATIONS OF TWO-DIMENSIONAL SHAPES THAT CAN FIT INSIDE ANOTHER");
		for(Shape firstShape : shapeList) {
			for(Shape secondShape : shapeList) {
				// EXTRA CREDIT: TEST THE canFitInside METHOD FOR PAIRS OF TWO DIMENSIONAL SHAPES. PRINT ANY SHAPES THAT NEST.
				if (firstShape instanceof TwoDShape && secondShape instanceof TwoDShape && firstShape != secondShape)
				{
					if (((TwoDShape) secondShape).perimeterCanFitInside((TwoDShape) firstShape))
					{
						System.out.println("Nested Shapes Found:");
						System.out.println("\t Outer: " + firstShape);
						System.out.println("\t Inner: " + secondShape + "\n");
					}
				}
			}
		}		
	}
}
