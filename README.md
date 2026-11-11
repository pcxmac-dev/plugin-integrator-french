# plugin-integrator-french

Kenneth R. French's Data Library (Tuck School of Business, Dartmouth) for
[Liminal](https://github.com/pcxmac-dev/liminal-charts): the Fama/French 3 and 5 factors and the 49
industry portfolios, daily and monthly from 1926 (1963 for the 5 factors), returns in percent. Four
datasets (`PublisherPlugin.datasets`), each a zipped CSV from the library's own server, fetched with the
app's `datasets fetch` and again every 30 days, every revision kept (the library revises its history
every month). No key; the files are free to download for research: cite the library.

A Liminal publisher plugin released on its own. The app finds it through the entry point group
`liminal.providers` and lists it on the Plugins view and in `liminal-charts plugins`
as `package: plugin-integrator-french`, with this package's version.

## Install

Into the app's environment, from the app's folder:

```powershell
.venv\Scripts\python.exe -m pip install "plugin-integrator-french @ git+https://github.com/pcxmac-dev/plugin-integrator-french@v0.3.0"
```

or with the app's plugins (`pip install -e ".[plugins]"` in liminal-charts). The app loads it on its next
start.

## Its API

The library is files, not a query API: [Kenneth R. French's Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html),
each table a zipped CSV (and text) file on the library's server, replaced in place when the library revises its
history from new CRSP data ([Changes in CRSP Data](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/changes_crsp.html)).
The plugin reads four of them: the [Fama/French 3 factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html)
daily and monthly, the [5 factors (2x3)](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_5_factors_2x3.html)
daily and the [49 industry portfolios](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html)
daily. No key, no published limit (the plugin keeps to 20 requests a day, an hour apart), nothing to pay.

`FrenchLibrary.apis` (`apis.py`, plugin API 2.2) says this on the plugin's page: the library's pages, every section
of the library (the ones the plugin reads first, then the sorts, the momentum and reversal factors, the breakpoints,
book equity, the benchmarks, and the developed and emerging markets), the files it downloads and the library's others,
as read on 2026-11-11.

## Compatibility

It is written for plugin API 2.2, the class contract of liminal-libs 1.49.0 (`PUBLISHER.api`; the
publisher is `FrenchLibrary`, a `PublisherPlugin` subclass declaring its datasets and what it attaches
to, `PUBLISHER` its instance). An app offering 2.2 or a later 2.x loads it; an app of another major,
or an older 2.x, leaves it out and says why on the Plugins view.

## Develop

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install "liminal-libs @ git+https://github.com/pcxmac-dev/liminal-libs@release/0.2.0"
.venv\Scripts\python.exe -m pip install -e ".[dev]"
.venv\Scripts\python.exe -m pytest -q
```

Tests never send requests and never read your keys.
