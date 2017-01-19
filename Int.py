def main():
    
    print (
    """
Program for training intuition.
The program generated two number '1' or '0',
and you have to guess what fell. You have 100
attemps. Then the program show you results of
your training.
Don't thinking! Listen the voice of intuition!
    """
    )
    rezult = []
    Choice(rezult)
    printResult(rezult)



# loop logic
def Choice(rezult):
     
     import random
     valid = ['0','1','3']
     
     while len(rezult)<10:
        
          print('Card ¹', len(rezult) + 1, 'of 10')
          user_choice = input('Input "0" or "1"! For exit press enter "3"!: ')
          zagad = str(random.randrange(2))
                    
          if  not user_choice:
                print('Please input correct input!')          
          elif user_choice in valid[0:2]:
               Check(zagad, user_choice, rezult)
          elif user_choice in valid[2]:
               break
          else:
               print('Please input correct input!')
 
     return rezult      
          

#check correct input 0 or 1
def Check(zagad, user_choice, rezult):
        
         if zagad == user_choice:
                   rezult.append(1)
         else:
                   rezult.append(0)
         return

def printResult(rezult):
    print('\n\nResult: correct -', int(rezult.count(1)*100/len(rezult)), '%', 'incorrect -', int(rezult.count(0)*100/len(rezult)), '% from',len(rezult))
    
    print('Large range of 10 cards (correct | incorrect):')
    print('correct -', int(rezult.count(1)*100/len(rezult)), '%', 'incorrect -', int(rezult.count(0)*100/len(rezult)), '%')
    print('Two intervals of 5 cards (correct | incorrect):')
    print('[',rezult[:5].count(1), '|', rezult[:5].count(0),']','[',rezult[5:].count(1),'|', rezult[5:].count(0),']')
    print('5 small intervals of 2 cards (correct | incorrect):')
    
    
    input('\nPress Enter for exit..')
    
    

main()