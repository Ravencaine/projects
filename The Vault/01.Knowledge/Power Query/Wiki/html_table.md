---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["html", "m-function"]
---


# Html.Table

Returns a table containing the results of running the specified CSS selectors against the provided html. An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: RowSelector

## Signature

```m
Html.Table(
html as any,
columnNameSelectorPairs as list,
optional options as nullable record
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| html | any | |
| columnNameSelectorPairs | list | |
| optional options | nullable record | |

## Returns

table

### Example 1

Returns a table from a sample html text value.

```m
Html.Table("<div class=""name"">Jo</div><span>Manager</span>", {{"Name", ".name"},
{"Title", "span"}}, [RowSelector=".name"])\
```

// Output
```
#table({"Name", "Title"}, {{"Jo", "Manager"}})
```

### Example 2

Extracts all the hrefs from a sample html text value.

```m
Power Query M
Html.Table("<a href=""/test.html"">Test</a>", {{"Link", "a", each [Attributes]
[href]}})
```

// Output
```
#table({"Link"}, {{"/test.html"}})
```

