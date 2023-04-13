
public class BlueWhale extends Whale implements WaterDweller{

	public BlueWhale(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return super.toString() + " BlueWhale";
	}

	@Override
	public boolean canLiveOutOfWater() {
		return false;
	}
}
