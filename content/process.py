#importing libraries
import random
import string

#creating variables
word=''
word_hint=''
alphabet=set(string.ascii_uppercase)
name=''
tries=0
win=0
loss=0
rand_num=0

#------history detail lists -----------
rand_word_list=[]
num_of_tries=[]
used_tries_list=[]
state_list=[]
rand_num_list=[]

def word_list():
    'word list for the program'
    wlist=['apple','car','road','python','designer','kitchen','chicken','home','fan','clock',
           'browser','phone','adult','fruits','window','books','fish','table','file','door']
    return wlist

def hint_list():
    'hint list for the program'
    hintlist=['Red delicious fruit','You can ride it','Path to somewhere','Programming language','One that create awesome arts','You can cook here','A lots of non-vegitarians love this food','Place that you and your family live','Equipment that give wind','It is always ticking',
           'Application software for accessing the World Wide Web','Technical equipment that everyone use in there day to day life','The grown ups','Eatable thing get from trees','Thing that used to get wind to the room','You can read this','These are swim in water','You studie on this','You store papers in this','You use this to enter a room']
    return hintlist

def rand_word():
    'getting random word from word list'
    global word, word_hint, rand_num_list
    rand_num=random.randrange(0,20)
    rand_num_list.append(rand_num)
    word=(word_list()[rand_num]).upper()
    word_hint=(hint_list()[rand_num])
    

    
def main():
    'main process'
    #creating variables
    global word, guessed_lett, alphabet, tries, win, loss, rand_word_list, num_of_tries, used_tries_list, state_list, word_hint
    word_lett=[]
    used_tries=0
    guessed_lett=set()
    
    rand_word()#calling random word funtion
    
    rand_word_list.append(word)#add word for history list
    
    #creating letter list of the word
    for x in range (len(word)):
        word_lett.append((word[x]))

    tries=len(word)#number of tries user getting
    num_of_tries.append(tries)#add number of tries to history list

    #show hint for the word
    print()
    print('HINT : ',word_hint)
    
    #displaying '_' number of word letters
    current_wd = []
    for x in range(len(word)):
        current_wd+='_'
        
    #main loop
    while len(word_lett)>0 and tries>0:
        print()
        print('You have',tries,'tries left')

        #show current_wd in string type
        print('Current word', ' '.join(current_wd))
        
        #getting user input
        user_lett=input('Guess a letter : ').upper()

        #show letter when correct letter guessed
        for position in range(len(word)):
            letter = word[position]
            
            if letter == user_lett:
                current_wd[position] = letter

        
        if user_lett in alphabet - guessed_lett:
            guessed_lett.add(user_lett)

            #remove letter from word_lett list if user guessed correctly
            if user_lett in word_lett:
                try:
                    while True:
                        word_lett.remove(user_lett)
                except ValueError:
                    pass

            else:
                tries-=1
                print('Wrong guess')

                
        elif user_lett in guessed_lett:
            print('YOU ALREADY USED THIS LETTER, TRY AGAIN!')

        else:
            print('INVALID INPUT, TRY AGAIN!')

    used_tries=len(word)-tries
    used_tries_list.append(used_tries)
    
    #check tries and give result after while loop
    if tries==0:
        print()
        print('LOOOSER! Word is : ',word)
        loss+=1
        state_list.append('LOSS')

    else:
        print()
        print('CONGRATULATIONS! You gesse the word correctly')
        print('Word is',word)
        win+=1
        state_list.append('WIN')
