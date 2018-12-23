# neuro script
Simple neuronet to learn and classify by answers

- config.py - append asks
- learn.py - append learn entryes
- classify_db.py - append classify entryes
- classify.py - classify exists entryes

# Install
- Install Phyton v3.6.x
- Use Phyton pip install tensorflow and keras (pip install tensorflow keras)

- Run config.py and enter asks for learning
- Run learn.py and enter items for learning database, fit asks and their classify
- Run classify_db.py and add main classify database for classify by learning database

# Use
- append -p <profile> to swith at new profile of learn and classify (learn.py -p new_profile)
- append -r to remove current profile (learn.py -p new_profile -r)
- append -l to list profiles learn.py -l
- append -n to re-new all learn database items woth new defines (learn.py -p new_profile -n)
