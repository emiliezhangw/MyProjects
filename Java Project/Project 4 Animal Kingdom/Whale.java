
public class Whale extends Mammal {
	
	public Whale() {
		this.name = "";
	}
	
	public Whale(String name) {
		this.name = name;
	}
	
	@Override
	public String toString() {
		return super.toString() + " Whale";
	}
}
