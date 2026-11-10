class TouristPackage:
    def __init__(self, country='', duration=0, price=0, hotel_name='', rating=0):
        self.__country = country
        self.__duration = duration
        self.__price = price
        self.hotel_name = hotel_name
        self.rating = rating
        
        
    def get_country(self):
        return self.__country
    
    def get_price(self):
        return self.__price
    
    def get_duration(self):
        return self.__duration

    def setter_countr(self, new_countr):
        return self.__country == new_countr
    
    
    def __lt__(self, other):
        return self.__price < other.get_price()  

    def __add__(self, object):
        return TouristPackage(
            self.__country + object.get_country(),
            self.__price + object.get_price(),
            self.__duration + object.get_duration()    
            )
        
    
    def __str__(self):
        return (f'Країна: {self.__country} \n'
            f'Тривалість : {self.__duration} \n'
            f'Ціна: {self.__price} \n'
            f"готель: {self.hotel_name}\n"
            f'Рейтинг: {self.rating}\n')
    
    
    def __repr__(self):
        return (
            f"TouristPackage(country={self.__country}, "
            f"duration={self.__duration}, "
            f"price={self.__price})"
        )
    # def __del__(self):
    #     print('всі значення видалені')
        
        
def main():
    tour1 = TouristPackage()
    tour2 = TouristPackage("Italy", 7, 850.0)
    tour3 = TouristPackage("Spain", 10, 1200.0)
    
    # tour4 = tour1 + tour2
    tour4 = tour2 + tour3
    print(tour4)
    print(tour2)
    # tour1.hotel_name = "Unknown"
    # tour1.rating = 0.0

    # tour2.hotel_name = "Hilton"
    # tour2.rating = 4.8

    # tour3.hotel_name = "Marriott"
    # tour3.rating = 4.5
    
    # for tour in (tour1, tour2, tour3):
    #     print("Туристична путівка")
            
    #     print("Країна:", tour.get_country())
    #     print("Тривалість:", tour.get_duration())
    #     print("Ціна:", tour.get_price())
    #     print(tour1.setter_countr('Italy'))
    #     print(str(tour))
    #     print(repr(tour))

    
    
    # del tour
    # del tour1
    # del tour2
    # del tour3
    # print("Кінець програми")
    
    tours = [
        TouristPackage("Італія", 7, 30000),
        TouristPackage("Франція", 5, 25000),
        TouristPackage("Єгипет", 10, 20000),
        TouristPackage("Іспанія", 6, 28000),
    ]
    for t in sorted(tours):
        print(t)



if __name__ == '__main__':
    main()
