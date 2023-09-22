<script lang="ts">
    import "../styles.css"
    import SideButton  from "$lib/components/SideButton.svelte"
    //@ts-expect-error
    import DesktopWindowsRounded from "virtual:icons/material-symbols/desktop-windows-rounded"
    //@ts-expect-error
    import ScreenshotMonitor from "virtual:icons/material-symbols/screenshot-monitor"

    let active: {
        [key: string]: boolean
    } = {
        agents: false,
        Screenshots: false,
    };

    function handleSidebarClick(prop: string): void {
        for (const key of Object.keys(active)) {
            active[key] = false
        }

        active[prop] = true
         
    }

</script>


<div class="page">
    <div class="sidebar-container">
        <div class="logo"></div>
        <div class="break"></div>
        <div class="buttons">
            <SideButton isActive={active.agents} text={"Agents"} url={"/agents"} 
                on:click={() => handleSidebarClick("agents")}>
                <DesktopWindowsRounded class="icon"/>
            </SideButton>
            <SideButton isActive={active.screenshots} text={"Screenshots"} url={"/screenshots"} 
                on:click={() => handleSidebarClick("screenshots")}>
                <ScreenshotMonitor class="icon"/>
            </SideButton>

        </div>
    </div>
    <div class="content-container">
        <slot />
    </div>
</div>
<style>
    .page {
        display: flex;
        flex-direction: row;
        width: 100vw;
        height: 100vh;
    }
    
    .sidebar-container {
        width: 20vw;
        max-width: 200px;
        height: 100vh;
        background: var(--bg_main);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }
  
    .logo {
        height: 80px;
        background: var(--accent);
    }

    .break {
        width: 85%;
        border-bottom: 1px solid var(--bg_light);
    }

    .content-container {
        width: 100%;
        height: 100%;
        background: var(--bg_dark);
        display: flex;
        flex-direction: column;
    }

    .buttons {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        width: 100%;
    }

    .icon {
        font-size: 1rem;
    }

    @media only screen and (min-width: 1024px) {
        .icon {
            font-size: 1.3rem;
        }
    }
</style>
