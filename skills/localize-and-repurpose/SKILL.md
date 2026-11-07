---
name: localize-and-repurpose
description: "Localize and repurpose existing creative content with fal. Deliver translated speech, accurate subtitles and channel cuts while preserving meaning, brand assets and source provenance."
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


# Localize and repurpose content

Turn an existing approved asset into verified locale and channel variants.

## Source and language contract

Collect the source media, transcript if available, target locales, glossary,
protected names, exact claims, voice permissions, target channels and budget.
Keep the original master unchanged. Pin speaker choices and preserve original
brand assets while changing only the requested locale and channel treatment.

1. Inspect source streams and duration. Extract an audio container before a speech
   endpoint that requires `audio_url`; a video path is not an audio URL.
2. Select a currently accessible timed transcription endpoint through live
   discovery. Check its language-code convention and word-timing output contract.
   Filter timing tokens by their actual type before building captions.
3. Translate the verified transcript for meaning, register, units and the supplied
   glossary. Preserve claims and proper nouns; do not invent stronger promises.
   Mark uncertain translations for a fluent reviewer before calling them approved.
4. For a dub, discover a current dubbing endpoint and inspect its target-language
   and source-media fields. Compare voices, speaker identity and meaning against the source.
   Do not add lip sync unless requested and supported by the chosen contract.
5. Re-transcribe the localized output for actual word timings. Build SRT/VTT from
   those timings, not proportional estimates from the original captions.
6. Make requested platform cuts from meaningful sentence/scene boundaries. Reframe
   around the subject; do not stretch footage. Recompose exact text/logo assets for
   each aspect ratio. Preserve RTL layout and glyph coverage where applicable.
7. Assemble with an available verified renderer. Check that dubbing did not remove
   requested music/effects. Keep localized voice, music and picture stems separate.

## Acceptance and delivery

Deliver folders by locale and channel, localized video/audio, SRT/VTT, translated
copy, glossary decisions and manifest. Verify no missing lines, caption order,
nonnegative timestamps, caption ends within runtime, text coverage and source/target
meaning. Listen to names and numbers. State when native-language review remains
outstanding. Do not publish or distribute variants without a separate instruction.

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
