from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta) :
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name =consumer_name
        self.__consumer_number = DirectToHomeService.__counter

        DirectToHomeService.__counter+=1
    def get_consumer_name(self):
        return self.__consumer_name
    def get_consumer_number(self):
        return self.__consumer_number
    @abstractmethod
    def calculate_monthly_rent(self):
        pass


class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name =base_pack_name
        self.__subscription_period = subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name
    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        base_pack=["Silver","Gold","Platinum"]
        if self.__base_pack_name in base_pack:
            return True
        else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")

    def calculate_monthly_rent(self):
        Base_Pack = ["Silver" , "Gold" ,"Platinum"]
        Monthly_Rent=[350.00,440.00,560.00]
        discount = 0
        self.__base_pack_name = self.__base_pack_name.capitalize()
        final_rent = 0
        if self.__subscription_period >=1 and self.__subscription_period <=24:
            if self.validate_base_pack_name():
                Bp_Index = Base_Pack.index(self.__base_pack_name)
                rent=Monthly_Rent[Bp_Index]
                if self.__subscription_period >12:
                    discount =rent
                final_rent =((rent*self.__subscription_period)-discount)/self.__subscription_period
            return final_rent
        else:
            return -1

