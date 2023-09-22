<script lang="ts">
    export let data;
    import Console from "$lib/components/Console.svelte"

    let CurrentRenderedComponent = Console;

    let active: {
        [key: string]: boolean 
    } = {
        console: true,
        files: false,
        placeholder: false
    }

    function handleClick(current: string): void {
        for (let key of Object.keys(active)) {
            active[key] = false;
        }

        active[current] = true;
    }
</script>

<div class="container">
    <div class="top">
        <h2>Agent - {data.id}({data.agentType})</h2>
        <div class="top-content">
            <div>
                <p class="text" style="font-weight: 600">INFO</p>
                <p class="text"><span class="highlight">OS: </span>{data.os} {data.arch}</p>
                <p class="text"><span class="highlight">System: </span>username @ {data.hostname}</p>
                <p class="text"><span class="highlight">Process: </span>{data.procName} ({data.pid})</p>
                <p class="text"><span class="highlight">Comments: </span>TODO COMMENTS</p>
            </div>
            <div>
                <p class="text" style="font-weight: 600; padding: 0px; padding-bottom: 5px;">QUICK CONTROL</p>
                <div class="button">
                    <p class="kill-text">Kill Agent</p>
                </div>
            </div>
        </div>
    </div>
    <div class="bottom">
        <nav>
            <button class="nav-button" class:active={active.console} on:click={() => handleClick("console")}>Console</button>
            <button class="nav-button" class:active={active.files} on:click={() => handleClick("files")}>Files</button>
            <button class="nav-button" class:active={active.placeholder} on:click={() => handleClick("placeholder")}>Placeholder</button>
        </nav>
        <CurrentRenderedComponent />
    </div>
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        height: 100vh;
        gap: 15px;
        align-items: center;
        padding-left: 15px;
        padding-right: 15px;
    }

    .top {
        display: flex;
        flex-direction: column;
        height: 25vh;
        width: 100%;
        margin-top: 10px;
    }

    .bottom {
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
        margin-bottom: 10px;
    }

    h2 {
        padding-left: 10px;
        color: var(--text);
        font-family: monospace;
        font-size: 20px;
    }

    .text {
        font-family: monospace;
        color: var(--text);
        padding-left: 10px;
        font-size: 16px;
        margin: 0px;
        margin-top: 1px;
    }

    .highlight {
        color: var(--accent);
    }

    .top-content {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }

    .kill-text {
        font-family: monospace;
        font-size: 16px;
        font-weight: bold;
        margin: 0px;
    }

    .button {
        background-color: var(--bg_dark);
        border: 1px solid var(--error);
        display: inline-block;
        padding: 8px;
        border-radius: 4px;
        color: var(--error);
    }

    .button:hover {
        background-color: var(--error);
        cursor: pointer;
        color: var(--bg_dark);
    }

    nav {
        width: 100%;
        height: 30px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
    }

    .nav-button {
        background-color: var(--bg_main);
        border: none;
        color: var(--text);
    }

    .active {
        border-bottom: 1px solid var(--accent);
        color: var(--accent);
    }
</style>
