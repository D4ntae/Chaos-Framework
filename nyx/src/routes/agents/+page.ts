import type { PageLoad } from "./$types";

export const load: PageLoad = async({ fetch }) => {
    let agentsPromise = await fetch("http://127.0.0.1:5000/agents/getall")
    let agents = await agentsPromise.json();
    return {
        agents
    }
}
