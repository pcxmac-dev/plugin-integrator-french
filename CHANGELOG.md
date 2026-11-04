# Changelog

## 0.2.0 (2026-11-03)

Renamed `plugin-integrator-french` (the package `plugin_integrator_french`; it was `liminal-plugin-french`) on 2026-11-03: the naming by system (plugins are `plugin-<app>-<name>`), on liminal-libs 1.4.0 (`liminal_libs`, the library renamed with it).

A class on plugin API 2.0 (liminal-libs 1.3.0; the user: "all the plugins under liminal should basically
follow inheritance/oop paradigm"): `FrenchLibrary`, a `PublisherPlugin` subclass, declares what the `Publisher`
record held (its name, kind, datasets and scrape checks, as class attributes); `PUBLISHER` is its instance,
the entry point as before. Nothing it does or says changes. Version 0.2.0: every Liminal distribution is
released at 0.2.0 together, tested against the library's `release/0.2.0` branch until the release.

## 1.1.1 (2026-11-02)

The plugin imports the library as `liminal_libs` and depends on liminal-libs (the app, renamed liminal-charts, is no longer needed to run the tests; the user, 2026-11-02: "lets rename the app to liminal-charts").

## 1.1.0 (2026-11-01)

- Released as its own package, `plugin-integrator-french`, registered under the entry point group
  `liminal.providers`; its version is the distribution's.
- Plugin API 1.4.

## 1.0.0 (2026-10-31)

- Built into the app (then massive-collate): the library's four datasets declared by this plugin
  (plugin API 1.4).
