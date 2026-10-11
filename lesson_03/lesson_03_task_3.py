from address import Address
from mailing import Mailing


to_addr1 = Address("48895", "London", "Parkov Street", "89", "12")
from_addr1 = Address("47561", "Saransk", "Lenina Street", "123", "212")

firts_mail = Mailing("{to_addr1}", "{from_addr1}", "5000", "34544-4143810")

print(
    f"Отправление {firts_mail.track} из {from_addr1.index}, "
    f"{from_addr1.flat} {from_addr1.city}, {from_addr1.street}, "
    f"{from_addr1.house} - в {to_addr1.index}, {to_addr1.city}, "
    f"{to_addr1.street}, {to_addr1.house} - {to_addr1.flat}. "
    f"Стоимостью {firts_mail.cost} рублей"
)
