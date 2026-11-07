# fal.ai for Gemini CLI

Create images, videos, audio and 3D with the hosted [fal MCP server](https://fal.ai/mcp).
The extension includes six focused skills: `fal-media` and five creative outcome
guides. It retrieves specialist guidance, current model contracts and pricing
through MCP when needed. The [community repository](https://github.com/fal-ai-community/skills)
keeps the complete library, references and optional local production tools.

## Install

```sh
gemini extensions install https://github.com/fal-ai-community/fal-gemini-extension
```

Restart Gemini. When the client requests authorization, use `/mcp auth fal` and
sign in with your fal account. Confirm that fal tools appear before generation.
The extension needs no API key in a file. Generation consumes your fal credits.

If your Gemini settings already define a server named `fal`, those settings take
precedence over the extension. Review that entry before a connection change.
Use a current Gemini CLI version with remote Streamable HTTP and browser OAuth.

## Try a creative workflow

- **Product campaign:** create hero art, channel variants and a short motion ad from your product brief and references.
- **Game assets:** produce consistent sprites, animation frames and an atlas with measured frame geometry.
- **Short film:** turn a storyboard into reviewed shots, then assemble picture and sound with local production tools.
- **Product photography:** create accurate hero, detail and lifestyle images from real SKU references.
- **Localization:** adapt speech, timed captions and channel cuts while preserving the source message.

Example:

> Use fal to plan a three-image campaign for my reusable water bottle. Ask for
> the product reference and missing brand details. Check models and prices, then
> show the deliverables and estimated cost before generation.

Assembled films, atlases and captioned exports can require local composition
tools. Check those capabilities before promising a completed export. This compact
extension installs no CLI, renderer, hooks or local runtime dependencies.

For the complete library and optional tools, use the community repository's
[installation guide](https://github.com/fal-ai-community/skills/blob/main/docs/install.md).
The [v0.1.0 full archive](https://github.com/fal-ai-community/skills/releases/tag/v0.1.0)
remains available for users who explicitly need every skill.

## Updates

```sh
gemini extensions update fal-ai
```

This repository is a generated distribution adapter. Edit skills in the canonical
repository, then regenerate this adapter from a reviewed commit. Do not edit the
copied skill files independently. `skills-source.lock.json` identifies that source;
`bundle-source.lock.json` records each generated file's hash.

Maintainers run the canonical `scripts/build-distribution.py` with a full source
commit SHA. Its default Gemini export is hybrid; `--gemini-bundle full` is an
explicit full-library option for separate exports. Copy the default `gemini/`
output into this repository. Rebuild the file-hash
lock and run the local validation before an update. CI validates files only.

```sh
python3 scripts/validate.py
```

The current adapter passed local extension installation and skill discovery.
Browser OAuth, refresh and generation remain separate runtime checks. Gallery
visibility depends on Google's crawler and validation, after topic registration.

MIT. The skill library and this adapter retain the canonical license.
