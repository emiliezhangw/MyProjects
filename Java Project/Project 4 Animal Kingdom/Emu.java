
public class Emu extends Bird implements Winged{

	public Emu(String name) {
		this.name = name;
	}

	@Override
	public boolean canFly() {
		return false;
	}
	
	@Override
	public String toString() {
		return super.toString() + " Emu";
	}
	
}
