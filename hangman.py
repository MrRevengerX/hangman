#importing modules
import content.process as process
import content.log as log

name=''
state='Y'

log.get_name()

#game replay loop
while state=='Y':
    process.main()
    print()
    state=input("Enter 'Y' to play again or enter any letter to stop playing : ").upper()

print()
print("You've played ",(process.win+process.loss),'games')
print('You won : ',process.win,'games')
print('You loss : ',process.loss, 'games')

#calling functions
log.create_txt()
log.create_web()
