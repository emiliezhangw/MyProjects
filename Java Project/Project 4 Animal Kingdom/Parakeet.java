
public class Parakeet extends Bird implements Winged, Adoptable{

	public Parakeet (String name) {
		this.name = name;
	}
	
	@Override
	public String toString() {
		return super.toString() + " Parakeet";
	}

	@Override
	public boolean canFly() {
		return true;
	}

	@Override
	public String homeCareDirections() {
		return "Feed, talk to, give lots of love.";
	}
	
}
