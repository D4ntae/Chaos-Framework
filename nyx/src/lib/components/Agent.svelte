<script lang="ts">
    //@ts-expect-error
    import DesktopWindowsRounded from "virtual:icons/material-symbols/desktop-windows-rounded"

    export let agentType: string;
    export let arch: string;
    export let hostname: string;
    export let id: number;
    export let os: string;
    export let pid: string;
    export let procName: string;
</script>

<a href="/agents/{id}" style="text-decoration: none;">
    <div class="container">
        <DesktopWindowsRounded style="font-size: 2.2rem; color: white;" /> 
        <div class="text-container">
           <div class="div-container">
                <p class="text">Type: <span style="color: var(--accent)">{agentType}</span></p>
                <p class="text">Last active: 5 seconds ago</p>
            </div>
            <div class="div-container">
                <p class="text">username @ <span style="color: var(--accent)">{hostname}</span></p>
                <p class="text">{os} <span style="color: var(--accent)">{arch}</span></p>
            </div>
            <div class="div-container">
                <p class="text">{procName}</p>
                <p class="text">PID: <span style="color: var(--accent)">{pid}</span></p>
            </div>
            <div class="div-container">
                <p class="text">Test comments</p>
            </div>
        </div>
    </div>
</a>

<style>
    .container {
        background-color: var(--bg_main);
        width: 100%;
        height: 50px;
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 20px;
        padding-left: 20px;
        border: 1px solid var(--bg_light);
        box-shadow: 2px 2px 5px black;
    }

    .div-container {
        text-align: left;
        height: 50px;
    }

    .text-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        width: 100%;
    }

    .text {
        padding: 0px;
        margin: 0px;
        padding-top: 3px;
        font-family: monospace;
        font-size: 16px;
        color: var(--text);
        font-weight: 600;
    }

    @media only screen and (max-width: 1024px) {
        .text {
            font-size: 12px;
        }
    }
</style>
