"""What the plugin attaches to (plugin API 2.2, apis.py): the library's card is sound, names the files the plugin
really reads (its datasets' own addresses) among the library's others, and every address on it is the library's own.
The page check (each address asked once) runs only with LIMINAL_VENDOR_PAGES=1, the weekly CI run's; nothing is sent
otherwise. The user, 2026-11-11: "each plugin should reflect the the API its attached to, and present links that
provide documentation"."""
from __future__ import annotations

import os
from datetime import date
from urllib.parse import urlsplit

import pytest

from liminal_libs.sources.apis import dead_links, problems, urls

import plugin_integrator_french as french
from plugin_integrator_french.apis import APIS, LIBRARY, LIBRARY_API


def test_the_card_is_sound_and_is_the_plugins():
    assert problems(APIS, today=date(2026, 11, 11)) == []
    assert french.PUBLISHER.apis == APIS and french.FrenchLibrary.apis is APIS
    assert LIBRARY_API.docs == LIBRARY and LIBRARY_API.verified == "2026-11-11" and LIBRARY_API.kind == "feed"
    assert french.PUBLISHER.interface()["apis"] == ["Kenneth R. French Data Library"]
    assert french.PUBLISHER.api_facts() == {}  # it learns nothing while it runs: the app reads its files


def test_the_card_names_the_files_the_plugin_really_reads():
    """Each call it makes is one of its datasets' files (by its address under the card's base), and each of those
    files is a call on the card; the library's other files and sections follow, not used."""
    read = {url for d in french.DATASETS for url, _ in d.files(date(2026, 11, 11))}
    assert {LIBRARY_API.base + c.name.removeprefix("GET ") for c in LIBRARY_API.used} == read
    assert LIBRARY_API.base == french.FRENCH and len(LIBRARY_API.used) == len(french.DATASETS) == 4
    areas = {a.name for a in LIBRARY_API.areas}
    assert all(c.area in areas for c in LIBRARY_API.calls)  # every call is in a part of the library
    assert {a.name for a in LIBRARY_API.covered} == {"Fama/French 3 factors", "Fama/French 5 factors (2x3)",
                                                     "Industry portfolios"}
    assert len(LIBRARY_API.areas) > len(LIBRARY_API.covered) and len(LIBRARY_API.calls) > len(LIBRARY_API.used)
    assert not any(c.writes or c.costs for c in LIBRARY_API.calls)  # files read, nothing changed, nothing billed


def test_every_address_is_the_librarys_own():
    assert {urlsplit(u).hostname for u in urls(APIS)} == {"mba.tuck.dartmouth.edu"}


@pytest.mark.skipif(not os.environ.get("LIMINAL_VENDOR_PAGES"),
                    reason="LIMINAL_VENDOR_PAGES=1 asks each address on the card (the weekly CI run)")
def test_every_address_on_the_card_answers():
    assert dead_links(APIS) == []
