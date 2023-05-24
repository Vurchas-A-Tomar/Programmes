name, service_years, diwali_bonus = input('Enter Name, Years of Service, Diwali bonus: ').split()

service_years = int(service_years)
diwali_bonus = int(diwali_bonus)

deduction = 2 * service_years + diwali_bonus * 5.5/100
print(deduction)
