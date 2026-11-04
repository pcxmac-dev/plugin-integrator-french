"""The Ken French plugin, run against the library installed beside it: its tables read, its class on
the plugin contract, and the app loading it from this package with its own version and the datasets
it declared as a built-in."""
from __future__ import annotations

from datetime import date, datetime, timezone
from importlib.metadata import version

from liminal_libs.sources import publishers, registry
from liminal_libs.sources.dataset import ms
from liminal_libs.sources.publisher import PublisherPlugin

import plugin_integrator_french as french
from plugin_integrator_french import FrenchLibrary, parse_french

FRENCH_DAILY = """This file was created by CMPT_ME_BEME_RETS_DAILY using the 202608 CRSP database.
The Tbill return is the simple daily rate.

,Mkt-RF,SMB,HML,RF
19260701,    0.10,   -0.25,   -0.27,    0.01
19260702,    0.45,   -0.33,   -0.06,    0.01
19260706,  -99.99,    0.12,   -0.11,    0.01

Copyright 2026 Kenneth R. French
"""

FRENCH_MONTHLY = """This file was created by CMPT_ME_BEME_RETS using the 202608 CRSP database.

,Mkt-RF,SMB,HML,RF
192607,    2.89,   -2.55,   -2.39,    0.22
192608,    2.64,   -1.14,    3.81,    0.25

 Annual Factors: January-December
,Mkt-RF,SMB,HML,RF
1927,   29.47,   -2.04,   -3.81,    3.12
"""

INDUSTRIES = """  Average Equal Weighted Returns -- Daily
,Agric,Food ,Soda
19260701,    9.99,    9.99,    9.99

  Average Value Weighted Returns -- Daily
,Agric,Food ,Soda
19260701,    0.56,   -0.12,  -99.99
19260702,    1.20,    0.34,    0.10
"""


def test_french_tables():
    daily = parse_french("x.CSV", FRENCH_DAILY.encode())
    assert daily.series["Mkt-RF"] == ("Mkt-RF", "%", "day")
    mkt = [(ts, v) for s, ts, v in daily.values if s == "Mkt-RF"]
    assert [v for _, v in mkt] == [0.10, 0.45]  # -99.99 is the library's missing value
    assert mkt[0][0] == int(datetime(1926, 7, 1, 4, tzinfo=timezone.utc).timestamp() * 1000)  # ET midnight
    monthly = parse_french("x.CSV", FRENCH_MONTHLY.encode())
    assert {s: f for s, (_, _, f) in monthly.series.items()} == {"Mkt-RF": "month", "SMB": "month", "HML": "month", "RF": "month"}
    assert len(monthly.values) == 8  # the annual table after it is left out
    vw = parse_french("x.CSV", INDUSTRIES.encode(), section="Average Value Weighted Returns")
    assert sorted(vw.series) == ["Agric", "Food", "Soda"]
    assert ("Agric", vw.values[0][1], 0.56) in vw.values and not any(v == 9.99 for *_, v in vw.values)


def test_it_is_a_class_on_the_plugin_contract():
    """The publisher is an instance of its class (plugin API 2.0), what it declares its class's
    attributes, its hooks the contract's defaults; the app loads it as that class."""
    p = french.PUBLISHER
    assert type(p) is FrenchLibrary and issubclass(FrenchLibrary, PublisherPlugin) and not p.is_record
    assert p.api == "2.0" and FrenchLibrary.api == "2.0" and p.KIND == "publisher"
    assert not p.has_moments and not p.has_calendar and not p.reads_itself and not p.has_settings
    assert p.moments(date(2026, 11, 3)) == () and p.calendar(date(2026, 11, 3)) == []  # the contract's defaults
    assert FrenchLibrary.datasets is french.DATASETS and p.datasets == french.DATASETS
    moved = p.with_(order=1)  # a changed copy, the registry's way (its origin and version)
    assert type(moved) is FrenchLibrary and moved.order == 1 and p.order == 400 and moved.datasets == p.datasets
    registry.reload()
    loaded = publishers()["french"]
    assert type(loaded) is FrenchLibrary and loaded.api == "2.0" and loaded.version == version("plugin-integrator-french")
    assert registry.api_refusal(loaded.api, record=loaded.is_record) is None
    assert not [why for where, why in registry.errors() if "french" in where or "french" in why]


def test_the_app_loads_it_from_this_package_with_its_own_version():
    registry.reload()
    p = publishers().get("french")
    assert p is not None, dict(registry.errors())
    assert p.origin in {"package: plugin-integrator-french (plugin_integrator_french:PUBLISHER)", "plugins/plugin-integrator-french (plugin_integrator_french:PUBLISHER)"}  # its package, or its checkout in the workspace\'s plugin directory
    assert p.version == version("plugin-integrator-french") and french.PUBLISHER.version == ""
    assert registry.api_refusal(p.api) is None and p.api == "2.0"
    assert not [why for where, why in registry.errors() if "french" in where or "french" in why]
    assert (p.title, p.kind, p.feeds) == ("Ken French Data Library", "research", ())
    assert [d.name for d in p.datasets] == ["french-3-factors-daily", "french-3-factors-monthly",
                                            "french-5-factors-daily", "french-49-industries-daily"]
    assert {d.provider for d in p.datasets} == {"french"} and p.policy.hosts == ("mba.tuck.dartmouth.edu",)
    files = [url for d in p.datasets for url, _ in d.files(date(2026, 11, 1))]
    assert all(url.startswith(french.FRENCH) and url.endswith("_CSV.zip") for url in files) and len(files) == 4
    # the library's revisions come about two months after a month: a first import is dated the 15th after
    assert p.datasets[0].published(ms(date(2026, 8, 31))) == ms(date(2026, 10, 15))
