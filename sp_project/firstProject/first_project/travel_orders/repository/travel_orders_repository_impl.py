from travel_orders.entity.travel_orders import TravelOrders
from travel_orders.repository.travel_orders_repository import TravelOrdersRepository

class TravelOrdersRepositoryImpl(TravelOrdersRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def create(self, accountId, status):
        orders = TravelOrders(account_id=accountId, status=status)
        orders.save()

        return orders