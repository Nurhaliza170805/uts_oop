# Definisi Class
class Animal:
    # Constructor, disebut saat objek dibuat
    def __init__(self, name, age):
        self.name = name  # Public variable
        self._age = age   # Protected variable (akses dari class dan subclass)
        self.__species = "Unknown"  # Private variable (akses hanya dari class ini)

    # Getter untuk mengambil nilai private variable
    def get_species(self):
        return self.__species

    # Setter untuk mengubah nilai private variable
    def set_species(self, species):
        self.__species = species

    # Method atau fungsi yang ada dalam class
    def make_sound(self):
        return "Some generic sound"

# Inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Memanggil constructor dari class Animal
        self.breed = breed

    # Overriding method dari class parent
    def make_sound(self):
        return "Woof woof!"

# Membuat objek dari class Dog
my_dog = Dog("Buddy", 3, "Golden Retriever")

# Menggunakan setter dan getter untuk private variable
my_dog.set_species("Dog")
print("Species:", my_dog.get_species())  # Output: Species: Dog

# Mengakses variabel dan method
print("Name:", my_dog.name)              # Output: Name: Buddy
print("Age:", my_dog._age)               # Output: Age: 3 (Protected variable)
print("Breed:", my_dog.breed)            # Output: Breed: Golden Retriever
print("Sound:", my_dog.make_sound())     # Output: Sound: Woof woof!
