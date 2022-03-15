public class Demo {
    public static void main(String[] args) throws Exception {

        // We want to create a deep copy or clone of an object
        Person john = new Person(new String[]{"John", "Smith"}, new Address("London Road", 123));
        Person jane = john; // Copying just the reference
        jane.names[0] = "Jane";
        jane.address.houseNumber = 124;

        System.out.println(john);
        System.out.println(jane);


//        Not a correct implementation
//        Person jane2 = (Person) john.clone();
//        jane2.names[0] = "Jane";
//        jane2.address.houseNumber = 124;
//
//        System.out.println(john);
//        System.out.println(jane);

        // Not a correct implementation
        // Implementation of Cloneable is not recommended
        Person jane2 = (Person) john.clone();
        john.names[0] = "John";
        jane2.names[0] = "Jane";
        jane2.address.houseNumber = 124;

        System.out.println(john);
        System.out.println(jane2);

    }
}
