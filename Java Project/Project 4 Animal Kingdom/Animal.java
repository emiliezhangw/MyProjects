
public abstract class Animal {

	protected String name;
	
	abstract boolean isWarmBlooded();
	
	public String toString() {
		return String.format("Animal Name: %-18s ", name);
	}
	
	public boolean equals(Animal other) {
		if (name.equalsIgnoreCase(other.name) && isWarmBlooded() == other.isWarmBlooded()) {
			return true;
		}
		return false;
	}
}

