import processing
import time
from configurations import ITEMS, FREQUENCY

if __name__ == "__main__":
    while True:
        try:
            for i in ITEMS:
                processing.find_stuff(i)
        except KeyboardInterrupt:
            print ("Interrupt")
            sys.exit(1)
        time.sleep(600)
