import java.util.Random;
import java.util.Scanner;

public class Battleship {
	
	private static final int n = 51;
	private static int ship[] = {2, 3, 5};
	private static int locations[];
	private static char userLocations[] = new char[n];
	
	//print welcome message on the screen
	public static void welcome()
	{
		System.out.println("Welcome to Battleship!");
		
		//tell user about rule of the game
		System.out.printf("The sizes of the ships are : [%d, %d, %d]\n", ship[0], ship[1], ship[2]);
		System.out.printf("Enter a number to fire at the ship. You only get 10 misses!\n");
	}
	
	//print the original array of locations of ships and the result array of the users
	public static void shotInfo() 
	{
		System.out.println("\nHere are your shots so far (H is hit, M is miss):");
		for (int i = 0; i < n; i++)
		{
			System.out.print(i + "   ");
		}
		System.out.println("");
		
		//print the results array that user have shoot
		for (int j = 0; j < n; j++)
		{
			if (j < 10)
			{
				System.out.print(userLocations[j] + "   ");
			}
			else
			{
				System.out.print(userLocations[j] + "    ");
			}
		}
		System.out.println("\nFire away! Aim for a location between 0 and 50");
	}
	
	//Print final information of the ships location and the shots
	public static void FinalInfo() 
	{
		
		System.out.println("\nHere are your shots so far (H is hit, M is miss):");
		for (int i = 0; i < n; i++)
		{
			System.out.print(i + "   ");
		}
		System.out.println("");
		
		//print the results array that user have shoot
		for (int j = 0; j < n; j++)
		{
			if (j < 10)
			{
				if (locations[j] != 0 && userLocations[j] == '-')
				{
					System.out.print("X   ");
				}
				else 
				{
					System.out.print(userLocations[j] + "   ");
				}
			}
			else
			{
				if (locations[j] != 0 && userLocations[j] == '-')
				{
					System.out.print("X    ");
				}
				else
				{
					System.out.print(userLocations[j] + "    ");
				}
			}
			
		}
		System.out.println("\nFire away! Aim for a location between 0 and 50");
	}
	
	//generate new random for ships
	public static void generateRandomShip(int shipi)
	{
		Random rand = new Random();
		int num = rand.nextInt(n - ship[shipi]) + 1;
		do
		{
			num = rand.nextInt(n - ship[shipi]) + 1;
		}
		while (isRepeated(num, shipi));
		
		for (int i = num; i < num + ship[shipi]; i++)
		{
			locations[i] = ship[shipi];
		}
	}
	
	//check if the random ship is repeated with other exist ships
	public static boolean isRepeated(int num, int shipi)
	{
		for (int i = num; i < num + ship[shipi]; i++)
		{
			if (locations[i] != 0)
			{
				return true;
			}
		}	
		return false;
	}
	
	//decide if the user shots a total ship
	public static boolean isShot(int s)
	{
		for (int i = 0; i < n; i++)
		{
			if (locations[i] == s)
			{
				if (userLocations[i] != 'H')
				{
					return false;
				}
			}
		}	
		return true;
	}
	
	//make sure the user input a valid shot and update the userLocations if user shots a ship location
	public static void shot(Scanner scan)
	{
		int times = 10;
		
		//allow user misses 10 times
		while (times > 0) 
		{
			//print shots of user so far
			shotInfo();
			
			int shot = Integer.parseInt(scan.nextLine());
			
			//make sure user inputs a valid number 
			if (shot > 50 || shot < 0)
			{
				do
				{
					System.out.println("Out of range. Try again.");
					shot = Integer.parseInt(scan.nextLine());
				}
				while (shot > 50 || shot < 0);
			}
			
			//make sure user inputs non-repeated number
			if (userLocations[shot] != '-')
			{
				do
				{
					System.out.println("You already fired there! Try again.");
					shotInfo();
					shot = Integer.parseInt(scan.nextLine());
				}
				while (userLocations[shot] != '-');
			}
			
			//tell user the result of this shoot
			int s = locations[shot];
			if(s != 0)
			{
				userLocations[shot] = 'H';
				//print the ships that have been shot by user
				if (isShot(s))
				{
					System.out.printf("Hit! You've sunk the size %d ship!\n", s);
				}
				else
				{
					System.out.println("Boom! That is a hit!!");
				}
			}
			
			else
			{
				System.out.println("Miss!");
				userLocations[shot] = 'M';
				times--;
			}
			
			//decide if the users wins the game before using out of allowed misses
			if (isAllShot())
			{
				System.out.println("You Wins! Unbelievable! You sank all the three boats!");
				return;
			}
		}
	}
	
	//decide if the user shots all of the three ships
	public static boolean isAllShot()
	{
		if (isShot(1) && isShot(2) && isShot(3))
		{
			return true;
		}
		return false;
	}
	
	//game starts
	public static void playGame(Scanner scan)
	{
		locations = new int[n];
		
		//generate new random for ships
		for (int i = 0; i < 3; i++)
		{
			generateRandomShip(i);
		}
		
		//generate original user locations array
		for (int i = 0; i < 9; i++)
		{
			userLocations[i] = '-';
		}
		for (int i = 9; i < n; i++)
		{
			userLocations[i] = '-';
		}
			
		//prompt user for shoot locations		
		shot(scan);
				
		//tell the user about the result of game
		if (!isAllShot())
		{
			//print the ships that have been shot by user
			System.out.println("You lose! Better luck next time.");
		}
		FinalInfo();
	}
	
	public static void main(String[] args)
	{
		
		Scanner scan = new Scanner(System.in);
		
		//print welcome messages
		welcome();
		playGame(scan);
		
		//prompt user for next step: play or end
		System.out.println("Play again? Enter y or n");
		String answer = scan.nextLine();
		
		//print the ending messages
		while (answer.charAt(0) == 'y')
		{
			playGame(scan);
			System.out.println("Play again? Enter y or n");
			answer = scan.nextLine();
		}
		
		System.out.println("Thank you for playing. Good-bye!");
		
		scan.close();
	}
}
