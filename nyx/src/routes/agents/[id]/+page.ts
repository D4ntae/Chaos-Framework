import type { PageLoad, RouteParams } from "../$types";

interface Params extends RouteParams {
    id: string;
}

export const load: PageLoad = async ({ fetch, params }) => {
    let { id } = params as Params;
    let url = "http://127.0.0.1:5000/agents/agent/" + id;
    let agentPromise = await fetch(url);
    let agent = await agentPromise.json();
    console.log(agent)
    return {
        ...agent
    }
}
