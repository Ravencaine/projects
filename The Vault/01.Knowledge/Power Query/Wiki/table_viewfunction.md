---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.ViewFunction

Creates a view function based on function that can be handled in a view created by Table.View. The OnInvoke handler of Table.View can be used to define a handler for the view function. As with the handlers for built-in operations, if no OnInvoke handler is specified, or if it does not handle the view function, or if an error is raised by the handler, function is applied on top of the view. Refer to the published Power Query custom connector documentation for a more complete description of Table.View and custom view functions. --- PAGE 1158 ---

## Signature

```m
Table.ViewFunction(function as function) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| function | function | |

## Returns

function

