variable1 = 1;
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

try:
    variable2 = 10 * (1/0);
except ZeroDivisionError:
    print("You're trying to divide by 0 dude!")
    # raise means it will still show the error line and ends the program
    raise
except:
    print("Unexpected error")
    raise

print("Next line")