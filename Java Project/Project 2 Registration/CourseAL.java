import java.util.ArrayList;

public class CourseAL {
	private String courseName;
	private int max_roster, max_waitlist;
	private ArrayList<Student> roster = new ArrayList<Student>(), waitlist = new ArrayList<Student>();

	//A constructor to initialize the variables
	public CourseAL(String name, int rosternum, int waitlistnum)
	{
		courseName = name;
		max_roster = rosternum;
		max_waitlist = waitlistnum;
	}
	
	public void set_courseName(String name)
	{
		courseName = name;
	}
	
	public String get_courseName()
	{
		return courseName;
	}
	
	public ArrayList<Student> get_roster()
	{
		return roster;
	}
	
	public ArrayList<Student> get_waitlist()
	{
		return waitlist;
	}
	
	public void set_maxroster(int input_maxRoster)
	{
		max_roster = input_maxRoster;
	}
	
	public int get_maxroster()
	{
		return max_roster;
	}
	
	public void set_maxwaitlist(int input_maxWaitlist)
	{
		max_waitlist = input_maxWaitlist;
	}
	
	public int get_maxwaitlist()
	{
		return max_waitlist;
	}
	
	//a toString method to provide the course information and the roster of enrolled students and the students on the waitlist
	public String toString() 
	{
		
		StringBuilder rosterstudent = new StringBuilder();
		StringBuilder waitliststudent = new StringBuilder();
		for (Student student : roster)
		{
			rosterstudent.append("\n        ").append(student);
		}
		
		for (Student student : waitlist)
		{
			waitliststudent.append("\n        ").append(student);
		}
		//waitliststudent.remove(System.getProperty("line.separator"));
		return courseName + "\n" + roster.size() + " enrolled (maximum allowed " + max_roster + ")" + rosterstudent + "\n" + waitlist.size() + 
				" on waitlist (maximum allowed " + max_waitlist + ")" + waitliststudent;
	}
	//decide whether a student can be added
	public boolean addStudent(Student student)
	{
		//if the student has not paid their tuition, already on the roster or on the waitlist, do not add them
		if (!student.isTuitionPaid() || roster.contains(student) || waitlist.contains(student))
		{
			return false;
		}
		
		//if there is room on the roster, add them to the roster
		if(roster.size() < max_roster)
		{
			roster.add(student);
			return true;
		}
		//if the roster is full but there is room on the waitlist, add them to the waitlist
		if(waitlist.size() < max_waitlist)
		{
			waitlist.add(student);
			return true;
		}
		
		return false;
	}
	//decide whether a student can be removed
	public boolean dropStudent(Student student)
	{
		//remove the person if they are on the roster
		if (roster.contains(student))
		{
			roster.remove(student);
			
			//add the first person on the waitlist to the roster if the waitlist is not empty
			if (waitlist.size() > 0)
			{
				roster.add(waitlist.get(0));
				waitlist.remove(0);
			}
			return true;
		}
		//remove the person if they are on the waitlist
		if (waitlist.contains(student))
		{
			waitlist.remove(student);
			return true;
		}
		
		return false;
	}
}
