from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_instances = []
    bar = CinemaBar()
    
    for customer_data in customers:
        customer = Customer(
            name=customer_data.get("name"), 
            food=customer_data.get("food")
        )
        customer_instances.append(customer)
        bar.sell_product(customer, customer.food)
        
    hall = CinemaHall(number=hall_number)
    staff_cleaner = Cleaner(name=cleaner)
    
    hall.movie_session(
        movie=movie, 
        customers=customer_instances, 
        cleaner=staff_cleaner
    )
