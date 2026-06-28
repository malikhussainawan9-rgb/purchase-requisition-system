# =========================================================
# THE REQUISITION CLASS (Encapsulation)
# =========================================================
class Requisition:
    # Class attribute to track ID across all instances
    _id_counter = 10001
    
    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition._id_counter
        Requisition._id_counter += 1
        
        self.items = [] # Encapsulated list of items
        self.total = 0.0
        self.status = "Pending"
        self.approval_ref = "Not Available"

    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        self.total += price

    def check_approval(self):
        # Decision-making logic
        if self.total < 500:
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_ref = f"{self.staff_id}{last_three}"
        else:
            self.status = "Pending"
            self.approval_ref = "Not Available"


if __name__ == "__main__":
    # Example usage
    req = Requisition("01/01/2024", "S123", "John Doe")
    req.add_item("Laptop", 450.00)
    req.add_item("Mouse", 25.00)
    req.check_approval()
    
    print(f"Requisition ID: {req.requisition_id}")
    print(f"Total: ${req.total}")
    print(f"Status: {req.status}")
    print(f"Approval Reference: {req.approval_ref}")