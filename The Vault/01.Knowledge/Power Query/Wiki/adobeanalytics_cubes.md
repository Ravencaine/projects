---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["adobeanalytics", "m-function"]
---


# AdobeAnalytics.Cubes

Returns a table of multidimensional packages from Adobe Analytics. An optional record parameter, options, may be specified to control the following options: HierarchicalNavigation: A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false). MaxRetryCount: The number of retries to perform when polling for the result of the query. The default value is 120. RetryInterval: The duration of time between retry attempts. The default value is 1 second. Implementation: Specifies Adobe Analytics API version. Valid values are: "2.0". Default uses API version 1.4. --- PAGE 316 ---

## Signature

```m
AdobeAnalytics.Cubes(optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| optional options | nullable record | |

## Returns

table

