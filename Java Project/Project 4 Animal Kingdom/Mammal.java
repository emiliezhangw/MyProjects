
public class Mammal extends Animal {

	@Override
	boolean isWarmBlooded() {
		return true;
	}
	
	@Override
	public String toString() {
		return super.toString() + "Warm Blooded\tMammal";
	}

}
