"""What the plugin attaches to (plugin API 2.2, liminal_libs.sources.apis), as the library's own pages describe it
(read 2026-11-11): Kenneth R. French's Data Library, zipped CSV and text files on the library's server, every section
of the library named (the four files the plugin reads first, the rest of the library after them). The user,
2026-11-11: "each plugin should reflect the the API its attached to, and present links that provide documentation
... it should also expose more of what the API is about"."""
from __future__ import annotations

from liminal_libs.sources.apis import Api, Area, Call, Link

HOME = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/"
LIBRARY = HOME + "data_library.html"
DETAILS = HOME + "Data_Library/"
FILES = HOME + "ftp/"  # the library's files (the plugin's FRENCH)
VERIFIED = "2026-11-11"  # the day these facts were read from the library's pages

DAILY_3 = "F-F_Research_Data_Factors_daily_CSV.zip"
MONTHLY_3 = "F-F_Research_Data_Factors_CSV.zip"
DAILY_5 = "F-F_Research_Data_5_Factors_2x3_daily_CSV.zip"
DAILY_49 = "49_Industry_Portfolios_daily_CSV.zip"
THREE = "Fama/French 3 factors"
FIVE = "Fama/French 5 factors (2x3)"
INDUSTRIES = "Industry portfolios"
MOMENTUM = "Momentum and reversal factors"

LIBRARY_API = Api(
    name="Kenneth R. French Data Library",
    maker="Kenneth R. French (Tuck School of Business, Dartmouth)",
    about=("A researcher's own library of stock returns for research: the Fama/French factors, U.S. portfolios sorted on "
           "size, value, profitability, investment, momentum and other characteristics, industry portfolios, "
           "breakpoints, and the same for developed and emerging markets, each a zipped CSV or text file on the "
           "library's server. It is files, not a query API: each file is replaced in place when the library revises its "
           "history from new CRSP data, and missing values are written -99.99 or -999."),
    kind="feed",
    base=FILES,
    version="the zipped CSV files (a header row, then YYYYMMDD or YYYYMM rows, an annual table after the monthly one)",
    auth="none: public files",
    limits=("none published; the plugin keeps its own: at most 20 requests a day, an hour apart at least, each "
            "dataset fetched again every 30 days"),
    costs="",
    links=(
        Link("Data Library", LIBRARY, "docs"),
        Link("Fama/French 3 factors: details", DETAILS + "f-f_factors.html", "reference"),
        Link("Fama/French 5 factors (2x3): details", DETAILS + "f-f_5_factors_2x3.html", "reference"),
        Link("49 industry portfolios: details", DETAILS + "det_49_ind_port.html", "reference"),
        Link("Changes in CRSP data", DETAILS + "changes_crsp.html", "changelog"),
        Link("Fama/French 3 factors: historical archives", DETAILS + "f-f_factors_archive.html", "reference"),
    ),
    areas=(
        Area(THREE, "the market, size (SMB) and value (HML) factors and the risk-free rate, daily, weekly and monthly "
                    "from 1926", DETAILS + "f-f_factors.html",
             covered="french-3-factors-daily and french-3-factors-monthly"),
        Area(FIVE, "the 3 factors with profitability (RMW) and investment (CMA), daily and monthly from 1963",
             DETAILS + "f-f_5_factors_2x3.html", covered="french-5-factors-daily"),
        Area(INDUSTRIES, "5, 10, 12, 17, 30, 38, 48 and 49 industry portfolios, value- and equal-weighted, daily and "
                         "monthly", DETAILS + "det_49_ind_port.html",
             covered="the 49 industries' value-weighted daily returns (french-49-industries-daily)"),
        Area("Univariate sorts", "portfolios formed on size, book-to-market, operating profitability, investment, "
                                 "earnings/price, cashflow/price and dividend yield", DETAILS + "det_port_form_sz.html"),
        Area("Bivariate sorts", "6, 25 and 100 portfolios formed on size and book-to-market, profitability or "
                                "investment, and on pairs of the others", DETAILS + "six_portfolios.html"),
        Area("Three-way sorts", "32 portfolios formed on size, book-to-market, profitability and investment",
             DETAILS + "32_ports_me_beme_op.html"),
        Area(MOMENTUM, "the momentum (Mom), short-term reversal and long-term reversal factors, daily and monthly, and "
                       "the portfolios formed on them", DETAILS + "det_mom_factor.html"),
        Area("Other characteristics", "portfolios formed on accruals, market beta, net share issues, variance and "
                                      "residual variance", DETAILS + "det_port_form_AC.html"),
        Area("Breakpoints", "the NYSE breakpoints of market equity, book-to-market, profitability, investment, E/P, "
                            "CF/P, D/P and prior 2-12 month returns", DETAILS + "det_me_breakpoints.html"),
        Area("Historical book equity", "the U.S. book equity data the sorts use, a file of its own",
             LIBRARY + "#BookEquity"),
        Area("Benchmark factors and portfolios", "the Fama/French benchmark factors and portfolios, kept as history",
             LIBRARY + "#HistBenchmarks"),
        Area("Developed markets", "3 and 5 factors, momentum and portfolios for developed markets, Europe, Japan, Asia "
                                  "Pacific ex Japan and North America", DETAILS + "f-f_3developed.html"),
        Area("Emerging markets", "5 factors, momentum and portfolios for emerging markets",
             DETAILS + "f-f_5emerging.html"),
    ),
    calls=(
        Call("GET " + DAILY_3, "the 3 factors and the risk-free rate, daily from 1926", THREE,
             used="french-3-factors-daily", docs=DETAILS + "f-f_factors.html"),
        Call("GET " + MONTHLY_3, "the 3 factors monthly from 1926, then an annual table", THREE,
             used="french-3-factors-monthly (its monthly table)", docs=DETAILS + "f-f_factors.html"),
        Call("GET " + DAILY_5, "the 5 factors and the risk-free rate, daily from 1963", FIVE,
             used="french-5-factors-daily", docs=DETAILS + "f-f_5_factors_2x3.html"),
        Call("GET " + DAILY_49, "the 49 industries' daily returns, value- then equal-weighted", INDUSTRIES,
             used="french-49-industries-daily (its value-weighted table)", docs=DETAILS + "det_49_ind_port.html"),
        Call("GET F-F_Research_Data_5_Factors_2x3_CSV.zip", "the 5 factors monthly from 1963", FIVE,
             docs=DETAILS + "f-f_5_factors_2x3.html"),
        Call("GET F-F_Research_Data_Factors_weekly_CSV.zip", "the 3 factors weekly", THREE,
             docs=DETAILS + "f-f_factors.html"),
        Call("GET 49_Industry_Portfolios_CSV.zip", "the 49 industries monthly", INDUSTRIES,
             docs=DETAILS + "det_49_ind_port.html"),
        Call("GET F-F_Momentum_Factor_daily_CSV.zip", "the momentum factor, daily", MOMENTUM,
             docs=DETAILS + "det_mom_factor_daily.html"),
        Call("GET F-F_Momentum_Factor_CSV.zip", "the momentum factor, monthly", MOMENTUM,
             docs=DETAILS + "det_mom_factor.html"),
        Call("GET ME_Breakpoints_CSV.zip", "the NYSE market-equity breakpoints", "Breakpoints",
             docs=DETAILS + "det_me_breakpoints.html"),
        Call("GET Developed_3_Factors_CSV.zip", "the developed markets' 3 factors, monthly", "Developed markets",
             docs=DETAILS + "f-f_3developed.html"),
        Call("GET Emerging_5_Factors_CSV.zip", "the emerging markets' 5 factors, monthly", "Emerging markets",
             docs=DETAILS + "f-f_5emerging.html"),
    ),
    verified=VERIFIED,
)

APIS = (LIBRARY_API,)
