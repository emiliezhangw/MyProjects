
public class Goldfish extends Fish implements Adoptable{

	public Goldfish (String name) {
		this.name = name;
	}
	
	@Override
	public String homeCareDirections() {
		return "Feed, change water, and give lots of love.";
	}
	
	@Override
	public String toString() {
		return super.toString() + " Goldfish";
	}

}
