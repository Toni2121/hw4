temp: float = float(input("please enter today's temperature: "))
print(f"{'normal' if 0 <= temp <= 20 else 'freezing' if temp < 0 else 'hot'} ")

