
public class Bat extends Mammal implements Winged{
	
	public Bat(String name) {
		this.name = name;
	}
	
	@Override
	public String toString() {
		return super.toString() + " Bat";
	}

	@Override
	public boolean canFly() {
		return true;
	}
	
}
