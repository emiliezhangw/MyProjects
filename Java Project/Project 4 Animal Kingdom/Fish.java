
public class Fish extends Animal implements WaterDweller{

	@Override
	boolean isWarmBlooded() {
		return false;
	}

	@Override
	public boolean canLiveOutOfWater() {
		return false;
	}
	
	@Override
	public String toString() {
		return super.toString() + "Cold Blooded\tFish";
	}

}
