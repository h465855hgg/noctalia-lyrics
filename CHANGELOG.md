# Changelog

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
