# Changelog

## 1.3.0

- Add an option for intro/interlude characters to follow the interface font or
  use a custom installed font family.
- Change the default active lyric color to `on_surface`.
- Change the default maximum visible character count to 15.

## 1.2.0

- Select the active MPRIS player across all available `playerctl` players.
- Add optional player allowlist and blocklist settings with wildcard matching.
- Send play/pause commands to the selected player instead of the global default.
- Prevent stale lyric and artwork requests from replacing the current track.

## 1.1.0

- Add per-widget active and inactive lyric color controls.
- Keep theme-aware semantic colors as defaults while allowing custom colors.

## 1.0.0

- Initial public release.
- Synchronized status-bar lyric widget with karaoke highlighting and animated
  line transitions (karaoke, cascade, wave, fade, none).
- Long-line smooth marquee scrolling with end pauses.
- Intro/instrumental cue text with configurable characters.
- Lyric sources: auto, LRCLIB, public NetEase, MPRIS text, custom HTTP, and
  external IPC push.
- Album artwork display with circular crop and runtime cache.
- Track-information fallback (`title + artist`) when no lyrics are available.
- Right-click pause/resume via `playerctl` with dimmed paused state.
- KRC dynamic-lyric parsing (plain, prefixed, and three-argument formats).
