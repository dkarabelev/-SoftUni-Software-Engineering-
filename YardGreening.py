area = float(input())
total_before_discount = area * 7.61
discount = total_before_discount * 0.18
after_discount = total_before_discount - discount
print(f"The final price is: {after_discount} lv.")
print(f"The discount is: {discount} lv.")