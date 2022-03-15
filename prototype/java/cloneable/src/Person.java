import java.util.Arrays;

public class Person implements Cloneable{
    public String[] names;
    public Address address;

    public Person(String[] names, Address address) {
        this.names = names;
        this.address = address;
    }

    @Override
    public String toString() {
        return "Person{" +
                "names=" + Arrays.toString(names) +
                ", address=" + address +
                '}';
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        // Not a correct implementation
//        return new Person(names, address);

        // deep copy
        return new Person (names.clone(), (Address) address.clone());
    }
}
