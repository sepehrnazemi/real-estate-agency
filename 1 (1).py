# class Home:
#     def __init__(self, area_size, address, const_year, rooms, parking, furnished, status):
#         self.address = address
#         self.area_size = area_size
#         self.const_year = const_year
#         self.rooms = rooms
#         self.parking = parking
#         self.status = status
#         self.furnished = furnished

# class BuyingHome(Home):
#     def __init__(self, price, address, area_size, const_year, rooms, parking, furnished, seller, buyer, status):
#         super().__init__(address, const_year, area_size, rooms, parking, furnished, status)
#         self.price = price
#         self.seller = seller
#         self.buyer = buyer

# class RentingHome(Home):
#     def __init__(self, security_deposit, mo_rent, address, area_size, const_year, rooms, parking, furnished, period, start_date, owner, renter, status):
#         super().__init__(address, const_year, area_size, rooms, parking, furnished, status)
#         self.security_deposit = security_deposit
#         self.mo_rent = mo_rent
#         self.period = period
#         if start_date != "unknown":
#             start_date = start_date.split(" ")
#             self.start_date = datetime(start_date[0], start_date[1], start_date[2])
#             self.end_date = self.start_date + relativedelta(months=+int(self.period))
#         else:
#             self.start_date = "unknown"
#             self.end_date = "unknown"
#         self.owner = owner
#         self.renter = renter
