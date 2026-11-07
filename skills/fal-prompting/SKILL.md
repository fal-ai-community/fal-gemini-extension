---
name: fal-prompting
description: "Write prompts for a selected fal model family. Use for GPT Image, Kling and Happy Horse parameter-specific prompt craft; select an endpoint before use."
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


# fal.ai Prompting

> **Runtime:** All endpoint calls run via the [genmedia CLI](https://github.com/fal-ai-community/genmedia-cli). See the `genmedia` skill for command syntax; run `genmedia init` once if not yet installed.

Model families have meaningful prompting nuances. A prompt that works on GPT Image 2 (long, structured, exact text in quotes) will fail on Happy Horse (which wants ~20 plain-English words). This skill collects family-specific guides.

## When to load which reference

| Reference | Load when |
|-----------|-----------|
| [kling.md](references/kling.md) | Working with Kling video models (O3, v3), multi-prompt, element controls, Standard vs Pro tier |
| [gpt-image-2.md](references/gpt-image-2.md) | Working with `openai/gpt-image-2` or `/edit`, structured prompts, EXACT TEXT, multi-image compositing |
| [happy-horse.md](references/happy-horse.md) | Working with `alibaba/happy-horse/text-to-video` or `image-to-video`, brevity-first, camera language |

## Universal principles (all families)

1. **Visual facts beat prestige adjectives.** Replace "stunning, cinematic, masterpiece" with "overcast daylight, brushed aluminum, 50mm feel."
2. **Style tags need visual targets.** "Minimalist brutalist" → "cream background, heavy black sans serif, asymmetrical type block, generous negative space."
3. **One controlled variable per iteration.** Comparison only works when one axis changes at a time.
4. **Inspect schema before assuming a control exists.** `genmedia schema <endpoint_id> --json`. Negative prompt, seed, multi-prompt, and reference-image fields differ across families.
5. **Per-family rules override universal advice.** Happy Horse rejects what GPT Image 2 rewards.

## Catalog cross-reference

For "which model do I use" questions, see `fal-models-catalog`:

- Text-to-image endpoint selection → [fal-models-catalog/references/text-to-image.md](../fal-models-catalog/references/text-to-image.md)
- Text-to-video endpoint selection → [fal-models-catalog/references/text-to-video.md](../fal-models-catalog/references/text-to-video.md)
- Image-to-video endpoint selection → [fal-models-catalog/references/image-to-video.md](../fal-models-catalog/references/image-to-video.md)
