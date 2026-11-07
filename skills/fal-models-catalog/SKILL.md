---
name: fal-models-catalog
description: "Compare fal model families by modality and role. Use for catalog exploration; verify current availability and contracts before execution."
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


# fal.ai Models Catalog

Endpoint-first navigation for fal.ai production work. Each modality reference lists curated picks organized by use case (premium realism / fast & cheap / 4K / specialized). Before reaching for free-text search, consult the modality reference that matches the task.

> **Runtime:** All endpoint calls run via the [genmedia CLI](https://github.com/fal-ai-community/genmedia-cli). See the `genmedia` skill for command syntax; run `genmedia init` once if not yet installed.

## Endpoint-first rule

1. Pick the endpoint ID from the right modality reference.
2. Verify it: `genmedia models --endpoint_id <endpoint_id> --json`.
3. Inspect it: `genmedia schema <endpoint_id> --json`.
4. Check cost when relevant: `genmedia pricing <endpoint_id> --json`.
5. Use text search only if the routed endpoint is missing, deprecated, rejected, or the role is not covered here:

 ```bash
 genmedia models "<task description>" --json
 genmedia docs "<topic>" --json
 ```

Do not invent endpoint IDs.

## Modality references

Load the reference matching the user's task:

- [text-to-image.md](references/text-to-image.md), image generation from prompt (text-heavy, premium still, fast draft)
- [image-to-image.md](references/image-to-image.md), image editing, inpainting, background removal, upscaling
- [text-to-video.md](references/text-to-video.md), video generation from prompt (highest quality, fast/economical, multi-shot storytelling)
- [image-to-video.md](references/image-to-video.md), video from a reference frame (including audio-driven and lip-sync variants)
- [video-to-video.md](references/video-to-video.md), video edit, restyle, upscale, background removal
- [text-to-3d.md](references/text-to-3d.md), 3D model generation from text
- [image-to-3d.md](references/image-to-3d.md), 3D model generation from reference images
- [text-to-audio.md](references/text-to-audio.md). TTS, music, SFX generation
- [audio-to-text.md](references/audio-to-text.md), speech-to-text (Whisper, ElevenLabs Scribe with diarization)
- [image-to-text.md](references/image-to-text.md). OCR, captioning, VQA, detection, segmentation

## Utility endpoints

Workflow utility endpoint IDs (resize, composite, mask, audio merge, subtitle, etc.) live in the `fal-workflow` skill:
[fal-workflow/references/utility-endpoints.md](../fal-workflow/references/utility-endpoints.md).

Utility endpoints are explicit because they are deterministic tools, not creative model choices. Always inspect schema before use.
