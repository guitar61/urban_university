class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            products = file.read().strip()
            file.close()
            return products
        except FileNotFoundError:
            return ""
        except Exception as e:
            return f"An error occurred: {e}"

    def add(self, *products):
        try:
            # Get current products from the file
            current_products = self.get_products()

            # Create a set of existing product names
            existing_names = set()
            if current_products:
                for line in current_products.split('\n'):
                    existing_names.add(line.split(',')[0].strip())

            # Open the file in append mode
            file = open(self.__file_name, 'a')
            for product in products:
                if product.name in existing_names:
                    print(f"Product {product.name} is already in the store")
                else:
                    file.write(str(product) + '\n')
                    existing_names.add(product.name)
            file.close()
        except Exception as e:
            return f"An error occurred: {e}"


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Testing __str__ method

    s1.add(p1, p2, p3)

    print(s1.get_products())
