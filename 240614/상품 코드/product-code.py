class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

product1 = Product('codetree', 50)
product_name, product_code = input().split()
product2 = Product(product_name, product_code)

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")