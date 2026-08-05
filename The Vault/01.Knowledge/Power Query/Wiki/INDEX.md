---
created: 2026-07-26
updated: 2026-08-02
note_type: index
tags: [powerquery, m-code, index]
---

# Power Query — Knowledge Base Index

This is the index for the Power Query knowledge base. 825 notes grouped by type.

## Core Concepts  (635 notes)

| Note | Description |
|------|-------------|
| [[Import-Stock-Data.md]] | Import and Prep Stock Data (Power Query)

Load stock price data from Investing.com into Power BI and shape it for time p |
| [[Import-Theme-JSON.md]] | Import Theme JSON with Custom Fonts (Power Query)

Export a Power BI theme, edit the JSON to add custom font families, a |
| [[QUESTIONS.md]] | Open Questions

(None yet — questions surface here after ingestion, health checks, or during note-writing.)

Open questi |
| [[Set-Data-Category-Image-URL.md]] | Set Data Category to Image URL (Power Query)

When a column contains public web URLs pointing to images (PNG, JPG, SVG), |
| [[about.md]] | About

Placeholder stub for Related content fragment. |
| [[access_database.md]] | Access.Database

Returns a structural representation of an Access database, database. |
| [[accesscontrolkind_type.md]] | AccessControlKind.Type

Signature

```m

``` |
| [[activedirectory_domains.md]] | ActiveDirectory.Domains

Returns a list of Active Directory domains in the same forest as the specified domain or of the |
| [[adobeanalytics_cubes.md]] | AdobeAnalytics.Cubes

Returns a table of multidimensional packages from Adobe Analytics. |
| [[adodotnet_datasource.md]] | AdoDotNet.DataSource

Returns the schema collection for the ADO.NET data source with provider name providerName and conn |
| [[adodotnet_query.md]] | AdoDotNet.Query

Returns the result of running query with the connection string connectionString using the ADO.NET provi |
| [[age.md]] | Age

Placeholder stub for Related content fragment. |
| [[analysisservices_database.md]] | AnalysisServices.Database

Returns a table of multidimensional cubes or tabular models from the Analysis Services databa |
| [[analysisservices_databases.md]] | AnalysisServices.Databases

Returns databases on an Analysis Services instance, server. |
| [[azurestorage_blobcontents.md]] | AzureStorage.BlobContents

Returns the content of the blob at the URL, url, from an Azure storage vault. |
| [[azurestorage_blobs.md]] | AzureStorage.Blobs

Returns a navigational table containing a row for each container found at the account URL, account,  |
| [[azurestorage_datalake.md]] | AzureStorage.DataLake

Returns a navigational table containing the documents found in the specified container and its su |
| [[azurestorage_datalakecontents.md]] | AzureStorage.DataLakeContents

Returns the content of the file at the URL, url, from an Azure Data Lake Storage filesyst |
| [[azurestorage_tables.md]] | AzureStorage.Tables

Returns a navigational table containing a row for each table found at the account URL, account, fro |
| [[binary_approximatelength.md]] | Binary.ApproximateLength

Returns the approximate length of binary, or an error if the data source doesn't support an ap |
| [[binary_buffer.md]] | Binary.Buffer

Buffers the binary value in memory. |
| [[binary_combine.md]] | Binary.Combine

Combines a list of binaries into a single binary. |
| [[binary_compress.md]] | Binary.Compress

Compresses a binary value using the given compression type. |
| [[binary_decompress.md]] | Binary.Decompress

Decompresses a binary value using the given compression type. |
| [[binary_from.md]] | Binary.From

Returns a binary value from the given value. |
| [[binary_infercontenttype.md]] | Binary.InferContentType

Returns a record with field Content.Type that contains the inferred MIME-type. |
| [[binary_length.md]] | Binary.Length

Returns the number of characters. |
| [[binary_range.md]] | Binary.Range

Returns a subset of the binary value beginning at the offset binary. |
| [[binary_view.md]] | Binary.View

Returns a view of binary where the functions specified in handlers are used in lieu of the default behavior |
| [[binaryencoding_type.md]] | BinaryEncoding.Type

Signature

```m

``` |
| [[binaryformat_byte.md]] | BinaryFormat.Byte

A binary format that reads an 8-bit unsigned integer. |
| [[binaryformat_byteorder.md]] | BinaryFormat.ByteOrder

Returns a binary format with the byte order specified by binaryFormat. |
| [[binaryformat_choice.md]] | BinaryFormat.Choice

Returns a binary format that chooses the next binary format based on a value that has already been  |
| [[binaryformat_decimal.md]] | BinaryFormat.Decimal

A binary format that reads a .NET 16-byte decimal value. |
| [[binaryformat_double.md]] | BinaryFormat.Double

A binary format that reads an 8-byte IEEE double-precision floating point value. |
| [[binaryformat_length.md]] | BinaryFormat.Length

Returns a binary format that limits the amount of data that can be read. |
| [[binaryformat_null.md]] | BinaryFormat.Null

A binary format that reads zero bytes and returns null. |
| [[binaryformat_signedinteger16.md]] | BinaryFormat.SignedInteger16

A binary format that reads a 16-bit signed integer. |
| [[binaryformat_signedinteger32.md]] | BinaryFormat.SignedInteger32

A binary format that reads a 32-bit signed integer. |
| [[binaryformat_signedinteger64.md]] | BinaryFormat.SignedInteger64

A binary format that reads a 64-bit signed integer. |
| [[binaryformat_single.md]] | BinaryFormat.Single

A binary format that reads a 4-byte IEEE single-precision floating point value. |
| [[binaryformat_unsignedinteger16.md]] | BinaryFormat.UnsignedInteger16

A binary format that reads a 16-bit unsigned integer. |
| [[binaryformat_unsignedinteger32.md]] | BinaryFormat.UnsignedInteger32

A binary format that reads a 32-bit unsigned integer. |
| [[binaryformat_unsignedinteger64.md]] | BinaryFormat.UnsignedInteger64

A binary format that reads a 64-bit unsigned integer. |
| [[binaryoccurrence_type.md]] | BinaryOccurrence.Type

Signature

```m

``` |
| [[buffermode_type.md]] | BufferMode.Type

Signature

```m

``` |
| [[byte_from.md]] | Byte.From

Returns an 8-bit integer number value from the given value. |
| [[byteorder_type.md]] | ByteOrder.Type

Signature

```m

``` |
| [[cdm_contents.md]] | Cdm.Contents

This function is unavailable in the current context. |
| [[chen-python-power-query-source.md]] | Python in Power Query — Mark Chen

> Type: practical guide / intermediate
> Author: Mark Chen
> Published: 2026-05-21
>  |
| [[python-script-in-power-query.md]] | Running Python Scripts Inside Power Query

Power Query allows Python scripts to run directly inside Power Query — the table is passed as a pandas DataFrame called `dataset`. No external scripts, no file imports. Extended with a Holt-Winters forecasting example. |
| [[combiner_combinetextbydelimiter.md]] | Combiner.CombineTextByDelimiter

Returns a function that combines a list of text values into a single text value using t |
| [[combiner_combinetextbyeachdelimiter.md]] | Combiner.CombineTextByEachDelimiter

Returns a function that combines a list of text values into a single text value usi |
| [[combiner_combinetextbylengths.md]] | Combiner.CombineTextByLengths

Returns a function that combines a list of text values into a single text value using the |
| [[combiner_combinetextbypositions.md]] | Combiner.CombineTextByPositions

Returns a function that combines a list of text values into a single text value using t |
| [[combiner_combinetextbyranges.md]] | Combiner.CombineTextByRanges

Returns a function that combines a list of text values into a single text value using the  |
| [[comparer_equals.md]] | Comparer.Equals

Returns a logical value based on the equality check over the two given values, x and y, using the provi |
| [[comparer_fromculture.md]] | Comparer.FromCulture

Returns a comparer function that uses the culture and the case-sensitivity specified by ignoreCase |
| [[comparer_ordinal.md]] | Comparer.Ordinal

Returns a comparer function which uses Ordinal rules to compare the provided values x and y. |
| [[comparer_ordinalignorecase.md]] | Comparer.OrdinalIgnoreCase

Returns a case-insensitive comparer function which uses Ordinal rules to compare the provide |
| [[comparison_criteria.md]] | Comparison criteria

An optional value used by list and table functions to control equality testing and ordering. |
| [[compression_deflate.md]] | Compression.Deflate

Signature

```m

``` |
| [[compression_gzip.md]] | Compression.GZip

Signature

```m

``` |
| [[compression_type.md]] | Compression.Type

Signature

```m

``` |
| [[compute_scorevector.md]] | Compute.ScoreVector

Signature

```m

``` |
| [[csv_document.md]] | Csv.Document

Returns the contents of the CSV document as a table. |
| [[csvstyle_type.md]] | CsvStyle.Type

Signature

```m

``` |
| [[cube_attributememberid.md]] | Cube.AttributeMemberId

Returns the unique member identifier from a member property value. |
| [[cube_attributememberproperty.md]] | Cube.AttributeMemberProperty

Returns the property propertyName of dimension attribute attribute. |
| [[cube_dimensions.md]] | Cube.Dimensions

Returns a table containing the set of available dimensions within the cube. |
| [[cube_displayfolders.md]] | Cube.DisplayFolders

Returns a nested tree of tables representing the display folder hierarchy of the objects (for examp |
| [[cube_measureproperties.md]] | Cube.MeasureProperties

Returns a table containing the set of available properties for measures that are expanded in the |
| [[cube_measureproperty.md]] | Cube.MeasureProperty

Returns the property propertyName of measure measure. |
| [[cube_measures.md]] | Cube.Measures

Returns a table containing the set of available measures within the cube. |
| [[cube_properties.md]] | Cube.Properties

Returns a table containing the set of available properties for dimensions that are expanded in the cube |
| [[cube_propertykey.md]] | Cube.PropertyKey

Returns the key of property property. |
| [[cube_replacedimensions.md]] | Cube.ReplaceDimensions

Replaces the set of dimensions returned by Cube.Dimensions. |
| [[culture_and_text_formatting.md]] | Culture and Text Formatting in M

M's text formatting is culture-aware. |
| [[culture_current.md]] | Culture.Current

Signature

```m

``` |
| [[currency_from.md]] | Currency.From

Returns a currency value from the given value. |
| [[date_adddays.md]] | Date.AddDays

Returns the date, datetime, or datetimezone result from adding numberOfDays days to the datetime value dat |
| [[date_addmonths.md]] | Date.AddMonths

Returns the date, datetime, or datetimezone result from adding numberOfMonths months to the datetime val |
| [[date_addquarters.md]] | Date.AddQuarters

Returns the date, datetime, or datetimezone result from adding numberOfQuarters quarters to the dateti |
| [[date_addweeks.md]] | Date.AddWeeks

Returns the date, datetime, or datetimezone result from adding numberOfWeeks weeks to the datetime value  |
| [[date_addyears.md]] | Date.AddYears

Returns the date, datetime, or datetimezone result of adding numberOfYears to a datetime value dateTime. |
| [[date_day.md]] | Date.Day

Returns the day component of a date, datetime, or datetimezone value. |
| [[date_dayofweek.md]] | Date.DayOfWeek

Returns a number (from 0 to 6) indicating the day of the week of the provided dateTime. |
| [[date_dayofweekname.md]] | Date.DayOfWeekName

Returns the day of the week name for the provided date. |
| [[date_dayofyear.md]] | Date.DayOfYear

Returns a number representing the day of the year in the provided date, datetime, or datetimezone value, |
| [[date_daysinmonth.md]] | Date.DaysInMonth

Returns the number of days in the month in the date, datetime, or datetimezone value dateTime. |
| [[date_endofday.md]] | Date.EndOfDay

Returns the end of the day represented by dateTime. |
| [[date_endofmonth.md]] | Date.EndOfMonth

Returns the end of the month that contains dateTime. |
| [[date_endofquarter.md]] | Date.EndOfQuarter

Returns the end of the quarter that contains dateTime. |
| [[date_endofweek.md]] | Date.EndOfWeek

Returns the end of the week that contains dateTime. |
| [[date_endofyear.md]] | Date.EndOfYear

Returns the end of the year that contains dateTime, including fractional seconds. |
| [[date_from.md]] | Date.From

Returns a date value from the given value. |
| [[date_isincurrentday.md]] | Date.IsInCurrentDay

Indicates whether the given datetime value dateTime occurs during the current day, as determined by |
| [[date_isincurrentmonth.md]] | Date.IsInCurrentMonth

Indicates whether the given datetime value dateTime occurs during the current month, as determine |
| [[date_isincurrentquarter.md]] | Date.IsInCurrentQuarter

Indicates whether the given datetime value dateTime occurs during the current quarter, as deter |
| [[date_isincurrentweek.md]] | Date.IsInCurrentWeek

Indicates whether the given datetime value dateTime occurs during the current week, as determined  |
| [[date_isincurrentyear.md]] | Date.IsInCurrentYear

Indicates whether the given datetime value dateTime occurs during the current year, as determined  |
| [[date_isinnextday.md]] | Date.IsInNextDay

Indicates whether the given datetime value dateTime occurs during the next day, as determined by the c |
| [[date_isinnextmonth.md]] | Date.IsInNextMonth

Indicates whether the given datetime value dateTime occurs during the next month, as determined by t |
| [[date_isinnextndays.md]] | Date.IsInNextNDays

Indicates whether the given datetime value dateTime occurs during the next number of days, as determ |
| [[date_isinnextnmonths.md]] | Date.IsInNextNMonths

Signature

```m

``` |
| [[date_isinnextnquarters.md]] | Date.IsInNextNQuarters

Indicates whether the given datetime value dateTime occurs during the next number of quarters, a |
| [[date_isinnextnweeks.md]] | Date.IsInNextNWeeks

Indicates whether the given datetime value dateTime occurs during the next number of weeks, as dete |
| [[date_isinnextnyears.md]] | Date.IsInNextNYears

Indicates whether the given datetime value dateTime occurs during the next number of years, as dete |
| [[date_isinnextquarter.md]] | Date.IsInNextQuarter

Indicates whether the given datetime value dateTime occurs during the next quarter, as determined  |
| [[date_isinnextweek.md]] | Date.IsInNextWeek

Indicates whether the given datetime value dateTime occurs during the next week, as determined by the |
| [[date_isinnextyear.md]] | Date.IsInNextYear

Indicates whether the given datetime value dateTime occurs during the next year, as determined by the |
| [[date_isinpreviousday.md]] | Date.IsInPreviousDay

Indicates whether the given datetime value dateTime occurs during the previous day, as determined  |
| [[date_isinpreviousmonth.md]] | Date.IsInPreviousMonth

Indicates whether the given datetime value dateTime occurs during the previous month, as determi |
| [[date_isinpreviousndays.md]] | Date.IsInPreviousNDays

Indicates whether the given datetime value dateTime occurs during the previous number of days, a |
| [[date_isinpreviousnmonths.md]] | Date.IsInPreviousNMonths

Indicates whether the given datetime value dateTime occurs during the previous number of month |
| [[date_isinpreviousnquarters.md]] | Date.IsInPreviousNQuarters

Indicates whether the given datetime value dateTime occurs during the previous number of qua |
| [[date_isinpreviousnweeks.md]] | Date.IsInPreviousNWeeks

Indicates whether the given datetime value dateTime occurs during the previous number of weeks, |
| [[date_isinpreviousnyears.md]] | Date.IsInPreviousNYears

Indicates whether the given datetime value dateTime occurs during the previous number of years, |
| [[date_isinpreviousquarter.md]] | Date.IsInPreviousQuarter

Indicates whether the given datetime value dateTime occurs during the previous quarter, as det |
| [[date_isinpreviousweek.md]] | Date.IsInPreviousWeek

Indicates whether the given datetime value dateTime occurs during the previous week, as determine |
| [[date_isinpreviousyear.md]] | Date.IsInPreviousYear

Indicates whether the given datetime value dateTime occurs during the previous year, as determine |
| [[date_month.md]] | Date.Month

Returns the month component of the provided datetime value, dateTime. |
| [[date_monthname.md]] | Date.MonthName

Returns the name of the month component for the provided date. |
| [[date_quarterofyear.md]] | Date.QuarterOfYear

Returns a number from 1 to 4 indicating which quarter of the year the date dateTime falls in. |
| [[date_startofday.md]] | Date.StartOfDay

Returns the start of the day represented by dateTime. |
| [[date_startofmonth.md]] | Date.StartOfMonth

Returns the start of the month that contains dateTime. |
| [[date_startofquarter.md]] | Date.StartOfQuarter

Returns the start of the quarter that contains dateTime. |
| [[date_startofweek.md]] | Date.StartOfWeek

Returns the start of the week that contains dateTime. |
| [[date_startofyear.md]] | Date.StartOfYear

Returns the start of the year that contains dateTime. |
| [[date_weekofmonth.md]] | Date.WeekOfMonth

Returns a number from 1 to 6 indicating which week of the month the date dateTime falls in. |
| [[date_weekofyear.md]] | Date.WeekOfYear

Returns a number from 1 to 54 indicating which week of the year the date, dateTime, falls in. |
| [[date_year.md]] | Date.Year

Returns the year component of the provided datetime value, dateTime. |
| [[datetime_addzone.md]] | DateTime.AddZone

Adds timezone information to the dateTime value. |
| [[datetime_fixedlocalnow.md]] | DateTime.FixedLocalNow

Returns a datetime value set to the current date and time on the system. |
| [[datetime_from.md]] | DateTime.From

Returns a datetime value from the given value. |
| [[datetime_fromfiletime.md]] | DateTime.FromFileTime

Creates a datetime value from the fileTime value and converts it to the local time zone. |
| [[datetime_isincurrenthour.md]] | DateTime.IsInCurrentHour

Indicates whether the given datetime value dateTime occurs during the current hour, as determi |
| [[datetime_isincurrentminute.md]] | DateTime.IsInCurrentMinute

Indicates whether the given datetime value dateTime occurs during the current minute, as det |
| [[datetime_isincurrentsecond.md]] | DateTime.IsInCurrentSecond

Indicates whether the given datetime value dateTime occurs during the current second, as det |
| [[datetime_isinnexthour.md]] | DateTime.IsInNextHour

Indicates whether the given datetime value dateTime occurs during the next hour, as determined by |
| [[datetime_isinnextminute.md]] | DateTime.IsInNextMinute

Indicates whether the given datetime value dateTime occurs during the next minute, as determine |
| [[datetime_isinnextnhours.md]] | DateTime.IsInNextNHours

Indicates whether the given datetime value dateTime occurs during the next number of hours, as  |
| [[datetime_isinnextnminutes.md]] | DateTime.IsInNextNMinutes

Indicates whether the given datetime value dateTime occurs during the next number of minutes, |
| [[datetime_isinnextnseconds.md]] | DateTime.IsInNextNSeconds

Indicates whether the given datetime value dateTime occurs during the next number of seconds, |
| [[datetime_isinnextsecond.md]] | DateTime.IsInNextSecond

Indicates whether the given datetime value dateTime occurs during the next second, as determine |
| [[datetime_isinprevioushour.md]] | DateTime.IsInPreviousHour

Indicates whether the given datetime value dateTime occurs during the previous hour, as deter |
| [[datetime_isinpreviousminute.md]] | DateTime.IsInPreviousMinute

Indicates whether the given datetime value dateTime occurs during the previous minute, as d |
| [[datetime_isinpreviousnhours.md]] | DateTime.IsInPreviousNHours

Indicates whether the given datetime value dateTime occurs during the previous number of ho |
| [[datetime_isinpreviousnminutes.md]] | DateTime.IsInPreviousNMinutes

Indicates whether the given datetime value dateTime occurs during the previous number of  |
| [[datetime_isinpreviousnseconds.md]] | DateTime.IsInPreviousNSeconds

Indicates whether the given datetime value dateTime occurs during the previous number of  |
| [[datetime_isinprevioussecond.md]] | DateTime.IsInPreviousSecond

Indicates whether the given datetime value dateTime occurs during the previous second, as d |
| [[datetime_localnow.md]] | DateTime.LocalNow

Returns a datetime value set to the current date and time on the system. |
| [[datetime_time.md]] | DateTime.Time

Returns the time part of the given datetime value, dateTime. |
| [[datetimezone_fixedlocalnow.md]] | DateTimeZone.FixedLocalNow

Returns a datetime value set to the current date and time on the system. |
| [[datetimezone_fixedutcnow.md]] | DateTimeZone.FixedUtcNow

Returns the current date and time in UTC (the GMT timezone). |
| [[datetimezone_from.md]] | DateTimeZone.From

Creates a datetimezone from the given value. |
| [[datetimezone_fromfiletime.md]] | DateTimeZone.FromFileTime

Creates a datetimezone value from the fileTime value and converts it to the local time zone. |
| [[datetimezone_localnow.md]] | DateTimeZone.LocalNow

Returns a datetimezone value set to the current date and time on the system. |
| [[datetimezone_removezone.md]] | DateTimeZone.RemoveZone

Returns a #datetime value from dateTimeZone with timezone information removed. |
| [[datetimezone_switchzone.md]] | DateTimeZone.SwitchZone

Changes timezone information to on the datetimezone value dateTimeZone to the new timezone info |
| [[datetimezone_tolocal.md]] | DateTimeZone.ToLocal

Changes timezone information of the datetimezone value dateTimeZone to the local timezone informat |
| [[datetimezone_toutc.md]] | DateTimeZone.ToUtc

Changes timezone information of the datetime value dateTimeZone to the UTC or Universal Time timezon |
| [[datetimezone_utcnow.md]] | DateTimeZone.UtcNow

Returns the current date and time in UTC (the GMT timezone). |
| [[datetimezone_zonehours.md]] | DateTimeZone.ZoneHours

Returns the time zone hour component of a datetimezone value. |
| [[datetimezone_zoneminutes.md]] | DateTimeZone.ZoneMinutes

Returns the time zone minutes component of a datetimezone value. |
| [[day_type.md]] | Day.Type

Signature

```m

``` |
| [[db2_database.md]] | DB2.Database

Returns a table of SQL tables and views available in a Db2 database on server server in the database insta |
| [[decimal_from.md]] | Decimal.From

Returns a Decimal number value from the given value. |
| [[deltalake_metadata.md]] | DeltaLake.Metadata

Given a Delta Lake table, returns the log entries for that table. |
| [[deploy-vs-maintain-power-query-dax.md]] | Deploy vs Maintain: Power Query and DAX Trade-offs Over Time

Performance and speed aren't the only factors. |
| [[diagnostics_activityid.md]] | Diagnostics.ActivityId

Returns an opaque identifier for the currently-running evaluation. |
| [[diagnostics_correlationid.md]] | Diagnostics.CorrelationId

Returns an opaque identifier to correlate incoming requests with outgoing ones. |
| [[diagnostics_trace.md]] | Diagnostics.Trace

Writes a trace message, if tracing is enabled, and returns value. |
| [[directquerycapabilities_from.md]] | DirectQueryCapabilities.From

This function is intended for internal use only. |
| [[double_from.md]] | Double.From

Returns a Double number value from the given value. |
| [[duration_days.md]] | Duration.Days

Returns the days portion of duration. |
| [[duration_from.md]] | Duration.From

Returns the duration value from the given value. |
| [[duration_hours.md]] | Duration.Hours

Returns the hours portion of duration. |
| [[duration_minutes.md]] | Duration.Minutes

Returns the minutes portion of duration. |
| [[duration_seconds.md]] | Duration.Seconds

Returns the seconds portion of duration. |
| [[duration_support.md]] | Duration Support in Power Query M

M supports duration values representing a span of time. |
| [[duration_totaldays.md]] | Duration.TotalDays

Returns the total days spanned by duration. |
| [[duration_totalhours.md]] | Duration.TotalHours

Returns the total hours spanned by duration. |
| [[duration_totalminutes.md]] | Duration.TotalMinutes

Returns the total minutes spanned by duration. |
| [[duration_totalseconds.md]] | Duration.TotalSeconds

Returns the total seconds spanned by duration. |
| [[embedded_value.md]] | Embedded.Value

This function is intended for internal use only. |
| [[equation_criteria.md]] | Equation criteria

See: comparison_criteria |
| [[essbase_cubes.md]] | Essbase.Cubes

Returns a table of cubes grouped by Essbase server from an Essbase instance at APS server url. |
| [[excel_currentworkbook.md]] | Excel.CurrentWorkbook

Returns the contents of the current Excel workbook. |
| [[excel_workbook.md]] | Excel.Workbook

Returns the contents of the Excel workbook. |
| [[exchange.md]] | Exchange

Placeholder stub for Related content fragment. |
| [[exchange_contents.md]] | Exchange.Contents

Returns a table of contents from the Microsoft Exchange account mailboxAddress. |
| [[expression_constant.md]] | Expression.Constant

Returns the M source code representation of a constant value. |
| [[expression_evaluate.md]] | Expression.Evaluate

Returns the result of evaluating an M expression document, with the available identifiers that can  |
| [[expression_identifier.md]] | Expression.Identifier

Returns the M source code representation of an identifier name. |
| [[expressions_vs_values.md]] | Expressions vs Values

An expression is a recipe for computation; a value is the result. |
| [[extravalues_type.md]] | ExtraValues.Type

Signature

```m

``` |
| [[fabricai_prompt.md]] | FabricAI.Prompt

Returns the result of passing the specified input to an AI model. |
| [[fieldname.md]] | FieldName

Placeholder stub for Related content fragment. |
| [[file_contents.md]] | File.Contents

Returns the contents of the file, path, as binary. |
| [[fixing-data-structure-pq.md]] | Fixing Data Structure in Power Query

Common structural problems when importing data into Power BI: wrong headers, wrong |
| [[folder_contents.md]] | Folder.Contents

Returns a table containing a row for each folder and file found in the folder path. |
| [[folder_files.md]] | Folder.Files

Returns a table containing a row for each file found in the specified folder and all its subfolders. |
| [[geographypoint_from.md]] | GeographyPoint.From

Creates a record representing a geographic point from its constituent parts, such as longitude, lat |
| [[googleanalytics_accounts.md]] | GoogleAnalytics.Accounts

Returns Google Analytics accounts that are accessible from the current credential. |
| [[graph_nodes.md]] | Graph.Nodes

This function is intended for internal use only. |
| [[guid_from.md]] | Guid.From

Returns a Guid.Type value from the given value. |
| [[hdfs_contents.md]] | Hdfs.Contents

Returns a table containing a row for each folder and file found at the folder URL, url, from a Hadoop fil |
| [[hdfs_files.md]] | Hdfs.Files

Returns a table containing a row for each file found at the folder URL, url, and subfolders from a Hadoop fi |
| [[hdinsight_containers.md]] | HdInsight.Containers

Returns a navigational table containing a row for each container found at the account URL, account |
| [[hdinsight_contents.md]] | HdInsight.Contents

Returns a navigational table containing a row for each container found at the account URL, account,  |
| [[hdinsight_files.md]] | HdInsight.Files

Returns a table containing a row for each blob file found at the container URL, account, from an Azure  |
| [[identity_from.md]] | Identity.From

Creates an identity. |
| [[identity_ismemberof.md]] | Identity.IsMemberOf

Determines whether an identity is a member of an identity collection. |
| [[identityprovider_default.md]] | IdentityProvider.Default

The default identity provider for the current host. |
| [[information.md]] | Information

Placeholder stub for Related content fragment. |
| [[informix_database.md]] | Informix.Database

Returns a table of SQL tables and views available in an Informix database on server server in the dat |
| [[int16_from.md]] | Int16.From

Returns a 16-bit integer number value from the given value. |
| [[int32_from.md]] | Int32.From

Returns a 32-bit integer number value from the given value. |
| [[int64_from.md]] | Int64.From

Returns a 64-bit integer number value from the given value. |
| [[int8_from.md]] | Int8.From

Returns a signed 8-bit integer number value from the given value. |
| [[itemexpression_from.md]] | ItemExpression.From

Returns the abstract syntax tree (AST) for the body of function, normalized into an item expression |
| [[itemexpression_item.md]] | ItemExpression.Item

Signature

```m

``` |
| [[joinalgorithm_type.md]] | JoinAlgorithm.Type

Signature

```m

``` |
| [[joinkind_fullouter.md]] | JoinKind.FullOuter

Signature

```m

``` |
| [[joinkind_inner.md]] | JoinKind.Inner

Signature

```m

``` |
| [[joinkind_leftanti.md]] | JoinKind.LeftAnti

Signature

```m

``` |
| [[joinkind_leftouter.md]] | JoinKind.LeftOuter

Signature

```m

``` |
| [[joinkind_leftsemi.md]] | JoinKind.LeftSemi

Signature

```m

``` |
| [[joinkind_rightanti.md]] | JoinKind.RightAnti

Signature

```m

``` |
| [[joinkind_rightouter.md]] | JoinKind.RightOuter

Signature

```m

``` |
| [[joinkind_rightsemi.md]] | JoinKind.RightSemi

Signature

```m

``` |
| [[joinkind_type.md]] | JoinKind.Type

Signature

```m

``` |
| [[joinside_type.md]] | JoinSide.Type

Signature

```m

``` |
| [[json_document.md]] | Json.Document

Returns the content of the JSON document. |
| [[json_fromvalue.md]] | Json.FromValue

Produces a JSON representation of a given value value with a text encoding specified by encoding. |
| [[lazy_list_record_evaluation_gotcha.md]] | List and Record Literals Use Lazy Evaluation — Not Computed Until Accessed

When you write a list or record literal, the |
| [[lazy_vs_eager_evaluation.md]] | Lazy vs Eager Evaluation

M uses different evaluation strategies depending on the construct. |
| [[limitclausekind_type.md]] | LimitClauseKind.Type

Signature

```m

``` |
| [[list_accumulate.md]] | List.Accumulate

Accumulates a summary value from the items in the specified list using the accumulator. |
| [[list_alltrue.md]] | List.AllTrue

Returns true if all expressions in the list list are true. |
| [[list_alternate.md]] | List.Alternate

Returns a list comprised of all the odd numbered offset elements in a list. |
| [[list_anytrue.md]] | List.AnyTrue

Returns true if any expression in the list list is true. |
| [[list_average.md]] | List.Average

Returns the average value for the items in the list, list. |
| [[list_buffer.md]] | List.Buffer

Buffers the list list in memory. |
| [[list_combine.md]] | List.Combine

Takes a list of lists, lists, and merges them into a single new list. |
| [[list_conformtopagereader.md]] | List.ConformToPageReader

This function is intended for internal use only. |
| [[list_contains.md]] | List.Contains

Indicates whether the list contains the specified value. |
| [[list_containsall.md]] | List.ContainsAll

Indicates whether the list includes all the values from another list. |
| [[list_containsany.md]] | List.ContainsAny

Indicates whether the list contains any of the values from another list. |
| [[list_count.md]] | List.Count

Returns the number of items in the specified list. |
| [[list_covariance.md]] | List.Covariance

Returns the covariance between two lists, numberList1 and numberList2. |
| [[list_dates.md]] | List.Dates

Returns a list of date values of size count, starting at start. |
| [[list_datetimes.md]] | List.DateTimes

Returns a list of datetime values of size count, starting at start. |
| [[list_datetimezones.md]] | List.DateTimeZones

Returns a list of datetimezone values of size count, starting at start. |
| [[list_difference.md]] | List.Difference

Returns the items in list list1 that do not appear in list list2. |
| [[list_distinct.md]] | List.Distinct

Returns a list that contains all the values in the specified list with duplicates removed. |
| [[list_durations.md]] | List.Durations

Returns a list of count duration values, starting at start and incremented by the given duration step. |
| [[list_first.md]] | List.First

Returns the first item in the list list, or the optional default value, defaultValue, if the list is empty. |
| [[list_firstn.md]] | List.FirstN

If a number is specified, up to that many items are returned. |
| [[list_generate.md]] | List.Generate

Generates a list of values using the provided functions. |
| [[list_insertrange.md]] | List.InsertRange

Returns a new list produced by inserting the values in values into list at index. |
| [[list_intersect.md]] | List.Intersect

Returns the intersection of the list values found in the input list lists. |
| [[list_isdistinct.md]] | List.IsDistinct

Returns a logical value whether there are duplicates in the list list; true if the list is distinct, fa |
| [[list_isempty.md]] | List.IsEmpty

Returns true if the list, list, contains no values (length 0). |
| [[list_last.md]] | List.Last

Returns the last item in the specified list, or the optional default value if the list is empty. |
| [[list_lastn.md]] | List.LastN

Returns a list of the last item or items in the specified list. |
| [[list_matchesall.md]] | List.MatchesAll

Returns true if the condition function is satisfied by all of the values in the list, otherwise returns |
| [[list_matchesany.md]] | List.MatchesAny

Returns true if the condition function is satisfied by any of the values in the list, otherwise returns |
| [[list_max.md]] | List.Max

Returns the maximum item in the list or the optional default value if the list is empty. |
| [[list_maxn.md]] | List.MaxN

Returns the maximum value(s) in the specified list. |
| [[list_median.md]] | List.Median

Returns the median item of the list list. |
| [[list_min.md]] | List.Min

Returns the minimum item in the list list, or the optional default value default if the list is empty. |
| [[list_minn.md]] | List.MinN

Returns the minimum value(s) in the list, list. |
| [[list_mode.md]] | List.Mode

Returns the item that appears most frequently in list. |
| [[list_modes.md]] | List.Modes

Returns the items that appear most frequently in list. |
| [[list_nonnullcount.md]] | List.NonNullCount

Returns the number of non-null items in the list list. |
| [[list_numbers.md]] | List.Numbers

Returns a list of numbers given an initial value, count, and optional increment value. |
| [[list_percentile.md]] | List.Percentile

Returns one or more sample percentiles of the list list. |
| [[list_positionof.md]] | List.PositionOf

Returns the offset at which the specified value appears in a list. |
| [[list_positionofany.md]] | List.PositionOfAny

Returns the offset at which an item from the specified list of values appears in a list. |
| [[list_positions.md]] | List.Positions

Returns a list of offsets for the specified input list. |
| [[list_product.md]] | List.Product

Returns the product of the non-null numbers in the list, numbersList. |
| [[list_random.md]] | List.Random

Returns a list of random numbers between 0 and 1, given the number of values to generate and an optional se |
| [[list_range.md]] | List.Range

Returns a subset of list beginning at offset. |
| [[list_removefirstn.md]] | List.RemoveFirstN

Returns a list that removes the first element of list list. |
| [[list_removeitems.md]] | List.RemoveItems

Removes all occurrences of the given values in the list2 from list1. |
| [[list_removelastn.md]] | List.RemoveLastN

Returns a list that removes the last countOrCondition elements from the end of list list. |
| [[list_removematchingitems.md]] | List.RemoveMatchingItems

Removes all occurrences of the given values in list2 from the list list1. |
| [[list_removenulls.md]] | List.RemoveNulls

Removes all occurrences of "null" values in the list. |
| [[list_removerange.md]] | List.RemoveRange

Removes count values in the list starting at the specified position, index. |
| [[list_repeat.md]] | List.Repeat

Returns a list that is count repetitions of the original list, list. |
| [[list_replacematchingitems.md]] | List.ReplaceMatchingItems

Performs the given replacements to the list list. |
| [[list_replacerange.md]] | List.ReplaceRange

Replaces count values in the list with the list replaceWith, starting at specified position, index. |
| [[list_replacevalue.md]] | List.ReplaceValue

Searches a list of values, list, for the value oldValue and replaces each occurrence with the replace |
| [[list_reverse.md]] | List.Reverse

Returns a list with the values in the list list in reversed order. |
| [[list_select.md]] | List.Select

Returns the values from the specified list that match the selection condition. |
| [[list_single.md]] | List.Single

If there is only one item in the list list, returns that item. |
| [[list_singleordefault.md]] | List.SingleOrDefault

If there is only one item in the list list, returns that item. |
| [[list_skip.md]] | List.Skip

Returns a list that skips the first element of list list. |
| [[list_split.md]] | List.Split

Splits list into a list of lists where the first element of the output list is a list containing the first p |
| [[list_standarddeviation.md]] | List.StandardDeviation

Returns a sample based estimate of the standard deviation of the values in the list, numbersList |
| [[list_sum.md]] | List.Sum

Returns the sum of the non-null values in the list, list. |
| [[list_times.md]] | List.Times

Returns a list of time values of size count, starting at start. |
| [[list_union.md]] | List.Union

Takes a list of lists lists, unions the items in the individual lists and returns them in the output list. |
| [[list_zip.md]] | List.Zip

Takes a list of lists, lists, and returns a list of lists combining items at the same position. |
| [[logical_from.md]] | Logical.From

Returns a logical value from the given value. |
| [[m-code_pdf_source.md]] | Power Query M Language Reference

Official Microsoft documentation for the Power Query M formula language, covering the  |
| [[m_consolidated_grammar.md]] | M Language Specification — Consolidated Grammar

The M consolidated grammar defines the complete formal grammar of the P |
| [[m_evaluation_model.md]] | M Evaluation Model

M's evaluation model is similar to spreadsheet cell evaluation — expressions are evaluated in depend |
| [[m_if_expressions.md]] | If Expressions (Conditionals)

The if expression selects between two expressions based on a logical condition. |
| [[m_let_expressions.md]] | Let Expressions

A let expression assigns names to values and expressions, which are then used in a final expression aft |
| [[m_lexical_structure.md]] | M Lexical Structure

The lexical structure defines the valid textual representations in M: identifiers, keywords, litera |
| [[m_metadata.md]] | Metadata in M

Every M value can carry metadata — additional information stored in a metadata record. |
| [[m_operator_behaviour.md]] | M Operator Behaviour

M operators behave differently depending on the types of their operands. |
| [[m_operators.md]] | M Operators

M includes operators for arithmetic, comparison, logic, text, lists, and records. |
| [[m_operators_operand_dependent_meaning.md]] | Operators Have Operand-Dependent Meaning — Same Operator, Different Behaviour

M operators behave differently depending  |
| [[m_primitive_types.md]] | M Primitive Types

M defines 14 primitive types. |
| [[m_query_structure_let_in.md]] | M Query Structure — let…in

Every M query in Power Query follows the let…in pattern. |
| [[m_sections.md]] | Sections (Modularity)

Sections provide a modularity mechanism in M, allowing shared definitions to be grouped and named |
| [[m_standard_library.md]] | M Standard Library

M includes a standard library — a set of named values and functions available in every expression wi |
| [[m_type_system.md]] | M Type System

M has a rich type system. |
| [[missingfield_ignore.md]] | MissingField.Ignore

Signature

```m

``` |
| [[missingfield_type.md]] | MissingField.Type

Signature

```m

``` |
| [[missingfield_usenull.md]] | MissingField.UseNull

Signature

```m

``` |
| [[module_versions.md]] | Module.Versions

Returns a record of module versions for the current module and its dependencies. |
| [[mysql_database.md]] | MySQL.Database

Returns a table of SQL tables, views, and stored scalar functions available in a MySQL database on serve |
| [[number_abs.md]] | Number.Abs

Returns the absolute value of number. |
| [[number_acos.md]] | Number.Acos

Returns the arccosine of number. |
| [[number_asin.md]] | Number.Asin

Returns the arcsine of number. |
| [[number_atan.md]] | Number.Atan

Returns the arctangent of number. |
| [[number_atan2.md]] | Number.Atan2

Returns the angle, in radians, whose tangent is the quotient y/x of the two numbers y and x. |
| [[number_bitwiseand.md]] | Number.BitwiseAnd

Returns the result of performing a bitwise "And" operation between number1 and number2. |
| [[number_bitwisenot.md]] | Number.BitwiseNot

Returns the result of performing a bitwise "Not" operation on number. |
| [[number_bitwiseor.md]] | Number.BitwiseOr

Returns the result of performing a bitwise "Or" between number1 and number2. |
| [[number_bitwiseshiftleft.md]] | Number.BitwiseShiftLeft

Returns the result of performing a bitwise shift to the left on number1, by the specified numbe |
| [[number_bitwiseshiftright.md]] | Number.BitwiseShiftRight

Returns the result of performing a bitwise shift to the right on number1, by the specified num |
| [[number_bitwisexor.md]] | Number.BitwiseXor

Returns the result of performing a bitwise "XOR" (Exclusive-OR) between number1 and number2. |
| [[number_combinations.md]] | Number.Combinations

Returns the number of unique combinations from a list of items, setSize with specified combination  |
| [[number_cos.md]] | Number.Cos

Returns the cosine of the specified angle. |
| [[number_cosh.md]] | Number.Cosh

Returns the hyperbolic cosine of number. |
| [[number_epsilon.md]] | Number.Epsilon

Signature

```m

``` |
| [[number_exp.md]] | Number.Exp

Returns the result of raising e to the power of number (exponential function). |
| [[number_factorial.md]] | Number.Factorial

Returns the factorial of the number number. |
| [[number_from.md]] | Number.From

Returns a number value from the given value. |
| [[number_integerdivide.md]] | Number.IntegerDivide

Returns the integer portion of the result from dividing a number, number1, by another number, numb |
| [[number_iseven.md]] | Number.IsEven

Indicates if the value, number, is even by returning true if it is even, false otherwise. |
| [[number_isnan.md]] | Number.IsNaN

Indicates if the value is NaN (Not a number). |
| [[number_isodd.md]] | Number.IsOdd

Indicates if the value is odd. |
| [[number_ln.md]] | Number.Ln

Returns the natural logarithm of a number, number. |
| [[number_log.md]] | Number.Log

Returns the logarithm of a number, number, to the specified base base. |
| [[number_log10.md]] | Number.Log10

Returns the base 10 logarithm of a number, number. |
| [[number_mod.md]] | Number.Mod

Returns the remainder resulting from the integer division of number by divisor. |
| [[number_nan.md]] | Number.NaN

Signature

```m

``` |
| [[number_negativeinfinity.md]] | Number.NegativeInfinity

Signature

```m

``` |
| [[number_permutations.md]] | Number.Permutations

Returns the number of permutations that can be generated from a number of items, setSize, with a sp |
| [[number_pi.md]] | Number.PI

Signature

```m

``` |
| [[number_positiveinfinity.md]] | Number.PositiveInfinity

Signature

```m

``` |
| [[number_power.md]] | Number.Power

Returns the result of raising number to the power of power. |
| [[number_random.md]] | Number.Random

Returns a random number between 0 and 1. |
| [[number_randombetween.md]] | Number.RandomBetween

Returns a random number between bottom and top. |
| [[number_round.md]] | Number.Round

Returns the result of rounding number to the nearest number. |
| [[number_roundawayfromzero.md]] | Number.RoundAwayFromZero

Returns the result of rounding number based on the sign of the number. |
| [[number_rounddown.md]] | Number.RoundDown

Returns the result of rounding number down to the previous highest integer. |
| [[number_roundtowardzero.md]] | Number.RoundTowardZero

Returns the result of rounding number based on the sign of the number. |
| [[number_roundup.md]] | Number.RoundUp

Returns the result of rounding number up to the next highest integer. |
| [[number_sign.md]] | Number.Sign

Returns 1 for if number is a positive number, -1 if it is a negative number, and 0 if it is zero. |
| [[number_sin.md]] | Number.Sin

Returns the sine of number. |
| [[number_sinh.md]] | Number.Sinh

Returns the hyperbolic sine of number. |
| [[number_sqrt.md]] | Number.Sqrt

Returns the square root of number. |
| [[number_tan.md]] | Number.Tan

Returns the tangent of number. |
| [[number_tanh.md]] | Number.Tanh

Returns the hyperbolic tangent of number. |
| [[occurrence.md]] | Occurrence

Placeholder stub for Related content fragment. |
| [[occurrence_all.md]] | Occurrence.All

Signature

```m

``` |
| [[occurrence_type.md]] | Occurrence.Type

Signature

```m

``` |
| [[odata_feed.md]] | OData.Feed

Returns a table of OData feeds offered by an OData service from a uri serviceUri, headers headers. |
| [[odataomitvalues_type.md]] | ODataOmitValues.Type

Signature

```m

``` |
| [[odbc_datasource.md]] | Odbc.DataSource

Returns a table of SQL tables and views from the ODBC data source specified by the connection string co |
| [[odbc_inferoptions.md]] | Odbc.InferOptions

Returns the result of trying to infer SQL capbabilities with the connection string connectionString u |
| [[odbc_query.md]] | Odbc.Query

Returns the result of running query with the connection string connectionString using ODBC. |
| [[oledb_datasource.md]] | OleDb.DataSource

Returns a table of SQL tables and views from the OLE DB data source specified by the connection string |
| [[oledb_query.md]] | OleDb.Query

Returns the result of running query with the connection string connectionString using OLE DB. |
| [[oracle_database.md]] | Oracle.Database

Returns a table of SQL tables and views from the Oracle database on server server. |
| [[order_type.md]] | Order.Type

Signature

```m

``` |
| [[pad-3-digit-numbers-workflow.md]] | Pad 3-Digit Numbers in Mixed-Type Column

Steps to pad only 3-digit numbers to 4 digits in a column that also contains t |
| [[pdf_tables.md]] | Pdf.Tables

Returns any tables found in pdf. |
| [[percentage_from.md]] | Percentage.From

Returns a percentage value from the given value. |
| [[percentilemode_type.md]] | PercentileMode.Type

Signature

```m

``` |
| [[postgresql_database.md]] | PostgreSQL.Database

Returns a table of SQL tables and views available in a PostgreSQL database on server server in the  |
| [[power-query-5-core-components.md]] | Power Query Editor: 5 Core Components

Power Query Editor has five UI components that work together. |
| [[power-query-6-transformation-categories.md]] | Power Query: 6 Transformation Categories

Six major transformation types cover almost every data cleaning scenario. |
| [[power-query-advanced-editor.md]] | Power Query: Advanced Editor

Displays and allows editing of the underlying M language (Power Query Formula Language) co |
| [[power-query-applied-steps-repeatability.md]] | Power Query: Applied Steps and Repeatability

Applied Steps is what makes Power Query transformative — not just a cleani |
| [[power-query-choose-remove-columns.md]] | Power Query: Choose Columns / Remove Columns

Choose Columns

Keeps only the selected columns. |
| [[power-query-csv-from-folder.md]] | Power Query: Import CSV Files from a Folder

Loads all CSV files in a folder into a single query, enabling analysis acro |
| [[power-query-custom-function-text-analytics.md]] | Power Query Custom Function — Text Analytics API

Build a reusable Power Query M function to call Azure Cognitive Servic |
| [[power-query-data-catalog-search.md]] | Power Query: Data Catalog Search

A curated search of public data websites (Wikipedia, Census Bureau, etc.) that returns |
| [[power-query-dax-combined-usage-patterns.md]] | Six Rules for Using Power Query and DAX Together

Power Query and DAX are teammates, not rivals. |
| [[power-query-editor-janvi-source.md]] | Power Query Editor — Janvi Gupta

> Type: tutorial / beginner guide
> Author: Janvi Gupta
> Published: 2025-09-22
> URL: |
| [[power-query-expand-versus-extract.md]] | Table.ExpandRecordColumn and Table.ExpandListColumn

Two Power Query transforms for flattening nested data structures in |
| [[power-query-group-by-single-dual-triple-field.md]] | Power Query Group By: Single, Dual, and Triple Field Aggregation

Group By in Power Query aggregates data by one or more |
| [[power-query-group-by.md]] | Power Query: Group By

Groups rows by one or more columns and computes an aggregation (count, sum, average, etc.) for ea |
| [[power-query-import-json-from-web-api.md]] | Power Query: Import JSON from Web API — Multi-Level Expand

Power Query can pull data from any JSON REST API, handling n |
| [[power-query-import-multiple-csv-files-from-folder.md]] | Power Query: Import Multiple CSV Files from Folder

Power Query can combine all CSV files from a folder into a single qu |
| [[power-query-import-tables-from-web-pages.md]] | Power Query: Import Tables from Web Pages

Power Query can scrape HTML tables directly from any web page, automatically  |
| [[power-query-json-import.md]] | Power Query: Import JSON from URL

Imports nested JSON data from a web URL, expanding arrays and records into tabular fo |
| [[power-query-remove-duplicates.md]] | Power Query: Remove Duplicates

Removes duplicate rows from a table based on all visible columns or selected columns. |
| [[power-query-unpivot-columns.md]] | Table.Unpivot

Transforms columns into rows — converts a wide-format table into long format for analysis. |
| [[power-query-vs-dax-core-difference.md]] | Power Query vs DAX: Core Difference

Power Query and DAX both manipulate data, but they operate at completely different  |
| [[power-query-vs-dax-model-size-performance.md]] | Power Query vs DAX: Model Size and Performance Impact

Both tools affect model size and performance — but in opposite wa |
| [[power-query-workflow-process.md]] | Power Query: The Workflow Process

A repeatable four-step process for every data preparation task. |
| [[pq_text_case_sensitive_vs_power_bi_normalization.md]] | Text Comparison Is Case-Sensitive in M; Power BI Normalizes on Load

M's text comparison operators are always case-sensi |
| [[precision_type.md]] | Precision.Type

Signature

```m

``` |
| [[progress_datasourceprogress.md]] | Progress.DataSourceProgress

This function is intended for internal use only. |
| [[python-data-types-power-query.md]] | Python Data Types Don't Carry Into Power Query

Setting `astype()` in pandas inside a Python script does not preserve da |
| [[python-null-nan-handling-power-query.md]] | Handling Null/NaN Values in Power Query with Python

Pandas uses `NaN` (Not a Number) for missing values. |
| [[python-power-query-workflow-integration.md]] | Python in Power Query: Workflow Integration

How Python cleaning scripts fit into the broader Power Query ETL workflow. |
| [[python-script-in-power-query.md]] | Running Python Scripts Inside Power Query

Power BI allows Python scripts to run directly inside Power Query — the table |
| [[python-text-cleaning-power-query.md]] | Text Cleaning in Power Query with Python

pandas string methods for cleaning messy text data inside Power Query Python s |
| [[quoted_identifier_syntax.md]] | Quoted Identifier Syntax — #"Name with Spaces"

M identifiers cannot contain spaces normally. |
| [[quotestyle_type.md]] | QuoteStyle.Type

Signature

```m

``` |
| [[rankkind_type.md]] | RankKind.Type

Signature

```m

``` |
| [[record_addfield.md]] | Record.AddField

Adds a field to a record record, given the name of the field fieldName and the value value. |
| [[record_and_list_lookup.md]] | Record Field Lookup and List Item Access

M provides two primary access patterns: record field lookup with `[]` or `` an |
| [[record_combine.md]] | Record.Combine

Combines the records in the given records. |
| [[record_field.md]] | Record.Field

Returns the value of the specified field in the record. |
| [[record_fieldcount.md]] | Record.FieldCount

Returns the number of fields in the record record. |
| [[record_fieldnames.md]] | Record.FieldNames

Returns the names of the fields in the record record as text. |
| [[record_fieldordefault.md]] | Record.FieldOrDefault

Returns the value of the specified field field in the record record. |
| [[record_fieldvalues.md]] | Record.FieldValues

Returns a list of the field values in record record. |
| [[record_hasfields.md]] | Record.HasFields

Indicates whether the record record has the fields specified in fields, by returning a logical value ( |
| [[record_removefields.md]] | Record.RemoveFields

Returns a record that removes all the fields specified in list fields from the input record. |
| [[record_renamefields.md]] | Record.RenameFields

Returns a record after renaming fields in the input record to the new field names specified in list |
| [[record_reorderfields.md]] | Record.ReorderFields

Reorders the fields of a record to match the order of a list of field names. |
| [[record_selectfields.md]] | Record.SelectFields

Returns a record which includes only the fields specified in list fields from the input record. |
| [[relativeposition_type.md]] | RelativePosition.Type

Signature

```m

``` |
| [[replacer_replacevalue.md]] | Replacer.ReplaceValue

Replaces the old value in the original value with the new value. |
| [[roundingmode_type.md]] | RoundingMode.Type

Signature

```m

``` |
| [[salesforce_data.md]] | Salesforce.Data

Returns the objects on the Salesforce account provided in the credentials. |
| [[salesforce_reports.md]] | Salesforce.Reports

Returns the reports on the Salesforce account provided in the credentials. |
| [[sapbusinesswarehouse_cubes.md]] | SapBusinessWarehouse.Cubes

Returns a table of InfoCubes and queries grouped by InfoArea from an SAP Business Warehouse  |
| [[sapbusinesswarehouseexecutionmode_typ.md]] | SapBusinessWarehouseExecutionMode.Typ

Signature

```m

``` |
| [[saphana_database.md]] | SapHana.Database

Returns a table of multidimensional packages from the SAP HANA database server. |
| [[saphanadistribution_type.md]] | SapHanaDistribution.Type

Signature

```m

``` |
| [[saphanarangeoperator_type.md]] | SapHanaRangeOperator.Type

Signature

```m

``` |
| [[sharepoint_contents.md]] | SharePoint.Contents

Returns a table containing a row for each folder and document found at the specified SharePoint sit |
| [[sharepoint_files.md]] | SharePoint.Files

Returns a table containing a row for each document found at the specified SharePoint site, url, and su |
| [[sharepoint_tables.md]] | SharePoint.Tables

Returns a table containing a row for each List item found at the specified SharePoint list, url. |
| [[single_from.md]] | Single.From

Returns a Single number value from the given value. |
| [[soda_feed.md]] | Soda.Feed

Returns a table from the contents at the specified URL url formatted according to the SODA 2.0 API. |
| [[splitter_splitbynothing.md]] | Splitter.SplitByNothing

Returns a function that does no splitting, returning its argument as a single element list. |
| [[splitter_splittextbyanydelimiter.md]] | Splitter.SplitTextByAnyDelimiter

Returns a function that splits text into a list of text at any of the specified delimi |
| [[splitter_splittextbycharactertransition.md]] | Splitter.SplitTextByCharacterTransition

Returns a function that splits text into a list of text according to a transiti |
| [[splitter_splittextbydelimiter.md]] | Splitter.SplitTextByDelimiter

Returns a function that splits text into a list of text according to the specified delimi |
| [[splitter_splittextbyeachdelimiter.md]] | Splitter.SplitTextByEachDelimiter

Returns a function that splits text into a list of text at each specified delimiter i |
| [[splitter_splittextbylengths.md]] | Splitter.SplitTextByLengths

Returns a function that splits text into a list of text by each specified length. |
| [[splitter_splittextbypositions.md]] | Splitter.SplitTextByPositions

Returns a function that splits text into a list of text at each specified position. |
| [[splitter_splittextbyranges.md]] | Splitter.SplitTextByRanges

Returns a function that splits text into a list of text according to the specified offsets a |
| [[splitter_splittextbyrepeatedlengths.md]] | Splitter.SplitTextByRepeatedLengths

Returns a function that splits text into a list of text after the specified length  |
| [[splitter_splittextbywhitespace.md]] | Splitter.SplitTextByWhitespace

Returns a function that splits text into a list of text at whitespace. |
| [[sql-equijoin-vs-cartesian-product.md]] | Equijoin in SQL: Cartesian Product vs. |
| [[sql-equijoin-vs-cartesian.md]] | Cartesian Product

When querying multiple tables in SQL, the WHERE clause is not optional: omitting it produces a Cartes |
| [[sql-select-syntax-reference.md]] | SQL SELECT Syntax: FROM, WHERE, GROUP BY, HAVING, ORDER BY

Complete reference for the SQL SELECT statement syntax used  |
| [[sql-syntax-reference.md]] | SQL Syntax Reference

Standard SQL SELECT statement structure as used in PowerPivot/Excel SQL queries. |
| [[sql_database.md]] | Sql.Database

Returns a table of SQL tables, views, and stored functions from the SQL Server database database on server |
| [[sql_databases.md]] | Sql.Databases

Returns a table of databases on the specified SQL server, server. |
| [[sqlexpression_schemafrom.md]] | SqlExpression.SchemaFrom

This function is intended for internal use only. |
| [[sqlexpression_toexpression.md]] | SqlExpression.ToExpression

Converts the provided sql query to M code, with the available identifiers defined by environ |
| [[standard_date_and_time_format_strings.md]] | Standard Date and Time Format Strings

Standard format specifiers for date/time values include: `d` (short date), `D` (l |
| [[standard_numeric_format_strings.md]] | Standard Numeric Format Strings

Standard format strings in M use single-letter format specifiers with optional precisio |
| [[summarize_this_article_for_me.md]] | Summarize this article for me

Placeholder stub for Related content fragment. |
| [[sybase_database.md]] | Sybase.Database

Returns a table of SQL tables and views available in a Sybase database on server server in the database |
| [[table_addkey.md]] | Table.AddKey

Adds a key to table, where columns is the list of column names that define the key, and isPrimary specifie |
| [[table_buffer.md]] | Table.Buffer

Buffers a table in memory, isolating it from external changes during evaluation. |
| [[table_combine.md]] | Table.Combine

Returns a table that is the result of merging a list of tables, tables. |
| [[table_conformtopagereader.md]] | Table.ConformToPageReader

This function is intended for internal use only. |
| [[table_contains.md]] | Table.Contains

Indicates whether the specified record, row, appears as a row in the table. |
| [[table_containsall.md]] | Table.ContainsAll

Indicates whether all the specified records in the list of records rows, appear as rows in the table. |
| [[table_containsany.md]] | Table.ContainsAny

Indicates whether any the specified records in the list of records rows, appear as rows in the table. |
| [[table_demoteheaders.md]] | Table.DemoteHeaders

Demotes the column headers (i.e. |
| [[table_distinct.md]] | Table.Distinct

Removes duplicate rows from the table. |
| [[table_filldown.md]] | Table.FillDown

Returns a table from the table specified where the value of a previous cell is propagated to the null-va |
| [[table_fillup.md]] | Table.FillUp

Returns a table from the table specified where the value of the next cell is propagated to the null-valued |
| [[table_first.md]] | Table.First

Returns the first row of the table or an optional default value, default, if the table is empty. |
| [[table_firstn.md]] | Table.FirstN

Returns the first row(s) of the table table, depending on the value of countOrCondition: If countOrConditi |
| [[table_firstvalue.md]] | Table.FirstValue

Returns the first column of the first row of the table table or a specified default value. |
| [[table_frompartitions.md]] | Table.FromPartitions

Returns a table that is the result of combining a set of partitioned tables, partitions. |
| [[table_fromrecords.md]] | Table.FromRecords

Converts a specified list of records into a table. |
| [[table_fromvalue.md]] | Table.FromValue

Creates a table with a column containing the provided value or list of values, value. |
| [[table_fuzzyjoin.md]] | Table.FuzzyJoin

Joins the rows of table1 with the rows of table2 based on a fuzzy matching of the values of the key col |
| [[table_fuzzynestedjoin.md]] | Table.FuzzyNestedJoin

Joins the rows of table1 with the rows of table2 based on a fuzzy matching of the values of the k |
| [[table_isdistinct.md]] | Table.IsDistinct

Indicates whether the table contains only distinct rows (no duplicates). |
| [[table_isempty.md]] | Table.IsEmpty

Indicates whether the table contains any rows. |
| [[table_join.md]] | Table.Join

Joins the rows of table1 with the rows of table2 based on the equality of the values of the key columns sele |
| [[table_keys.md]] | Table.Keys

Returns the keys of the specified table. |
| [[table_last.md]] | Table.Last

Returns the last row of the table or an optional default value, default, if the table is empty. |
| [[table_lastn.md]] | Table.LastN

Returns the last row(s) from the table, table, depending on the value of countOrCondition: If countOrCondit |
| [[table_literal_syntax.md]] | Table Literal Syntax — #table()

Tables in M have no direct literal syntax. |
| [[table_max.md]] | Table.Max

Returns the largest row in the table, given the comparisonCriteria. |
| [[table_maxn.md]] | Table.MaxN

Returns the largest row(s) in the table, given the comparisonCriteria. |
| [[table_min.md]] | Table.Min

Returns the smallest row in the table, given the comparisonCriteria. |
| [[table_minn.md]] | Table.MinN

Returns the smallest row(s) in the table, given the comparisonCriteria. |
| [[table_nestedjoin.md]] | Table.NestedJoin

Joins the rows of table1 with the rows of table2 based on the equality of the values of the key column |
| [[table_partition.md]] | Table.Partition

Partitions the table into a list of groups number of tables, based on the value of the column and a has |
| [[table_partitionkey.md]] | Table.PartitionKey

Returns the partition key of the specified table. |
| [[table_partitionvalues.md]] | Table.PartitionValues

Returns information about how a table is partitioned. |
| [[table_positionof.md]] | Table.PositionOf

Returns the row position of the first occurrence of the row in the table specified. |
| [[table_positionofany.md]] | Table.PositionOfAny

Returns the row(s) position(s) from the table of the first occurrence of the list of rows. |
| [[table_profile.md]] | Table.Profile

Returns a profile for the columns in table. |
| [[table_promoteheaders.md]] | Table.PromoteHeaders

Promotes the first row of values as the new column headers (i.e. |
| [[table_range.md]] | Table.Range

Returns the rows from the table starting at the specified offset. |
| [[table_removefirstn.md]] | Table.RemoveFirstN

Returns a table that does not contain the first specified number of rows, countOrCondition, of the t |
| [[table_removelastn.md]] | Table.RemoveLastN

Returns a table that does not contain the last countOrCondition rows of the table table. |
| [[table_repeat.md]] | Table.Repeat

Returns a table with the rows from the input table repeated the specified count times. |
| [[table_replacekeys.md]] | Table.ReplaceKeys

Replaces the keys of the specified table. |
| [[table_replacepartitionkey.md]] | Table.ReplacePartitionKey

Replaces the partition key of the specified table. |
| [[table_replacerelationshipidentity.md]] | Table.ReplaceRelationshipIdentity

This function is intended for internal use only. |
| [[table_replacevalue.md]] | Table.ReplaceValue

Replaces a value with a new value in the specified columns of a table. |
| [[table_schema.md]] | Table.Schema

Returns a table describing the columns of table. |
| [[table_skip.md]] | Table.Skip

Returns a table that does not contain the first specified number of rows, countOrCondition, of the table tab |
| [[table_split.md]] | Table.Split

Splits table into a list of tables where the first element of the list is a table containing the first page |
| [[table_splitat.md]] | Table.SplitAt

Signature

```m

``` |
| [[table_stopfolding.md]] | Table.StopFolding

Prevents any downstream operations from being run against the original source of the data in table. |
| [[table_torecords.md]] | Table.ToRecords

Converts a table, table, to a list of records. |
| [[table_transpose.md]] | Table.Transpose

Makes columns into rows and rows into columns. |
| [[table_view.md]] | Table.View

Returns a view of table where the functions specified in handlers are used in lieu of the default behavior o |
| [[tables_getrelationships.md]] | Tables.GetRelationships

Gets the relationships among a set of tables. |
| [[teradata_database.md]] | Teradata.Database

Returns a table of SQL tables and views from the Teradata database on server server. |
| [[text_afterdelimiter.md]] | Text.AfterDelimiter

Returns the portion of text after the specified delimiter. |
| [[text_at.md]] | Text.At

Returns the character in the text value, text at position index. |
| [[text_beforedelimiter.md]] | Text.BeforeDelimiter

Returns the portion of text before the specified delimiter. |
| [[text_betweendelimiters.md]] | Text.BetweenDelimiters

Returns the portion of text between the specified startDelimiter and endDelimiter. |
| [[text_clean.md]] | Text.Clean

Returns a text value with all control characters of text removed. |
| [[text_combine.md]] | Text.Combine

Returns the result of combining the list of text values, texts, into a single text value. |
| [[text_contains.md]] | Text.Contains

Detects whether text contains the value substring. |
| [[text_end.md]] | Text.End

Returns a text value that is the last count characters of the text value text. |
| [[text_endswith.md]] | Text.EndsWith

Indicates whether the given text, text, ends with the specified value, substring. |
| [[text_format.md]] | Text.Format

Returns formatted text that is created by applying arguments from a list or record to a format string forma |
| [[text_from.md]] | Text.From

Returns the text representation of a specified value. |
| [[text_infernumbertype.md]] | Text.InferNumberType

Infers the granular number type (Int64.Type, Double.Type, and so on) of text. |
| [[text_infernumbertype_infers_the_granular_number_type_int64type_doubletype_and_so_on_of_a.md]] | Text.InferNumberType infers the granular number type (Int64, Double, etc.) of a value

See: text_infernumbertype |
| [[text_insert.md]] | Text.Insert

Returns the result of inserting text value newText into the text value text at position offset. |
| [[text_length.md]] | Text.Length

Returns the number of characters in the text text. |
| [[text_lower.md]] | Text.Lower

Returns the result of converting all characters in text to lowercase. |
| [[text_middle.md]] | Text.Middle

Returns count characters, or through the end of text; at the offset start. |
| [[text_newguid.md]] | Text.NewGuid

Returns a new, random globally unique identifier (GUID). |
| [[text_padend.md]] | Text.PadEnd

Returns a text value padded to length count by inserting spaces at the end of the text value text. |
| [[text_padstart.md]] | Text.PadStart

Returns a text value padded to length count by inserting spaces at the start of the text value text. |
| [[text_positionof.md]] | Text.PositionOf

Returns the position of the specified occurrence of the text value substring found in text. |
| [[text_positionofany.md]] | Text.PositionOfAny

Returns the first position of any character in the list characters that is found in text. |
| [[text_proper.md]] | Text.Proper

Returns the result of capitalizing only the first letter of each word in text value text. |
| [[text_range.md]] | Text.Range

Returns the substring from the text text found at the offset offset. |
| [[text_remove.md]] | Text.Remove

Returns a copy of the text value text with all the characters from removeChars removed. |
| [[text_removerange.md]] | Text.RemoveRange

Returns a copy of the text value text with all the characters from position offset removed. |
| [[text_repeat.md]] | Text.Repeat

Returns a text value composed of the input text text repeated count times. |
| [[text_replace.md]] | Text.Replace

Returns the result of replacing all occurrences of text value old in text value text with text value new. |
| [[text_replacerange.md]] | Text.ReplaceRange

Returns the result of removing a number of characters, count, from text value text beginning at posit |
| [[text_reverse.md]] | Text.Reverse

Reverses the provided text. |
| [[text_select.md]] | Text.Select

Returns a copy of the text value text with all the characters not in selectChars removed. |
| [[text_split.md]] | Text.Split

Returns a list of text values resulting from the splitting of a text value based on the specified delimiter. |
| [[text_splitany.md]] | Text.SplitAny

Returns a list of text values resulting from the splitting of a text value based on any character specifi |
| [[text_start.md]] | Text.Start

Returns the first count characters of text as a text value. |
| [[text_startswith.md]] | Text.StartsWith

Returns true if text value text starts with text value substring. |
| [[text_trim.md]] | Text.Trim

Returns the result of removing all leading and trailing characters from the specified text. |
| [[text_trimend.md]] | Text.TrimEnd

Returns the result of removing all trailing characters from the specified text. |
| [[text_trimstart.md]] | Text.TrimStart

Returns the result of removing all leadling characters from the specified text. |
| [[text_upper.md]] | Text.Upper

Returns the result of converting all characters in text to uppercase. |
| [[textencoding_ascii.md]] | TextEncoding.Ascii

Signature

```m

``` |
| [[textencoding_type.md]] | TextEncoding.Type

Signature

```m

``` |
| [[time_endofhour.md]] | Time.EndOfHour

Returns the end of the hour represented by dateTime, including fractional seconds. |
| [[time_endofhour_returns_the_end_of_the_hour.md]] | Time.EndOfHour returns the end of the hour

See: time_endofhour |
| [[time_from.md]] | Time.From

Returns a time value from the given value. |
| [[time_from_returns_a_time_value_from_a_value.md]] | Time.From returns a time value from a value

See: time_from |
| [[time_hour.md]] | Time.Hour

Returns the hour component of the provided time, datetime, or datetimezone value, dateTime. |
| [[time_hour_returns_an_hour_value_from_a_datetime_value.md]] | Time.Hour returns an hour value from a datetime value

See: time_hour |
| [[time_minute.md]] | Time.Minute

Returns the minute component of the provided time, datetime, or datetimezone value, dateTime. |
| [[time_minute_returns_a_minute_value_from_a_datetime_value.md]] | Time.Minute returns a minute value from a datetime value

See: time_minute |
| [[time_second.md]] | Time.Second

Returns the second component of the provided time, datetime, or datetimezone value, dateTime. |
| [[time_startofhour.md]] | Time.StartOfHour

Returns the start of the hour represented by dateTime. |
| [[timezone_current.md]] | TimeZone.Current

Signature

```m

``` |
| [[tracelevel_critical.md]] | TraceLevel.Critical

Signature

```m

``` |
| [[tracelevel_information.md]] | TraceLevel.Information

Signature

```m

``` |
| [[tracelevel_type.md]] | TraceLevel.Type

Signature

```m

``` |
| [[tracelevel_verbose.md]] | TraceLevel.Verbose

Signature

```m

``` |
| [[tracelevel_warning.md]] | TraceLevel.Warning

Signature

```m

``` |
| [[type_addtablekey.md]] | Type.AddTableKey

Adds a key to the given table type. |
| [[type_facets.md]] | Type.Facets

Returns a record containing the facets of type. |
| [[type_is.md]] | Type.Is

Determines if a value of type1 is always compatible with type2. |
| [[type_isnullable.md]] | Type.IsNullable

Returns true if a type is a nullable type; otherwise, false. |
| [[type_listitem.md]] | Type.ListItem

Returns an item type from a list type. |
| [[type_nonnullable.md]] | Type.NonNullable

Returns the non nullable type from the type. |
| [[type_recordfields.md]] | Type.RecordFields

Returns a record describing the fields of a record type. |
| [[type_replacefacets.md]] | Type.ReplaceFacets

Replaces the facets of type with the facets contained in the record facets. |
| [[type_replacetablekeys.md]] | Type.ReplaceTableKeys

Returns a new table type with all keys replaced by the specified list of keys. |
| [[type_replacetablepartitionkey.md]] | Type.ReplaceTablePartitionKey

Returns a new table type with the partition key replaced by the specified partition key. |
| [[type_tablekeys.md]] | Type.TableKeys

Returns the possibly empty list of keys for the given table type. |
| [[type_tablepartitionkey.md]] | Type.TablePartitionKey

Returns the partition key for the given table type if it has one. |
| [[type_tableschema.md]] | Type.TableSchema

Returns a table describing the columns of tableType. |
| [[type_union.md]] | Type.Union

Returns the union of the types in types. |
| [[types.md]] | Types

Placeholder stub for Related content fragment. |
| [[uri_buildquerystring.md]] | Uri.BuildQueryString

Assemble the record query into a URI query string, escaping characters as necessary. |
| [[uri_combine.md]] | Uri.Combine

Returns an absolute URI that is the combination of the input baseUri and relativeUri. |
| [[uri_escapedatastring.md]] | Uri.EscapeDataString

Encodes special characters in the input data according to the rules of RFC 3986. |
| [[uri_parts.md]] | Uri.Parts

Returns the parts of the input absoluteUri as a record, containing values such as Scheme, Host, Port, Path, Q |
| [[value_add.md]] | Value.Add

Returns the sum of value1 and value2. |
| [[value_alternates.md]] | Value.Alternates

Expresses alternate query plans within a query plan expression obtained through Value.Expression(Value |
| [[value_as.md]] | Value.As

Returns the value if it's compatible with the specified type. |
| [[value_compare.md]] | Value.Compare

Returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second. |
| [[value_divide.md]] | Value.Divide

Returns the result of dividing value1 by value2. |
| [[value_equals.md]] | Value.Equals

Returns true if value value1 is equal to value value2, false otherwise. |
| [[value_expression.md]] | Value.Expression

Returns an abstract syntax tree (AST) that represents the value's expression. |
| [[value_firewall.md]] | Value.Firewall

This function is intended for internal use only. |
| [[value_is.md]] | Value.Is

Determines whether a value is compatible with the specified type. |
| [[value_lineage.md]] | Value.Lineage

This function is intended for internal use only. |
| [[value_metadata.md]] | Value.Metadata

Returns a record containing the input's metadata. |
| [[value_multiply.md]] | Value.Multiply

Returns the product of multiplying value1 by value2. |
| [[value_nativequery.md]] | Value.NativeQuery

Evaluates query against target using the parameters specified in parameters and the options specified |
| [[value_nullableequals.md]] | Value.NullableEquals

Returns null if either argument value1, value2 is null, otherwise equivalent to Value.Equals. |
| [[value_optimize.md]] | Value.Optimize

When used within Value.Expression, if value represents a query that can be optimized, this function indi |
| [[value_removemetadata.md]] | Value.RemoveMetadata

Strips the input of metadata. |
| [[value_replacemetadata.md]] | Value.ReplaceMetadata

Replaces the input's metadata information. |
| [[value_replacetype.md]] | Value.ReplaceType

Replaces the value's type with the provided type. |
| [[value_subtract.md]] | Value.Subtract

Returns the difference of value1 and value2. |
| [[value_traits.md]] | Value.Traits

This function is intended for internal use only. |
| [[value_type.md]] | Value.Type

Returns the type of the given value. |
| [[value_versionidentity.md]] | Value.VersionIdentity

Returns the version identity of the value, or null if it doesn't have a version. |
| [[value_versions.md]] | Value.Versions

Returns a navigation table containing the available versions of the value. |
| [[variable_value.md]] | Variable.Value

Returns the value of the specified variable identifier defined by the current evaluation environment. |
| [[variable_valueordefault.md]] | Variable.ValueOrDefault

Returns the value of the specified variable identifier defined by the current evaluation enviro |
| [[web_contents.md]] | Web.Contents

Returns the contents downloaded from url as binary. |
| [[web_headers.md]] | Web.Headers

Returns the headers downloaded from url as a record. |
| [[web_page.md]] | Web.Page

Returns the contents of the HTML document broken into its constituent structures, as well as a representation  |
| [[webaction_request.md]] | WebAction.Request

Creates an action that, when executed, will return the results of performing a method request against |
| [[webmethod_type.md]] | WebMethod.Type

Signature

```m

``` |
| [[xml_document.md]] | Xml.Document

Returns the contents of the XML document as a hierarchical table. |
| [[xml_tables.md]] | Xml.Tables

Returns the contents of the XML document as a nested collection of flattened tables. |

| [[five-benefits-single-formula-design.md]] | Five Benefits of Single-Formula Design

Efficiency, consistency, scalability, flexibility, and optimization from one-record-per-output design |
| [[multiple-calculations-single-formula-source.md]] | Multiple Calculations Single Formula Power Query — Source

Beginner tutorial: record literal syntax for multi-column output in one Power Query Custom Column step |
## Transformations  (72 notes)

| Note | Description |
|------|-------------|
| [[binaryformat_group.md]] | BinaryFormat.Group

The parameters are as follows: The binaryFormat parameter specifies the binary format of the key val |
| [[binaryformat_transform.md]] | BinaryFormat.Transform

Returns a binary format that will transform the values read by another binary format. |
| [[cube_addandexpanddimensioncolumn.md]] | Cube.AddAndExpandDimensionColumn

Merges the specified dimension table, dimensionSelector, into the filter context of th |
| [[cube_addmeasurecolumn.md]] | Cube.AddMeasureColumn

Adds a column with the name column to the cube that contains the results of the measure measureSe |
| [[cube_collapseandremovecolumns.md]] | Cube.CollapseAndRemoveColumns

Changes the dimensional granularity of the filter context for the cube by collapsing the  |
| [[cube_transform.md]] | Cube.Transform

Applies the list cube functions, transforms, on the cube. |
| [[groupkind_type.md]] | GroupKind.Type

Signature

```m

``` |
| [[list_sort.md]] | List.Sort

Sorts a list of data, list, according to the optional criteria specified. |
| [[list_transform.md]] | List.Transform

Returns a new list of values by applying the transform function transform to the list, list. |
| [[list_transformmany.md]] | List.TransformMany

Returns a list whose elements are projected from the input list. |
| [[record_transformfields.md]] | Record.TransformFields

Returns a record after applying transformations specified in list transformOperations to record. |
| [[rowexpression_column.md]] | RowExpression.Column

Returns an abstract syntax tree (AST) that represents access to column columnName of the row withi |
| [[rowexpression_from.md]] | RowExpression.From

Returns the abstract syntax tree (AST) for the body of function, normalized into a row expression: T |
| [[rowexpression_row.md]] | RowExpression.Row

Signature

```m

``` |
| [[table_addcolumn.md]] | Table.AddColumn

Adds a column named newColumnName to the table table. |
| [[table_addfuzzyclustercolumn.md]] | Table.AddFuzzyClusterColumn

Adds a new column newColumnName to table with representative values of columnName. |
| [[table_addindexcolumn.md]] | Table.AddIndexColumn

Appends a column named newColumnName to the table with explicit position values. |
| [[table_addjoincolumn.md]] | Table.AddJoinColumn

Joins the rows of table1 with the rows of table2 based on the equality of the values of the key col |
| [[table_addrankcolumn.md]] | Table.AddRankColumn

Appends a column named newColumnName to the table with the ranking of one or more other columns des |
| [[table_aggregatetablecolumn.md]] | Table.AggregateTableColumn

Aggregates tables in table[column] into multiple columns containing aggregate values for the |
| [[table_alternaterows.md]] | Table.AlternateRows

Keeps the initial offset then alternates taking and skipping the following rows. |
| [[table_approximaterowcount.md]] | Table.ApproximateRowCount

Returns the approximate number of rows in the table, or an error if the data source doesn't s |
| [[table_column.md]] | Table.Column

Returns the column of data specified by column from the table table as a list. |
| [[table_columncount.md]] | Table.ColumnCount

Returns the number of columns in the table table. |
| [[table_columnnames.md]] | Table.ColumnNames

Returns the column names in the table table as a list of text. |
| [[table_columnsoftype.md]] | Table.ColumnsOfType

Returns a list with the names of the columns from table table that match the types specified in lis |
| [[table_combinecolumns.md]] | Table.CombineColumns

Combines the specified columns into a new column using the specified combiner function. |
| [[table_combinecolumnstorecord.md]] | Table.CombineColumnsToRecord

Combines the specified columns of table into a new record-valued column named newColumnNam |
| [[table_duplicatecolumn.md]] | Table.DuplicateColumn

Duplicate the column named columnName to the table table. |
| [[table_expandlistcolumn.md]] | Table.ExpandListColumn

Given a table where column contains a list of values, splits the list into a row for each value. |
| [[table_expandrecordcolumn.md]] | Table.ExpandRecordColumn

Given the column of records in the input table, creates a table with a column for each field i |
| [[table_expandtablecolumn.md]] | Table.ExpandTableColumn

Expands tables in table[column] into multiple rows and columns. |
| [[table_filterwithdatatable.md]] | Table.FilterWithDataTable

This function is intended for internal use only. |
| [[table_fromcolumns.md]] | Table.FromColumns

Creates a table of type columns from a list lists containing nested lists with the column names and v |
| [[table_fromrows.md]] | Table.FromRows

Creates a table from the list rows where each element of the list is an inner list that contains the col |
| [[table_fuzzygroup.md]] | Table.FuzzyGroup

Groups the rows of table by fuzzily matching values in the specified column, key, for each row. |
| [[table_group.md]] | Table.Group

Groups the rows of table by the key columns defined by key. |
| [[table_hascolumns.md]] | Table.HasColumns

Indicates whether the table contains the specified column(s), columns. |
| [[table_insertrows.md]] | Table.InsertRows

Returns a table with the list of rows, rows, inserted into the table at the given position, offset. |
| [[table_matchesallrows.md]] | Table.MatchesAllRows

Indicates whether all the rows in the table match the given condition. |
| [[table_matchesanyrows.md]] | Table.MatchesAnyRows

Indicates whether any the rows in the table match the given condition. |
| [[table_pivot.md]] | Table.Pivot

Given a pair of columns representing attribute-value pairs, rotates the data in the attribute column into a |
| [[table_prefixcolumns.md]] | Table.PrefixColumns

Returns a table where all the column names from the table provided are prefixed with the given text |
| [[table_removecolumns.md]] | Table.RemoveColumns

Removes the specified columns from the table provided. |
| [[table_removematchingrows.md]] | Table.RemoveMatchingRows

Removes all occurrences of the specified rows from the table. |
| [[table_removerows.md]] | Table.RemoveRows

Removes count of rows from the beginning of the table, starting at the offset specified. |
| [[table_removerowswitherrors.md]] | Table.RemoveRowsWithErrors

Returns a table with the rows removed from the input table that contain an error in at least |
| [[table_renamecolumns.md]] | Table.RenameColumns

Performs the given renames to the columns in table table. |
| [[table_reordercolumns.md]] | Table.ReorderColumns

Returns a table from the input table, with the columns in the order specified by columnOrder. |
| [[table_replacematchingrows.md]] | Table.ReplaceMatchingRows

Replaces all the specified rows in the table with the provided ones. |
| [[table_replacerows.md]] | Table.ReplaceRows

Replaces a specified number of rows, count, in the input table with the specified rows, beginning aft |
| [[table_reverserows.md]] | Table.ReverseRows

Returns a table with the rows from the input table in reverse order. |
| [[table_rowcount.md]] | Table.RowCount

Returns the number of rows in the table. |
| [[table_selectcolumns.md]] | Table.SelectColumns

Returns the table with only the specified columns. |
| [[table_selectrows.md]] | Table.SelectRows

Returns a table of rows from the table, that matches the selection condition. |
| [[table_selectrowswitherrors.md]] | Table.SelectRowsWithErrors

Returns a table with only those rows of the input table that contain an error in at least on |
| [[table_singlerow.md]] | Table.SingleRow

Returns the single row in the one row table. |
| [[table_sort.md]] | Table.Sort

Sorts the table using the list of one or more column names and optional comparisonCriteria in the form { { c |
| [[table_splitcolumn.md]] | Table.SplitColumn

Splits the specified column into a set of additional columns using the specified splitter function. |
| [[table_tocolumns.md]] | Table.ToColumns

Creates a list of nested lists from the table, table. |
| [[table_torows.md]] | Table.ToRows

Creates a list of nested lists from the table, table. |
| [[table_transformcolumnnames.md]] | Table.TransformColumnNames

Transforms column names by using the given nameGenerator function. |
| [[table_transformcolumns.md]] | Table.TransformColumns

Transforms the specified table by applying each column operation in a list. |
| [[table_transformcolumntypes.md]] | Table.TransformColumnTypes

Returns a table by applying the transform operations to the specified columns using an optio |
| [[table_transformrows.md]] | Table.TransformRows

Creates a list by applying the transform operation to each row in table. |
| [[table_unpivot.md]] | Table.Unpivot

Translates a set of columns in a table into attribute-value pairs, combined with the rest of the values i |
| [[table_unpivotothercolumns.md]] | Table.UnpivotOtherColumns

Translates all columns other than a specified set into attribute-value pairs, combined with t |
| [[text-padstart-corrupts-mixed-columns.md]] | Text.PadStart Corrupts Mixed-Type Columns

Naive `Text.PadStart` on a column containing both numbers and text will prepe |
| [[transformation.md]] | Transformation

Placeholder stub for Related content fragment. |
| [[type_tablecolumn.md]] | Type.TableColumn

Returns the type of the column column in the table type tableType. |
| [[type_tablerow.md]] | Type.TableRow

Returns the row type of the specified table type. |
| [[web_browsercontents.md]] | Web.BrowserContents

Returns the HTML for the specified url, as viewed by a web browser. |

## M Functions & Reference  (69 notes)

| Note | Description |
|------|-------------|
| [[Build-Calendar-Table.md]] | Build a Calendar/Date Table (Power Query)

Create a dedicated date dimension table in Power Query. |
| [[Build-Period-Table.md]] | Build a Period Table (Power Query)

Create a static `Period` lookup table in Excel or Power Query to drive time period s |
| [[action_witherrorcontext.md]] | Action.WithErrorContext

This function is intended for internal use only. |
| [[binary_fromlist.md]] | Binary.FromList

Converts a list of numbers into a binary value. |
| [[binary_fromtext.md]] | Binary.FromText

Returns the result of converting text value text to a binary (list of number). |
| [[binary_tolist.md]] | Binary.ToList

Converts a binary value into a list of numbers. |
| [[binary_totext.md]] | Binary.ToText

Returns the result of converting a binary list of numbers binary into a text value. |
| [[binaryformat_binary.md]] | BinaryFormat.Binary

Returns a binary format that reads a binary value. |
| [[binaryformat_list.md]] | BinaryFormat.List

Returns a binary format that reads a sequence of items and returns a list. |
| [[binaryformat_record.md]] | BinaryFormat.Record

Returns a binary format that reads a record. |
| [[binaryformat_text.md]] | BinaryFormat.Text

Returns a binary format that reads a text value. |
| [[character_fromnumber.md]] | Character.FromNumber

Returns the character equivalent of the number. |
| [[character_tonumber.md]] | Character.ToNumber

Returns the number equivalent of the character. |
| [[date_fromtext.md]] | Date.FromText

Creates a date value from a textual representation. |
| [[date_isinyeartodate.md]] | Date.IsInYearToDate

Indicates whether the given datetime value dateTime occurs during the current year and is on or bef |
| [[date_torecord.md]] | Date.ToRecord

Returns a record containing the parts of the given date value, date. |
| [[date_totext.md]] | Date.ToText

Returns a textual representation of date. |
| [[datetime_date.md]] | DateTime.Date

Returns the date component of the dateTime parameter if the parameter is a date, datetime, or datetimezon |
| [[datetime_fromtext.md]] | DateTime.FromText

Creates a datetime value from a textual representation, text. |
| [[datetime_torecord.md]] | DateTime.ToRecord

Returns a record containing the parts of the given datetime value, dateTime. |
| [[datetime_totext.md]] | DateTime.ToText

Returns a textual representation of dateTime. |
| [[datetimezone_fromtext.md]] | DateTimeZone.FromText

Creates a datetimezone value from a textual representation, text. |
| [[datetimezone_torecord.md]] | DateTimeZone.ToRecord

Returns a record containing the parts of the given datetimezone value, dateTimeZone. |
| [[datetimezone_totext.md]] | DateTimeZone.ToText

Returns a textual representation of dateTimeZone. |
| [[deltalake_table.md]] | DeltaLake.Table

Returns the contents of the Delta Lake table. |
| [[duration_fromtext.md]] | Duration.FromText

Returns a duration value from the specified text, text. |
| [[duration_torecord.md]] | Duration.ToRecord

Returns a record containing the parts the duration value, duration. |
| [[duration_totext.md]] | Duration.ToText

Returns a textual representation in the form "day.hour:mins:sec" of the given duration value, duration. |
| [[error_record.md]] | Error.Record

Returns an error record from the provided text values for reason, mesage, detail, and error code. |
| [[excel_shapetable.md]] | Excel.ShapeTable

This function is intended for internal use only. |
| [[function_invokewitherrorcontext.md]] | Function.InvokeWithErrorContext

This function is intended for internal use only. |
| [[geography_fromwellknowntext.md]] | Geography.FromWellKnownText

Translates text representing a geographic value in Well-Known Text (WKT) format into a stru |
| [[geography_towellknowntext.md]] | Geography.ToWellKnownText

Translates a structured geographic point value into its Well-Known Text (WKT) representation  |
| [[geometry_fromwellknowntext.md]] | Geometry.FromWellKnownText

Translates text representing a geometric value in Well-Known Text (WKT) format into a struct |
| [[geometry_towellknowntext.md]] | Geometry.ToWellKnownText

Translates a structured geometric point value into its Well-Known Text (WKT) representation as |
| [[html_table.md]] | Html.Table

Returns a table containing the results of running the specified CSS selectors against the provided html. |
| [[lines_frombinary.md]] | Lines.FromBinary

Converts a binary value to a list of text values split at line breaks. |
| [[lines_fromtext.md]] | Lines.FromText

Converts a text value to a list of text values split at line breaks. |
| [[lines_tobinary.md]] | Lines.ToBinary

Converts a list of text into a binary value using the specified encoding and lineSeparator.The specified |
| [[lines_totext.md]] | Lines.ToText

Converts a list of text into a single text. |
| [[list_findtext.md]] | List.FindText

Returns a list of the values from the list list which contained the value text. |
| [[logical_fromtext.md]] | Logical.FromText

Creates a logical value from the text value text, either "true" or "false". |
| [[logical_totext.md]] | Logical.ToText

Creates a text value from the logical value logicalValue, either true or false. |
| [[number_encoded_in_text.md]] | Number encoded in text

Placeholder stub for Related content fragment. |
| [[number_fromtext.md]] | Number.FromText

Returns a number value from the given text value, text. |
| [[number_totext.md]] | Number.ToText

Converts the numeric value number to a text value according to the format specified by format. |
| [[rdata_frombinary.md]] | RData.FromBinary

Returns a record of data frames from the RData file. |
| [[record_fieldcount_returns_the_number_of_fields_in_a_record.md]] | Record.FieldCount returns the number of fields in a record

See: record_fieldcount |
| [[record_fromlist.md]] | Record.FromList

Returns a record given a list of field values and a set of fields. |
| [[record_fromtable.md]] | Record.FromTable

Returns a record from a table of records table containing field names and value names {[Name = name, V |
| [[record_hasfields_returns_true_if_the_field_name_or_field_names_are_present_in_a_record.md]] | Record.HasFields returns true if the field name or field names are present in a record

See: record_hasfields |
| [[record_tolist.md]] | Record.ToList

Returns a list of values containing the field values from the input record. |
| [[record_totable.md]] | Record.ToTable

Returns a table containing the columns Name and Value with a row for each field in record. |
| [[replacer_replacetext.md]] | Replacer.ReplaceText

Replaces the old text in the original text with the new text. |
| [[table_findtext.md]] | Table.FindText

Returns the rows in the table table that contain the text text. |
| [[table_fromlist.md]] | Table.FromList

Converts a list, list into a table by applying the optional splitting function, splitter, to each item i |
| [[table_tolist.md]] | Table.ToList

Converts a table into a list by applying the specified combining function to each row of values in the tab |
| [[table_witherrorcontext.md]] | Table.WithErrorContext

This function is intended for internal use only. |
| [[text_frombinary.md]] | Text.FromBinary

Decodes data from a binary value to a text value using the specified encoding type. |
| [[text_tobinary.md]] | Text.ToBinary

Encodes a text value into a binary value using the specified encoding. |
| [[text_tolist.md]] | Text.ToList

Returns a list of character values from the given text value text. |
| [[time_fromtext.md]] | Time.FromText

Creates a time value from a textual representation, text. |
| [[time_torecord.md]] | Time.ToRecord

Returns a record containing the parts of the given Time value, time. |
| [[time_totext.md]] | Time.ToText

Returns a textual representation of time. |
| [[type_closedrecord.md]] | Type.ClosedRecord

Returns a closed version of the given record type (or the same type, if it is already closed). |
| [[type_forrecord.md]] | Type.ForRecord

Returns a type that represents records with specific type constraints on fields. |
| [[type_isopenrecord.md]] | Type.IsOpenRecord

Returns a logical indicating whether a record type is open. |
| [[type_openrecord.md]] | Type.OpenRecord

Returns an opened version of the given record type (or the same type, if it is already opened). |
| [[value_fromtext.md]] | Value.FromText

Decodes a value from a textual representation and interprets it as a value with an appropriate type. |

| [[list-dates-m.md]] | List.Dates — M Date Series Generator

Generates a list of consecutive dates for Date Table construction |
| [[list-min-m.md]] | List.Min — M Minimum Aggregator

Returns the minimum value from a column; drives dynamic StartDate in Date Tables |
| [[list-max-m.md]] | List.Max — M Maximum Aggregator

Returns the maximum value from a column; drives dynamic EndDate in Date Tables |
| [[power-query-pbix-demo-download.md]] | Power Query PBIX Demo Download

Google Drive links for the sample CSV data and completed PBIX file |
| [[m-language-function-taxonomy.md]] | M Language Function Taxonomy

M function categories: Table, Text, Date/Duration, List, Record, Number, Logical, Specialized; immutable functional language |
| [[m-language-real-world-use-cases.md]] | M Language Real-World Use Cases

Data cleaning with Table.Distinct/Date.FromText, multi-source merge with Table.NestedJoin, custom parameterized functions |
## Python Integration  (6 notes)

| Note | Description |
|------|-------------|
| [[date_isleapyear.md]] | Date.IsLeapYear

Indicates whether the given datetime value dateTime falls in is a leap year. |
| [[formula-firewall-python-blocked.md]] | Formula Firewall: Why Python Scripts Only Work on Direct Queries

Power BI's Formula Firewall blocks Python scripts when |
| [[janvi-python-cleaning-magic-source.md]] | Python Cleaning Magic — Janvi Gupta

> Type: practical guide / beginner
> Author: Janvi Gupta
> Published: 2024-11-19
>  |
| [[name_description.md]] | name_description

Placeholder stub for fragment in Related content. |
| [[pandas-cumsum-vs-list-firstn.md]] | pandas cumsum() vs List.FirstN(): Cumulative Sums in Power Query

Power Query's M language has `List.FirstN()` for cumul |
| [[python-pandas-data-cleaning-patterns.md]] | Python Pandas Data Cleaning Patterns in Power Query

Common pandas operations for cleaning data inside Power Query's Pyt |

## Advanced Patterns  (42 notes)

| Note | Description |
|------|-------------|
| [[accesscontrolentry_conditiontoidentities.md]] | AccessControlEntry.ConditionToIdentities

Using the specified identityProvider, converts the condition into the list of  |
| [[binary_viewerror.md]] | Binary.ViewError

Creates a modified error record from errorRecord which won't trigger a fallback when raised by a handl |
| [[binary_viewfunction.md]] | Binary.ViewFunction

Creates a view function based on function that can be handled in a view created by Binary.View. |
| [[combiner_functions.md]] | Combiner functions

Combiner functions combine text values. |
| [[comparer_functions.md]] | Comparer functions

Comparer functions provide custom comparison logic for ordering and equality operations. |
| [[conditional-padstart-m-snippet.md]] | Conditional PadStart M Snippet

Copy-paste boilerplate for padding only N-digit numbers in a mixed-type column, leaving  |
| [[conditional-text-padstart.md]] | Conditional Text.PadStart

Applies `Text.PadStart` only to numeric values of a specific length, leaving all other values |
| [[cube_applyparameter.md]] | Cube.ApplyParameter

Returns a cube after applying parameter with arguments to cube. |
| [[cube_parameters.md]] | Cube.Parameters

Returns a table containing the set of parameters that can be applied to cube. |
| [[custom_date_and_time_format_strings.md]] | Custom date and time format strings

User-defined format patterns for date, time, and datetime values. |
| [[custom_numeric_format_strings.md]] | Custom Numeric Format Strings

Custom numeric format strings use placeholder characters to build format patterns. |
| [[function_from.md]] | Function.From

Takes a unary function function and creates a new function with the type functionType that constructs a l |
| [[function_invoke.md]] | Function.Invoke

Invokes the given function using the specified list of arguments and returns the result. |
| [[function_invokeafter.md]] | Function.InvokeAfter

Returns the result of invoking function after duration delay has passed. |
| [[function_isdatasource.md]] | Function.IsDataSource

Returns whether or not function is considered a data source. |
| [[function_scalarvector.md]] | Function.ScalarVector

Returns a scalar function of type scalarFunctionType that invokes vectorFunction with a single ro |
| [[geometrypoint_from.md]] | GeometryPoint.From

Creates a record representing a geometric point from its constituent parts, such as X coordinate, Y  |
| [[local_fixed_and_utc_variants_of_current_time_functions.md]] | Local, fixed, and UTC variants of current time functions

Power Query provides three variants of "current time" function |
| [[m_error_handling_with_try.md]] | Error Handling with Try

Errors occur when operators or functions encounter error conditions. |
| [[m_function_reference_index.md]] | M Function Reference Index

Complete index of all M library functions across 126 categories (711 unique functions). |
| [[m_functions_as_values.md]] | M Functions as Values

In M, a function is a value like any other. |
| [[m_language_is_functional_and_case_sensitive.md]] | M Language Is Functional and Case-Sensitive

M is a functional, case-sensitive language similar to F#. |
| [[record_functions.md]] | Record functions

Functions that create and manipulate record values. |
| [[replacer_functions.md]] | Replacer functions

Text replacement utilities in the Replacer standard library module. |
| [[sql-aggregate-functions.md]] | SQL Aggregate Functions

Functions

| Function | Returns |
|----------|---------|
| `COUNT()` | Number of non-empty rows |
| [[table_replaceerrorvalues.md]] | Table.ReplaceErrorValues

Replaces the error values in the specified columns of the table with the new values in the err |
| [[table_viewerror.md]] | Table.ViewError

Creates a modified error record from errorRecord which won't trigger a fallback when raised by a handle |
| [[table_viewfunction.md]] | Table.ViewFunction

Creates a view function based on function that can be handled in a view created by Table.View. |
| [[text_functions.md]] | Text functions

Functions that create and manipulate text values. |
| [[these_functions_create_and_manipulate_record_values.md]] | These functions create and manipulate record values

See: record_functions |
| [[these_functions_create_and_manipulate_text_values.md]] | These functions create and manipulate text values

See: text_functions |
| [[these_functions_create_and_manipulate_time_values.md]] | These functions create and manipulate time values

See: time_functions |
| [[time_fromtext_creates_a_time_from_local_universal_and_custom_time_formats.md]] | Time.FromText creates a Time from local, universal, and custom time formats

See: time_fromtext |
| [[time_functions.md]] | Time functions

Functions that create and manipulate time values. |
| [[tracelevel_error.md]] | TraceLevel.Error

Signature

```m

``` |
| [[type_forfunction.md]] | Type.ForFunction

Creates a function type from signature, a record of ReturnType and Parameters, and min, the minimum nu |
| [[type_functionparameters.md]] | Type.FunctionParameters

Returns a record with field values set to the name of the parameters of type, and their values  |
| [[type_functionrequiredparameters.md]] | Type.FunctionRequiredParameters

Returns a number indicating the minimum number of parameters required to invoke the inp |
| [[type_functionreturn.md]] | Type.FunctionReturn

Returns a type returned by a function type. |
| [[type_functions.md]] | Type functions

Functions that inspect, construct, and transform types. |
| [[value_viewerror.md]] | Value.ViewError

This function is intended for internal use only. |
| [[value_viewfunction.md]] | Value.ViewFunction

This function is intended for internal use only. |

| [[retail-power-query-data-preparation.md]] | Retail Power Query Data Preparation

ETL pipeline for retail data: deduplication, type correction, date columns, regional standardization |
| [[power-query-date-table-build.md]] | Power Query Date Table Build

Self-maintaining Date Table built in Power Query using List.Dates, List.Min, List.Max |
| [[single-formula-multiple-columns-power-query.md]] | Single Formula → Multiple Columns in Power Query

Record literal syntax in a Custom Column generates multiple output columns in one step |
| [[power-query-custom-column-workflow.md]] | Power Query Custom Column Workflow

End-to-end workflow: Add Column, Custom Column, expand record, Close & Apply |
| [[sort-column-pq-vs-dax.md]] | Sort Column — Power Query vs DAX

M conditional column for real imported dimensions (no DAX cycle); DATATABLE literals for disconnected tables |
| [[power-query-data-cleaning-checklist.md]] | Power Query Data Cleaning Checklist (12 Steps)

12-step PQ workflow: remove duplicates, fix types, handle blanks, trim spaces, standardize dates/categories, validate relationships, delete unused cols |
| [[pre-dashboard-cleaning-checklist-reference.md]] | Pre-Dashboard Cleaning Checklist (12 Steps)

Condensed checklist for pre-build use: types set, blanks handled, relationships validated, data quality page created |

## Patterns — Dynamic Date Granularity (Bittar, 2024)

|| Note | Description |
||------|-------------|
|| [[calendar-table-pq-daily-weekly-monthly.md]] | Calendar Table in Power Query: Daily + Weekly + Monthly Columns

M-code: List.Min/Max on Asset Data → Date.StartOfMonth bounds → ExpandListColumn; adds Daily (date), Weekly (Date.StartOfWeek), Monthly (Date.StartOfMonth) columns; three-column calendar supports field parameter granularity switching |

## Author Notes  (1 notes)

| Note | Description |
|------|-------------|
| [[nayan-pq-dax-source.md]] | Power Query vs DAX Decision Framework — Md Mizanur Rahman Nayan

| [[Isolation-Forest-Power-Query-Pattern.md]] | Isolation Forest Anomaly Detection in Power Query (Python)

Full Python pattern: null-drop → HourGroup → one-hot encoding → IsolationForest.fit_predict() → merge back to full dataset. No Premium required.

| [[Python-Data-Preparation-for-ML-Power-Query.md]] | Python Data Preparation for ML in Power Query — Checklist

Null-drop → feature engineering → one-hot encoding → fit → merge-back. The ordered checklist for embedding ML models in Power Query Python steps.

| [[Isolation-Forest-Python-Pandas-One-Hot-Snippet.md]] | Isolation Forest + Pandas One-Hot Encoding Boilerplate

| [[fxImageToBase64-Power-Query.md]] | fxImageToBase64 — Power Query M Function

M function: downloads an image URL and returns it as a Base64 data URL string. Wraps Web.Contents + Binary.ToText + BinaryEncoding.Base64.

| [[Power-Query-Base64-Conversion-Reference.md]] | Power Query Base64 Conversion — Key Concepts

| [[Binary-ToText-Base64-Power-Query.md]] | Binary.ToText — Power Query Binary to Base64

Binary.ToText(binary, BinaryFormat.Base64), complete Folder connector M pattern, Base64 vs Hex.

Web.Contents, Binary.ToText, BinaryEncoding.Base64 — the M functions for converting images to Base64 in Power Query.

Copy-paste Python snippet: sklearn IsolationForest with HourGroup bucketing, pd.get_dummies(), and merge-back to full dataset.

> Type: comparison guide / beginner
> Author: Md Mizanu |
