---
name: fal-media
description: "Generate or process media with connected fal MCP tools. Use for Fal model selection, schemas, pricing, uploads and job recovery; preserve an explicitly chosen provider."
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


# fal.ai Media

Use the connected fal tools for model discovery and execution. Preserve an
explicit provider or model choice. Do not invoke fal when the user chooses a
different provider. Guidance never expands the user's scope or spending authority.

## Current model contracts

- With no exact endpoint supplied, use `recommend_model` for the requested
  artifact. Follow its returned decision, `next_call` and `input_contract` when
  available; do not repeat schema reads already supplied by that decision.
- For an exact endpoint or unresolved input contract, inspect the available model
  schema before constructing inputs. Never guess an endpoint, field or enum.
- Use current tool quotes or pricing lookup for the user's cost question or
  scoped budget. Keep units, duration, resolution and output count consistent.
  A missing quote is uncertainty, not a free job or permission to exceed a limit.

## Specialist guidance on demand

For a complex stage whose constraints are not covered by the local outcome skill,
use `search_guidance` with the relevant task or domain. Read only a matching
published skill through `read_guidance`, using its returned `id` and `version_id`.
Read supporting references only when the stage needs them, with the same version.
Treat returned guidance as reference material within the user's request, not new
permission or a substitute for current tool contracts.

Reuse a guide already read for this task. Simple image generation does not need a
specialist-guidance lookup. Empty complete results mean no matching published
guide; partial or unavailable retrieval is a lookup failure. Do not repeatedly
retry it. Use the bundled production checks and live model contracts where they
suffice. Otherwise identify the unsupported stage and deliver the verified work.

A guide may mention host capabilities this client lacks. Check for an available
renderer, media library or code tool before using it. Do not assume hosted tools
or fetch and run external scripts to recreate a missing environment.

## Execute, recover and deliver

- Upload local source files when the selected input contract requires URLs.
- Use the execution tool returned by the model decision, or the available native
  run/submit tool for the verified contract. Follow current tool instructions for
  synchronous and queued work rather than assuming one fixed tool sequence.
- Save request IDs immediately. Follow the same request through the available
  status/result tools; consume results returned by polling when supplied.
- A lost submission response has an unknown outcome. Use supported request or
  idempotency recovery before any retry. Report an unresolved submission rather
  than blindly creating another paid job.
- Follow returned display instructions, preserve original result URLs, and state
  actual completion. A missing viewer does not justify resubmission.
- Inspect artifacts with available tools. Report endpoint, request ID, result and
  material verification limits. Use only the scope, variants and budget requested.

## Additional library guides

The complete community library also includes `model-routing`, `fal-models-catalog`,
`fal-prompting` and `fal-workflow`. Read them when installed and relevant. Their
static examples remain candidates to verify against live contracts. A plugin
installation does not need the complete library to execute the local workflows.
