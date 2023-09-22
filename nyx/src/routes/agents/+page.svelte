<script lang="ts">
    //@ts-expect-error
    import DesktopWindowsRounded from "virtual:icons/material-symbols/desktop-windows-rounded"
    import Agent from "$lib/components/Agent.svelte"

    export let data: {
        agents: any[]
    };
</script>

<div class="container">
    <h1 class="title">Agents</h1>
    <div class="table-start">
        <DesktopWindowsRounded style="font-size: 2.2rem; color: var(--bg_dark)" /> 
        <div class="text-container">
            <div class="div-container">
                <p>Info</p>
            </div>
            <div class="div-container">
                <p>System</p>
            </div>
            <div class="div-container">
                <p>Process</p>
            </div>
            <div class="div-container">
                <p>Comments</p>
            </div>
        </div>
    </div>
    <div class="agents">
        {#each data.agents as agent}
            <Agent {...agent}/>
        {/each}
    </div>
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        padding-left: 30px;
        padding-right: 30px;
    }

    .div-container {
        text-align: left;
    }

    .title {
        color: var(--text);
        font-size: 3rem;
        font-family: monospace;
    }

    .agents {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .table-start {
        width: 100%;
        display: flex;
        flex-direction: row;
        gap: 20px;
        padding-left: 20px;
        color: var(--text_grey); 
        font-family: monospace;
        font-weight: bold;
        font-size: 20px;
    }

    .text-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        width: 100%;
    }
</style>
