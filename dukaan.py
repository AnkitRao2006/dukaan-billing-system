class Dukaan:
    def __init__(self):
        self.items = {} # Ab format: {name: (qty, price)}
        self.total = 0
        self.load_from_file()
        print("Namaste! Dukaan khul gayi 👑")

    def add_item(self):
        name = input("Item ka naam kya hai? ")
        price = int(input("1 piece ka Price kitna hai? ₹"))
        qty = int(input("Kitne piece? "))

        if name in self.items:
            old_qty, old_price = self.items[name]
            new_qty = old_qty + qty
            self.items[name] = (new_qty, price)
            self.total += price * qty
            print(f"✅ {name} - {qty} piece aur add. Total {new_qty} piece")
        else:
            self.items[name] = (qty, price)
            self.total += price * qty
            print(f"✅ {name} x{qty} - ₹{price * qty} add ho gaya")

    def show_bill(self):
        if not self.items:
            print("Dukaan khali hai bhai")
            return
        print("\n===== TERA BILL =====")
        for item, (qty, price) in self.items.items():
            item_total = qty * price
            print(f"{item} x{qty} : ₹{item_total}")
        print("---------------------")
        print(f"TOTAL: ₹{self.total}")
        print("=====================\n")

    def delete_item(self):
        name = input("Kaunsa item hatana hai? ")
        if name in self.items:
            qty, price = self.items[name]
            self.total -= qty * price
            del self.items[name]
            print(f"🗑️ {name} dukan se nikal gaya")
        else:
            print("Abe ye item hai hi nahi dukan me")

    def save_to_file(self):
        with open("dukaan_data.txt", "w") as f:
            for item, (qty, price) in self.items.items():
                f.write(f"{item},{qty},{price}\n")
        print("💾 Data save ho gaya")

    def load_from_file(self):
        self.total = 0
        try:
            with open("dukaan_data.txt", "r") as f:
                for line in f:
                    item, qty, price = line.strip().split(",")
                    qty, price = int(qty), int(price)
                    self.items[item] = (qty, price)
                    self.total += qty * price
            print("📂 Purana data load ho gaya")
        except FileNotFoundError:
            print("Nayi dukan hai bhai")

    def run(self):
        while True:
            print("\n1. Maal Add Karo")
            print("2. Bill Dekho")
            print("3. Maal Delete Karo")
            print("4. Dukaan Band Karo")
            choice = input("Kya karna hai? ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.show_bill()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                self.save_to_file()
                print("Dukaan band. Kal milte hai ⚡")
                break
            else:
                print("Galat button daba diya bhai")

# Dukan chalu karo
apni_dukan = Dukaan()
apni_dukan.run()