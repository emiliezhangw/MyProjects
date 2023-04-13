
public class Cat extends Mammal implements Adoptable{

	public Cat(String name){
		this.name = name;
	}
	
	@Override
	public String homeCareDirections() {
		return "Feed, change litter, give lots of love.";
	}

	@Override
	public String toString() {
		return super.toString() + " Cat";
	}
}
