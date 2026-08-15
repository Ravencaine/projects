---
title: "This terminal tool is my favorite way to view spreadsheets on my computer"
source: "https://share.google/tyIiaAJnUhv4Ikhtb"
author: "share.google"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Inspect spreadsheets natively inside your CLI workflow.

This terminal tool is my favorite way to view spreadsheets on my computer Close Close By Afam Onyimadu Published Mar 6, 2026, 3:00 PM EST Afam's experience in tech publishing dates back to 2018, when he worked for Make Tech Easier. Over the years, he has built a reputation for publishing high-quality guides, reviews, tips, and explainer articles, covering Windows, Linux, and open source tools. His work has been featured on top websites, including Technical Ustad, Windows Report, Guiding Tech, Alphr, and Next of Windows. He holds a first degree in Computer Science and is a strong advocate for data privacy and security, with several tips, videos, and tutorials on the subject published on the Fuzo Tech YouTube channel. When he is not working, he loves to spend time with his family, cycling, or tending to his garden. Sign in to your MakeUseOf account One of the most distracting actions in a terminal-heavy workflow is opening a spreadsheet in Excel, Google Sheets, or LibreOffice. Even if you only need a quick peek, it breaks focus. I have been searching for a spreadsheet tool that integrates perfectly with my terminal workflow, but despite trying many — cat , CSV exports, Pandas scripts, and even csvlook — none were quite the right fit. The ideal tool will be fast, interactive, and able to handle Excel files natively. I recently tried xleak, and it comes closest to what I need. My main reservation is that it's quite new and doesn't have as many releases as some competitors. However, it's surprisingly polished and comes with a rich interactive Terminal User Interface (TUI). It's now one of my top ways of opening Excel files . Opening spreadsheets disrupted my terminal workflow The price of constant switching to a GUI Afam Onyimadu / MUO When I work on the terminal, I'm often forced to open a GUI because a terminal command points to a file. These switches typically don't last more than a few seconds to just under a minute. As soon as I get the value I want, I return to the terminal. The drawback is that when you have to do this several times a day, reorienting yourself each time you return to the terminal starts to take a toll. Several quick fixes are limited. An example is cat on Unix, which simply outputs raw file contents (bytes) to the terminal without formatting. csvlook only works if my data is a CSV file. VisiData is one I really liked, but it's primarily built as an Excel viewer. They fell short on full .xlsx navigation, formula support, and interactive features. Below is how xleak compares to other tools I tried: Tool Formats Interactive Terminal native Instant preview cat Any No Yes No csvlook CSV only No Yes Yes Pandas Many No No Requires scripting VisiData CSV, TSV, JSON, SQLite, xlsx + more Yes Yes Yes, but cluttered xleak xlsx, xls, xlsm, xlsb, ods Yes — Full TUI Yes Yes Installing xleak is straightforward on every major platform Package managers and binaries make setup painless Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Close Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Installation was much easier than I expected. I'm currently running xleak on Windows 11; the PowerShell command below gave me the fastest install route:  The command will download the latest GitHub release. You don't need any Windows package managers for this process. Xleak installed in under thirty seconds after running the command. If you prefer package managers, you can use Scoop; that process first requires adding the bucket, then running the install command, both listed below:  For anyone on macOS or Linux, Homebrew gives the cleanest install path:  Once you install xleak, you may want to run the commands below. Using the first command, you get a non-interactive preview, but the second exposes the full interactive TUI of xleak:  The interactive TUI is what makes xleak feel like a real tool Navigation, search, and formula inspection work as expected Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Close Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Afam Onyimadu / MUO Using the TUI convinced me that xleak would be a perfect fit for my workflow. I use the Tab key to navigate between sheets in my documents. For cell navigation, I use the arrow keys, and hitting Enter opens up a cell, displaying full cell details. These details include the cell name, type, column name, cell content, and underlying formula. Searching cells is also straightforward. I hit the forward slash key " / " on my keyboard, then type the search term. Copying is equally intuitive. I use c to copy the current cell, C to copy an entire row, and when I work on larger files, I add the -H flag to enable horizontal scrolling and auto-size columns. This flag ensures that a wide spreadsheet doesn't get truncated. The themes also make a difference. You can choose the Default theme or one of the following: Dracula, Solarized Dark, Solarized Light, GitHub Dark, and Nord. Themes make the terminal feel less boring, and it helps if you have to work for extended periods. xleak Price model Free Xleak is a fast, open-source terminal-based spreadsheet viewer that lets you interact with Excel files (.xlsx, .xls, .csv, etc.) directly in the terminal. See at GitHub Expand Collapse xleak handles exports and named tables better than I expected Piping spreadsheet data into CLI tools is genuinely useful Afam Onyimadu / MUO Xleak's export flags fit naturally into scripting workflows. When I need to pull a table from a workbook and quickly run aggregations on it, it takes two simple steps. First, I run the command below to see the named tables in my workbook, and once I identify the table, I extract it using the --table flag and export it as a CSV. Below are the two commands needed:  I can then pipe it into awk , and this process on xleak is faster than doing the actual steps

## Code / Examples

```
irm https://github.com/bgreenwell/xleak/releases/latest/download/xleak-installer.ps1 | iex
```
```
scoop bucket add bgreenwell https://github.com/bgreenwell/scoop-bucketscoop install xleak
```
```
brew install bgreenwell/tap/xleak
```
```
xleak MYFILE.xlsxxleak MYFILE.xlsx -i
```
```
xleak workbook.xlsx --list-tablesxleak workbook.xlsx --table Named_Table --export csv > sales.csv
```


---
*Source: [share.google](https://share.google/tyIiaAJnUhv4Ikhtb)*
