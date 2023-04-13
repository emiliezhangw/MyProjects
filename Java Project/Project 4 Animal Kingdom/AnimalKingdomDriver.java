import java.util.*;

public class AnimalKingdomDriver {
	public static void main(String[] args) {
		
		ArrayList<Animal> animalList = new ArrayList<>();
		Bat bat = new Bat("Count Batula");
		animalList.add(bat);
		animalList.add(new BlueWhale("Blubby Blubs"));
		animalList.add(new Cat("Ms. Purrfect"));
		animalList.add(new Emu("Outback Ollie"));
		animalList.add(new Goldfish("Sammy Swimmer"));
		animalList.add(new Otter("Henry Handholder"));
		animalList.add(new Parakeet("Songbird Stu"));
		animalList.add(new Turtle("Shelly Silversteen"));
		
		System.out.println("***** Here are all the animals. (8 animals printed)");
		for(Animal animal : animalList) {
			System.out.println(animal);
		}
		
		System.out.println("\n\n***** Check on the equals method."); 
		Bat batTest = new Bat(new String("Count Batula"));
		System.out.println("Should print true: " + bat.equals(batTest));
		batTest = new Bat(new String("COUNT BATULA"));
		System.out.println("Should print true: " + bat.equals(batTest));
		batTest = new Bat(new String("Batman"));
		System.out.println("Should print false: " + bat.equals(batTest));

		
		System.out.println("\n\n***** Here are just the mammals. (4 animals printed)");
		for(Animal animal : animalList) {
			// YOUR CODE HERE
			if (animal instanceof Mammal) {
				System.out.println(animal);
			}
		}
		
		System.out.println("\n\n***** Here are the winged animals along with information about whether they can fly.  (3 animals printed)");
		for(Animal animal : animalList) {
			// YOUR CODE HERE
			if (animal instanceof Winged) {
				System.out.printf("%-61s",animal);
				if (((Winged) animal).canFly()) {
					System.out.println("Can fly");
				}
				else {
					System.out.println("Cannot fly");
				}
			}
		}
		
		System.out.println("\n\n***** Here are the adoptable animals along with their care directions.  (4 animals printed)");
		for(Animal animal : animalList) {
			// YOUR CODE HERE
			if (animal instanceof Adoptable) {
				System.out.printf("%-69s",animal);
				System.out.println(((Adoptable)animal).homeCareDirections());
			}
		}
	
		
		System.out.println("\n\n***** Here are the animals that can dwell in water, along with whether they can also live on land.  (4 animals printed)");
		for(Animal animal : animalList) {
			// YOUR CODE HERE
			if (animal instanceof WaterDweller) {
				System.out.printf("%-69s", animal);
				if (((WaterDweller) animal).canLiveOutOfWater()) {
					System.out.println("Can also live on land");
				}
				else {
					System.out.println("Cannot also live on land");
				}
			}
		}
	}
}