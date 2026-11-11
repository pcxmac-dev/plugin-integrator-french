# Changelog

## 0.3.0 (2026-11-11)

Its API on its page (plugin API 2.2, liminal-libs 1.49.0; the user: "each plugin should reflect the the API its
attached to, and present links that provide documentation, the plugin interface should more or less contain what it
already has, BUT, it should also expose more of what the API is about"). `FrenchLibrary.apis` (apis.py) is the
library's card: Kenneth R. French's Data Library, zipped CSV files on the library's server, with its pages (the
library, the 3 and 5 factors' and the 49 industries' details, the changes in CRSP data), every section of the library
(the 3 and 5 factors and the industry portfolios it reads; the sorts, the momentum and reversal factors, the
breakpoints, book equity, the benchmarks, the developed and emerging markets it does not), the four files it downloads
and the library's others, verified 2026-11-11. Nothing it reads or does changes; it learns nothing while it runs, so
`api_facts()` says nothing. Needs liminal-libs>=1.49.0. A test checks that the card names the files the plugin really
reads; `LIMINAL_VENDOR_PAGES=1` asks each address on it.

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
