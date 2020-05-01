def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

for i in range(5):
    print(next(my_gen))

do_something = 4
do_something += 3
print(f'do_something: {do_something}')

for i in range(100):
    print(next(my_gen))