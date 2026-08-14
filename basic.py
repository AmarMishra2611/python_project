book_title = input("Enter the book title: ").strip().title()
author_name = input("Enter author name: ").strip().title()
price = float(input("Price: "))
stock = int(input("Stock Quantity: "))
total_price = price * stock
# output
print("\n" + "=" * 32)
print("            Book Details            ")
print("=" * 32)
print("Book Title:", book_title)
print("Author Name:", author_name)
print("Price:", price)
print("Stock Quantity:", stock)
print(f"Total Price:    rs.{total_price:.2f}")