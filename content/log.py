#importing modules
import content.process as process

#creating variables
name=''

def get_name():
    'ask user for enter player name'
    global name
    name=input('Enter your name : ')
    return name
    

def create_txt():
    'txt file log creation'
    log_file=open('log.txt','w')#creating text file
    log_file.write('Name : ' + name + '\n\n')

    for i in range (len(process.rand_word_list)): #type data collected in hangman funtion using loop
        log_file.write('Game #' + str(i+1)+'\n')
        log_file.write('Word guessed : ' + process.rand_word_list[i]+'\n')
        log_file.write('Turns provided : ' + str(process.num_of_tries[i])+'\n')
        log_file.write('Turns used : ' + str(process.used_tries_list[i])+'\n')
        log_file.write('Win/lost status : ' + process.state_list[i]+'\n\n')

    log_file.write('Total number of games played : '+str(process.win+process.loss)+'\n')
    log_file.write('Total wins : '+str(process.win)+'\n')
    log_file.write('Total loses :'+str(process.loss))
    
    log_file.close()

def create_web():
    'web page log creation'
    web_file=open('log_web.html','w')#opening html file in writing mode

    #type basic codes of HTML and styles
    web_file.write('<!DOCTYPE html>\n<head><style>table{\nwidth:450px;\nmargin-left: auto; \nmargin-right: auto;\n} \nimg{\nwidth:150px\n}\nh2, h4{\ntext-align: center;\n}</style>\n<title>Hangman Log</title>\n</head>')
    web_file.write('<body><h2>''Player name : '+ name +'</h2>\n')#show player name top center
    
    for i in range (len(process.rand_word_list)): #show table green or red according to WIN or LOSS
        if process.state_list[i]=='WIN':
            web_file.write('<table border="1" bordercolor=green>\n')
        else:
            web_file.write('<table border="1" bordercolor=red>\n')
            
        web_file.write('<th colspan="2"> Game #'+str(i+1)+'</th>')
        web_file.write('<th rowspan="5" style="width:100px"><img src=".\\img\\'+str(process.rand_num_list[i])+'.jpg"></th>')
        web_file.write('<tr>\n<td>Word guessed : </td><td>'+process.rand_word_list[i]+'</td>\n</tr>')
        web_file.write('<tr>\n<td>Turns provided : </td><td>'+str(process.num_of_tries[i])+'</td>\n</tr>')
        web_file.write('<tr>\n<td>Turns used : </td><td>'+str(process.used_tries_list[i])+'</td>\n</tr>')
        web_file.write('<tr>\n<td>Win/lost status : </td><td>'+process.state_list[i]+'</td>\n</tr>')
        web_file.write('</table><br>')

    web_file.write('<h4>Total number of games played : '+str(process.win+process.loss)+'</h4>')
    web_file.write('<h4>Total wins : '+str(process.win)+'</h4>')
    web_file.write('<h4>Total loses : '+str(process.loss)+'</h4>')
    web_file.write('</body></html>')
    web_file.close()
    
