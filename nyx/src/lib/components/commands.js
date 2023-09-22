let clear = {
    command: "clear",
    handler: function () {
        let div = document.getElementById("history");
        if (div === null) return;
        div.innerHTML = "";
        return "";
    }
}

let help = {
    command: "help",
    handler: function () {
        return `help - output all commands
clear - clear the screen`
    }
}

export let commands = [clear, help]
