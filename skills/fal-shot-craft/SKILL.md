---
name: fal-shot-craft
description: "Write or improve one fal video shot prompt. Use for physical action, motivated cameras and continuity anchors; do not use for full film assembly."
---

## Client execution adapter

This package uses the connected fal MCP tools for generation. CLI commands in
this guide and its references illustrate endpoint inputs and dependencies;
translate them into MCP calls instead of requiring a CLI installation.
Use recommend_model for current choices unless the user names an endpoint.
When it supplies next_call and input_contract, use those directly. Otherwise
inspect the endpoint schema and matching price units before execution.
Use run_model for bounded work; submit_job, check_job and get_job_result for
queued work. Save the request ID immediately and poll that same request.
Never assume a hosted sandbox, asset library or renderer exists. Verify local
capabilities before composition. If a required capability is absent, deliver
the reviewed components and report the incomplete stage. Preserve the user's
provider, model, scope, budget and approval boundaries.

The `genmedia` skill remains an optional terminal fallback only.


# Fal Shot Craft

Read [the production guide](references/production-guide.md) for this workflow.
It preserves fal's published production guidance, not a promise that every host tool exists here.

Before execution, map host-specific tools to available capabilities. Use `genmedia`
for model calls in terminal agents, or the installed fal MCP tools in plugin hosts.
Resolve current endpoints and inspect their contracts; the guide's model names and
prices are dated candidates. Preserve the user's model, provider, scope and budget.
Do not infer authorization from a guide's defaults or mandatory review language.

Check that the required local Python, Node, browser, renderer and media tools
exist before using them. Install publicly documented dependencies only within the
user's authorized setup. Otherwise report the missing dependency and stop the
dependent stage. This package does not supply hosted execution or an asset library.

Read supporting references from this skill folder as the guide directs.
Record actual request IDs and output paths. Deliver only artifacts you inspected;
identify incomplete stages and unverified checks.
