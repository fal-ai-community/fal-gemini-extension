---
name: product-ad-campaign
description: "Produce a complete fal product ad campaign from a brief and product references. Deliver reviewed hero art, channel variants, short motion ads and a reusable asset manifest."
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


# Product ad campaign

Turn one product brief into a consistent campaign asset package.

## Brief and production

Capture the product reference, original logo, approved copy, audience, offer,
channels, sizes, variant count and spending limit. Infer supplied values; ask only
for a missing input that blocks production. Never invent claims, discounts or testimonials.

1. Build a small matrix of hook × product benefit × channel. Name each deliverable
   and its dimensions. Keep the campaign concept and product identity consistent.
2. Lock one hero composition against the real product reference. Select a current
   reference-edit model through live discovery and use its actual input contract.
3. Review packaging, silhouette, colors, hands and product scale before variants.
   Use edit/reference inputs from the approved hero. Keep the product consistent;
   change only the planned hook, framing or backdrop.
4. Place original logos and exact copy with deterministic composition when model
   text or logos drift. Inspect the final exported image, including every copy string.
5. If motion is requested, animate approved product art with a verified image-to-video
   endpoint selected through live discovery. Check its required fields and supported
   duration before submission. Generate one short test before a batch.
6. Export each channel size without cutting the product, logo or CTA. Check current
   platform safe areas. Keep the editable composition, clean image and motion stems.

## Acceptance and delivery

Deliver a contact sheet, named final files, copy matrix and manifest. Check each
requested size, exact copy, actual product fidelity and motion continuity. Record
unverified platform specs. Do not publish ads, upload campaigns or make spending
commitments beyond the user's brief.

## Execution and specialist guidance

Use the installed `fal-media` skill for current model discovery, input contracts,
prices, native MCP execution and request recovery. Preserve the user's selected
provider, model, inputs, output count and spending limits.

The production checks above work without another domain skill. If a specialist
stage needs more guidance, follow `fal-media` to retrieve the relevant published
guide and only its needed version-pinned references. Reuse guidance already read.
If retrieval is unavailable, retain these local checks and current tool contracts;
report any stage that cannot be completed or verified. Do not invent a model,
privileged host tool or unavailable renderer to fill the gap.

Keep a manifest of sources, endpoint, actual inputs, request ID, result URL, local
file and QA findings. Inspect delivered artifacts and report unverified checks.

## Terminal execution

For a terminal-only workflow, read the [genmedia production-plan guide](../genmedia/references/production-plans.md)
and copy this skill's [example stage plan](assets/plan.json). The guide describes
explicit submission, state files and recovery. These examples are optional CLI
resources; connected MCP hosts use native fal tools.
