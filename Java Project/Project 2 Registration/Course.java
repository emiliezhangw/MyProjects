import java.util.Arrays;

public class Course {
	
	private String courseName;
	private int max_roster, max_waitlist, rosterNum = 0, waitlistNum = 0;
	private Student[] roster, waitlist;

	//A constructor to initialize the variables
	public Course(String name, int input_maxRoster, int input_maxWaitlist)
	{
		courseName = name;
		roster = new Student[input_maxRoster];
		waitlist = new Student[input_maxWaitlist];
		max_roster = input_maxRoster;
		max_waitlist = input_maxWaitlist;
	}
	
	public void set_courseName(String name)
	{
		courseName = name;
	}
	public String get_courseName()
	{
		return courseName;
	}
	public Student[] get_roster()
	{
		return roster;
	}
	public Student[] get_waitlist()
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
		for (int i = 0; i < rosterNum; i++) 
		{ 
			rosterstudent.append("\n        ").append(roster[i]);
		}
		for (int j = 0; j < waitlistNum; j++) 
		{
			waitliststudent.append("\n        ").append(waitlist[j]);
		}
		return courseName + "\n" + rosterNum + " enrolled (maximum allowed " + max_roster + ")" + rosterstudent + "\n" +  waitlistNum + 
				" on waitlist (maximum allowed " + max_waitlist + ")" + waitliststudent;
	}
	//decide whether a student can be added
	public boolean addStudent(Student student)
	{
		//if the student has not paid their tuition, do not add them
		if (!student.isTuitionPaid())
		{
			return false;
		}
		//if the student is already on the roster, do not add them
		for(Student studentExist : roster)
		{
			if (student.equals(studentExist))
			{
				return false;
			}
		}
		//if the student is already on the waitlist, do not add them
		for(Student studentExist : waitlist)
		{
			if (student.equals(studentExist))
			{
				return false;
			}
		}
		//if there is room on the roster, add them to the roster
		if(rosterNum < max_roster)
		{
			roster[rosterNum] = student;
			rosterNum++;
			return true;
		}
		//if the roster is full but there is room on the waitlist, add them to the waitlist
		else if(waitlistNum < max_waitlist)
		{
			waitlist[waitlistNum] = student;
			waitlistNum++;
			return true;
		}
		return false;
	}
	//decide whether a student can be removed
	public boolean dropStudent(Student student)
	{
		//remove the person if they are on the roster
		for(int i = 0; i < rosterNum; i++)
		{
			if (student.equals(roster[i]))
			{
				for (int k = i; k < rosterNum - 1; k++)
				{
					roster[k] = roster[k+1];
				}
				roster[rosterNum - 1] = null;
				//add the first person on the waitlist to the roster if the waitlist is not empty
				if (waitlistNum > 0)
				{
					roster[rosterNum - 1] = waitlist[0];
					for (int j = 0; j < waitlistNum - 1; j++)
					{
						waitlist[j] = waitlist[j+1];
					}
					waitlist[waitlistNum - 1] = null;
					waitlistNum--;
					return true;
				}
				rosterNum--;
				return true;
			}
		}
		//remove the person if they are on the waitlist
		for(int i = 0; i < waitlistNum; i++)
		{
			if (student.equals(waitlist[i]))
			{
				for (int k = i; k < waitlistNum - 1; k++)
				{
					waitlist[k] = waitlist[k+1];
				}
				waitlist[waitlistNum - 1] = null;
				waitlistNum--;
				return true;
			}
		}
		return false;
	}
}
