<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import { commands } from "./commands.js"

    let value: string;
    let inputRef: HTMLElement;

    let commandHistory: string[] = [];
    let historyPointer: number = -1;

    function keydownHandler(event: KeyboardEvent) {
        let key = event.key;
        if (key === "Tab") {
            event.preventDefault();
            for (let command of commands) {
                if (command.command.startsWith(value)) {
                    let input = document.getElementById("c-input")! as HTMLInputElement;
                    value = command.command;
                    input.value = command.command;

                    let ghost = document.getElementById("ghost")!;
                    ghost.innerText = ""
                    return
                }
            }
        } else if (key === "ArrowUp") {
            event.preventDefault();
            if (historyPointer === -1 && commandHistory.length === 0) return;
            if (historyPointer < commandHistory.length - 1) {
                historyPointer++; 
            }
            let input = document.getElementById("c-input")! as HTMLInputElement;
            value = commandHistory[historyPointer];
            input.value = commandHistory[historyPointer];
        } else if (key === "ArrowDown") {
            event.preventDefault();
            let input = document.getElementById("c-input")! as HTMLInputElement;
            if (historyPointer === 0) {
                historyPointer = -1;
                value = "";
                input.value = "";
            }
            if (historyPointer > 0) {
                historyPointer--;
                value = commandHistory[historyPointer];
                input.value = commandHistory[historyPointer];
            }
        }
    }

    onMount(() => {
        document.addEventListener("keydown", keydownHandler);
    })

    onDestroy(() => {
        document.removeEventListener("keydown", keydownHandler);
    })

    function autocomplete() {
        let ghost = document.getElementById("ghost")!;
        ghost.innerText = ""
        for (let command of commands) {
            if (command.command.startsWith(value)) {
                let t = "";
                for (let i = 0; i < value.length; i++) {
                    t += " ";
                }
                t += command.command.substring(value.length)
                if (value === "") {
                    t = ""
                }
                ghost.innerText = t;
                return;
            }
        }
    }

    function compareCommands(c1: string, c2: string): boolean {
        let c1Split = c1.split(" ");
        let c2Split = c2.split(" ");
        return c1Split[0] === c2Split[0]; 
    }

    function handleCommand(): string {
        for (let command of commands) {
            if (compareCommands(command.command, value)) {
                // @ts-ignore
                let output: string = command.handler() ;
                if (output !== "Command not found.") {
                    commandHistory.unshift(value);
                    if (commandHistory.length === 100) {
                        commandHistory = commandHistory.slice(0, 99);
                    }
                }
                historyPointer = -1;
                return output;
            }
        }

        return "Command not found."
    }

    function submitHandler() {
        let div = document.getElementById("history");

        let newLine = document.createElement("p");
        newLine.innerText = "> " + value;
        newLine.className = "history-line";
        div?.appendChild(newLine);

        let output = handleCommand();
        newLine = document.createElement("p");
        newLine.innerText = output;
        newLine.className = "history-line";
        div?.appendChild(newLine);

        inputRef.focus();

        value = "";
    }
</script>

<div class="container">
    <div class="content" id="history">
    </div>
    <div class="console-input">
        <span class="arrow">> </span>
        <span id="ghost" class="ghost-text"></span>
        <form on:submit|preventDefault={submitHandler}>
            <input bind:this={inputRef} bind:value on:input={autocomplete} type="text" id="c-input"/>
        </form>
    </div>
</div>

<style>
    .container {
        height: 75vh;
        width: 100%;
        display: flex;
        flex-direction: column;
    }

    .content {
        height: 90%;
        margin-top: 15px;
        background-color: black;
        border: 1px solid var(--accent);
        overflow: auto;
    }

    input:focus {
        outline: none;
        border: 1px solid white;
    }

    input {
        background-color: var(--bg_main);
        border: 1px solid var(--accent);
        height: 30px;
        padding-left: 32px;
        color: var(--text);
        font-size: 16px;
        font-family: monospace;
        margin-bottom: 15px;
        width: 100%;
        font-weight: bold;
    }

    .ghost-text {
        position: absolute;
        padding-left: 33px;
        top: 8px;
        color: dimgrey;
        font-size: 16px;
        font-family: monospace;
        font-weight: bold;
    }

    .arrow {
        font-family: monospace;
        color: white;
        width: 25px;
        position: absolute;
        font-size: 22px;
        padding-left: 10px;
        font-weight: bold;
        height: 25px;
        top: 4px;
    }

    .console-input {
        position: relative;
        display: flex;
        flex-direction: row;
        width: 100%;
        margin-top: 15px;
    }

    form {
        display: flex;
        width: 100%;
    }

    :global(.history-line) {
        font-family: monospace;
        color: var(--text);
        font-size: 14px;
        padding-left: 5px;
    }

    #ghost {
        white-space: pre-wrap;
    }
</style>
