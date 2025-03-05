from cart import Cart
from device import Device
from smartphone import Smartphone

if __name__ == "__main__":
    # Create devices
    device = Device('Laptop', 530, 33, '2030')
    sm1 = Smartphone('iPhone', 129000, 33, '2030', 15, 100)
    sm2 = Smartphone('Poco', 28000, 55, '2035', 10, 24)

    # Create cart and add devices
    cart = Cart()
    cart.add_device(sm1, 150)
    cart.add_device(sm2, 10)

    # Print cart items and total price
    cart.print_items()
    print(f"Total Price: {cart.get_total_price()}")

    # Proceed to checkout
    cart.checkout()