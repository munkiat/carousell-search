from pycarousell import CarousellSearch
import arrow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
import chatbot as robot
from configurations import RESULTS_COUNT

Base = declarative_base()

class CarousellListing(Base):
    __tablename__ = 'itemlistings'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer)
    seller = Column(String)
    title = Column(String)
    currency_symbol = Column(String)
    price = Column(Float)
    time = Column(String)

engine = create_engine('sqlite:///searchListings.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def find_stuff(search_query):
    my_want = CarousellSearch(search_query, results=RESULTS_COUNT)
    results = my_want.send_request()

    for r in results:
        #skip results without query in listing title
        if want not in (r['title']).lower():
            continue
        #check if listing is in DB already
        check = (session.query(CarousellListing).filter_by(listing_id=r['id']).
                    first())
        #if it is not in DB
        if check is None:
            listing = CarousellListing(
                listing_id = r['id'],
                seller = r['seller']['username'],
                title = r['title'],
                currency_symbol = r['currency_symbol'],
                price = r['price'],
                time = arrow.get(r['time_created']).format('DD/MM/YYYY HH:MM')
            )
            session.add(listing)
            session.commit()
            line_item = (r['seller']['username'], r['title'], r['price'],
                        arrow.get(r['time_indexed']).format('DD/MM/YYYY HH:MM'))
            robot.post_message(', '.join(line_item))
    return
