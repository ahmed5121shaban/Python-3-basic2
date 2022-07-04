class game:
    def __init__(self):
        while True:
            print('''HELLO from our simple game
                  choice btwean this games :
                  1-print single and even numper
                  2-print the long of Sentence
                  3-All numbers that are divisible by the second number
                  4-Printing numbers from 0 to the user numper
                  5-Two numbers that are divisible by numbers from 0 to 100
                  6-to exit from this game
                  ''')
            numof_game = int(input('inter your game numper : '))
            if numof_game == 1:
               self.even_single()
            elif numof_game == 2:
               self.long_sentence()
            elif numof_game == 3:
               self.divide_thenum()
            elif numof_game == 4:
               self.print_num()
            elif numof_game == 5:
               self.divide_twonum()
            elif numof_game == 6:
                break
            else:
                print('please inter game numper from 1 to 6')
                numof_game = int(input('inter your game numper : '))
            choice1=input('press any key to play again or N to exit : ')
            if choice1=='N' or choice1=='n':
                break

            
    def even_single(self):
        numper = input('inter numpers : ')
        even = []
        single = []
        for x in numper:
            if int(x) % 2 == 0:
                even.append(x)
            else:
                single.append(x)
        print(f'your even numpers : {even}')
        print(f'your single numpers : {single}')
    
    def long_sentence(self):
        sentence = input('inter Sentence : ')
        words = [word for word in sentence.split()]
        for word in words:
            word_long = words.index(word)
        print(f'The number of words = {word_long}')

        
    def divide_thenum(self):
        frist_num = int(input('your frist numper : '))
        second_num = int(input('rang for numper from 0 to : '))
        your_num = []
        for c in range(0,second_num+1):
            if c % frist_num == 0:
                your_num.append(c)
        print(your_num)

    def print_num(self):
        user_numper = int(input('inter your numper : '))
        list_of_num = []
        for x in range(0,user_numper+1):
            list_of_num.append(x)
        print(list_of_num)


    def divide_twonum(self):
        num1 = int(input('inter frist numper : '))
        num2 = int(input('inter second numper : '))
        num3 = []
        for x in range(0,100+1):
            if x % num1 == 0 or x % num2 == 0:
                num3.append(x)
        print(num3)


  
x = game()
