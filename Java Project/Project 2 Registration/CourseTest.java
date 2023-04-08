import java.util.Scanner;

public class CourseTest 
{
	static Scanner scan = new Scanner(System.in);
	static String first_name;
	static String last_name;
	static String id;
	static boolean tuitionPaid;
	static Student student;
	
	//prompt user for an option
	public static int menu()
	{
		System.out.println("\nWhat action would you like to take?");
		System.out.println("1 to add a student");
		System.out.println("2 to drop a student");
		System.out.println("3 to print the course");
		System.out.println("4 to exit");
		int input = scan.nextInt();
		return input;
	}
	
	//prompt user for a new student, include first name, last name, id name and tuitionPaid
	public static Student new_student()
	{
		System.out.println("Enter the first name:");
		first_name = scan.next();
		
		System.out.println("Enter the last name:");
		last_name = scan.next();
		
		System.out.println("Enter the id name:");
		id = scan.next();
		
		//prompt user for the tuitionPaid
		System.out.println("Has the student paid tuition? Enter y or n:");
		char answer = scan.next().charAt(0);
		
		if (Character.toLowerCase(answer) == 'y')
		{
			tuitionPaid = true;
		}
		else
		{
			tuitionPaid = false;
		}
		
		student = new Student(first_name, last_name, id, tuitionPaid);
		return student;
	}
	
	//according to user's option, add a student, drop a student or print the course information for them
	public static void main(String[] args)
	{
		Course course = new Course("Introduction to Java", 2, 2);
		System.out.print(course + "\n");
		
		int input;
		do
		{
			//prompt user for option
			input = menu();
			switch(input) 
			{
				case 1:
					new_student();
					//boolean added = course.addStudent(student);
					System.out.println(student + (course.addStudent(student) ? " added successfully" : " not added"));
					break;
				case 2:
					new_student();
					System.out.println(student + (course.dropStudent(student) ? " dropped successfully" : " not dropped"));
					break;
				case 3:
					System.out.print(course);
				default:
					break;
			}
		}
		while (input != 4);
		
		//print the goodbye messages and the course information
		System.out.println("Thank you for using the system.");
		System.out.print(course);
		return;
	}
}
