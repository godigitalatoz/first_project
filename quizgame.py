print ('Welcome to Python Quiz Game')
def start_game():
    while True:
        playing = input('Do you want to play? :').lower()
        if playing == 'yes':
            print ('Lets Play:)')
            return 'yes'
        elif playing =='no':
            print ('goodbye:)')
            quit ()
            return 'no'
        else:
            print ('Invalid Input, Try Again')
decision = start_game()

score = 0
ans = input ('Is python an object oriented language ? ').lower()
if ans ==  'yes':
    print ('correct')
    score +=1
else:
    print ('incorrect')

ans = input ('what is short for - integrated development environment ').lower()
if ans ==  'IDLE':
    print ('correct')
    score +=1
else:
    print ('incorrect')

ans = input ('Is python a high level language? ').lower()
if ans ==  'yes':
    print ('correct')
    score +=1
else:
    print ('incorrect')

ans = input ('what is NUMPY? ').lower()
if ans ==  'numerical python':
    print ('correct')
    score +=1
else:
    print ('incorrect')


print ('your score is ' + str (score))
print ('your percentage is ' + str ((score/4)*100))
