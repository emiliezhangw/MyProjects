
public class Reptile extends Animal {

	@Override
	boolean isWarmBlooded() {
		return false;
	}
	
	@Override
	public String toString() {
		return super.toString() + "Cold Blooded\tReptile";
	}

}
