<script lang="ts">
    // @ts-expect-error

    export let text: string;
    export let url: string;
    export let isActive: boolean;
</script>

<a href="{url}" class="link" on:click>
    <div class="container" style={isActive ? "border-bottom: 1px solid var(--accent)" : ""}>
        <slot />
        <p class="text">{text}</p>
    </div>
</a>

<style>
    .container {
        height: 35px;
        display: flex;
        align-items: center;
        flex-direction: row;
    }

    .link {
        text-decoration: none;
        color: var(--text);
        width: 85%;
    }

    .text {
        padding-left: 10px;
        font-family: monospace;
        font-size: 1rem;
        font-weight: 600;
    }
</style>
