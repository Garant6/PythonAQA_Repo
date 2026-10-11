from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S23", "+79998887766"),
    Smartphone("Apple", "13", "+75554443322"),
    Smartphone("NothingPhone", "9 Pro", "+74651118862"),
    Smartphone("Xiaomi", "10T", "+74561238855"),
    Smartphone("Samsung", "S25 Ultra", "+77777777777")
]

for phone in catalog:
    print(f"{phone.phone_stamp} - {phone.phone_model}. {phone.phone_number}")
