# liminal-plugin-french

Kenneth R. French's Data Library (Tuck School of Business, Dartmouth) for
[Liminal](https://github.com/pcxmac-dev/liminal): the Fama/French 3 and 5 factors and the 49
industry portfolios, daily and monthly from 1926 (1963 for the 5 factors), returns in percent. Four
datasets (`Publisher.datasets`), each a zipped CSV from the library's own server, fetched with the
app's `datasets fetch` and again every 30 days, every revision kept (the library revises its history
every month). No key; the files are free to download for research: cite the library.

A Liminal publisher plugin released on its own. The app finds it through the entry point group
`liminal.providers` and lists it on the Plugins view and in `python -m liminal plugins`
as `package: liminal-plugin-french`, with this package's version.

## Install

Into the app's environment, from the app's folder:

```powershell
.venv\Scripts\python.exe -m pip install "liminal-plugin-french @ git+https://github.com/pcxmac-dev/liminal-plugin-french@v1.1.0"
```

or with the app's plugins (`pip install -e ".[plugins]"` in liminal). The app loads it on its next
start.

## Compatibility

It is written for plugin API 1.4 (`PUBLISHER.api`: datasets declared by a publisher). An app
offering 1.4 or a later 1.x loads it; an app of another major, or one older than 1.4, leaves it out
and says why on the Plugins view.

## Develop

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install "liminal @ git+https://github.com/pcxmac-dev/liminal@feature/collector"
.venv\Scripts\python.exe -m pip install -e ".[dev]"
.venv\Scripts\python.exe -m pytest -q
```

Tests never send requests and never read your keys.
