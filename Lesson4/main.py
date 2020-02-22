import website_alive.check_response as cr
s = input("Print url : ")
print("Доступен" if (cr.check_response(s)) else "Не доступен")