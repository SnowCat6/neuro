# neuro script
Simple neuronet to learn and classify by answers

- db_config.py - append asks
- db_learn.py - append learn entryes
- db_classify.py - append classify entryes
- classify.py - classify exists entryes

# Install
- Install Phyton v3.6.x
- Use Phyton pip install tensorflow and keras (pip install tensorflow keras)

- Run db_config.py and enter asks for learning
- Run db_learn.py and enter items for learning database, fit asks and their classify
- Run db_classify.py and add main classify database for classify by learning database

# Use
- append -p \<profile\> to swith at new profile of learn and classify (db_learn.py -p new_profile)
- append -r to remove current profile (db_learn.py -p new_profile -r)
- append -l to list profiles db_learn.py -l
- append -n to re-new all learn database items woth new defines (db_learn.py -p new_profile -n)
