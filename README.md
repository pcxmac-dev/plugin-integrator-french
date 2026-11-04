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
.venv\Scripts\python.exe -m pip install "plugin-integrator-french @ git+https://github.com/pcxmac-dev/plugin-integrator-french@v0.2.0"
```

or with the app's plugins (`pip install -e ".[plugins]"` in liminal-charts). The app loads it on its next
start.

## Compatibility

It is written for plugin API 2.0, the class contract of liminal-libs 1.3.0 (`PUBLISHER.api`; the
publisher is `FrenchLibrary`, a `PublisherPlugin` subclass declaring its datasets, `PUBLISHER` its
instance). An app offering 2.0 or a later 2.x loads it; an app of another major leaves it out and
says why on the Plugins view.

## Develop

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install "liminal-libs @ git+https://github.com/pcxmac-dev/liminal-libs@release/0.2.0"
.venv\Scripts\python.exe -m pip install -e ".[dev]"
.venv\Scripts\python.exe -m pytest -q
```

Tests never send requests and never read your keys.
