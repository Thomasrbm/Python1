from give_bmi import give_bmi, apply_limit

try:
    height = ["qsdqsd", 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")