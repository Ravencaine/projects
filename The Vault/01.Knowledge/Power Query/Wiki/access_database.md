---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["access", "m-function"]
---


# Access.Database

Returns a structural representation of an Access database, database. An optional record parameter, options, may be specified to control the following options: CreateNavigationProperties: A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false). NavigationPropertyNameGenerator: A function that is used for the creation of names for navigation properties. The record parameter is specified as [option1 = value1, option2 = value2...], for example. --- PAGE 314 ---

## Signature

```m
Access.Database(database as binary, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| database | binary | |
| optional options | nullable record | |

## Returns

table

