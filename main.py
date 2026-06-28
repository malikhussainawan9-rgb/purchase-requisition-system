#-------- FINAL VERSION ------------

import tkinter as tk
from tkinter import messagebox

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

# =========================================================
# TKINTER GUI (The View)
# =========================================================
class RequisitionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Purchase Requisition System")
        self.root.geometry("400x500")

        # Entry fields
        tk.Label(root, text="Staff Name:").pack()
        self.name_ent = tk.Entry(root); self.name_ent.pack()
        
        tk.Label(root, text="Staff ID:").pack()
        self.id_ent = tk.Entry(root); self.id_ent.pack()
        
        tk.Label(root, text="Date (DD/MM/YYYY):").pack()
        self.date_ent = tk.Entry(root); self.date_ent.pack()
        
        tk.Label(root, text="Item Name:").pack()
        self.item_name_ent = tk.Entry(root); self.item_name_ent.pack()
        
        tk.Label(root, text="Item Price:").pack()
        self.price_ent = tk.Entry(root); self.price_ent.pack()

        # Buttons
        tk.Button(root, text="Add Item", command=self.add_item_to_req).pack()
        self.item_list = tk.Listbox(root, height=5); self.item_list.pack()
        
        tk.Button(root, text="Calculate Total", command=self.calc_total).pack()
        self.total_lbl = tk.Label(root, text="Total: $0"); self.total_lbl.pack()
        
        tk.Button(root, text="Check Approval", command=self.process_req).pack()
        self.result_lbl = tk.Label(root, text="", fg="blue"); self.result_lbl.pack()

        self.current_req = None

    def add_item_to_req(self):
        if not self.current_req:
            self.current_req = Requisition(self.date_ent.get(), self.id_ent.get(), self.name_ent.get())
        
        price = float(self.price_ent.get())
        self.current_req.add_item(self.item_name_ent.get(), price)
        self.item_list.insert(tk.END, f"{self.item_name_ent.get()} - ${price}")
        self.item_name_ent.delete(0, tk.END); self.price_ent.delete(0, tk.END)

    def calc_total(self):
        if self.current_req:
            self.total_lbl.config(text=f"Total: ${self.current_req.total}")

    def process_req(self):
        if self.current_req:
            self.current_req.check_approval()
            self.result_lbl.config(text=f"ID: {self.current_req.requisition_id}\n"
                                        f"Status: {self.current_req.status}\n"
                                        f"Ref: {self.current_req.approval_ref}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RequisitionGUI(root)
    root.mainloop()