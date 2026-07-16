# Contributing

Thanks for helping improve the Noctalia Lyrics plugin. This repository is the
primary development source. Stable releases are periodically synced to
[noctalia-dev/community-plugins](https://github.com/noctalia-dev/community-plugins).

## Getting started

1. Fork the repository and create a topic branch from `main`.
2. Make your change. Keep plugin code under the repository root (the plugin
   manifest is `plugin.toml` with `id = "h465855hgg/lyrics"`).
3. Run the validation workflow locally:

   ```sh
   python3 tools/validate.py
   ```

4. Open a pull request describing the motivation and behavior change.

## Guidelines

- **Plugin API**: keep `plugin_api` aligned with the current Noctalia community
  requirement. Do not reintroduce `min_noctalia`; the upstream CI has deprecated
  it.
- **Translations**: English is shipped as `translations/en.json`. Add other
  locales alongside it. Keep `label_key`/`description_key` references valid.
- **No secrets**: never include browser cookies, player credentials, or API
  tokens. The plugin only uses public endpoints and local MPRIS metadata.
- **Assets**: screenshots live in `screenshots/` and the catalog thumbnail is
  `thumbnail.webp` (960x540). Avoid large binary diffs.
- **Code style**: match the existing Luau/Python style. No comments unless the
  change is non-obvious.

## Reporting issues

Use the bug or feature templates. Include Noctalia version, your media player,
lyrics source configuration, and reproduction steps.
