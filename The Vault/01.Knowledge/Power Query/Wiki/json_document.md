---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [json, m-function]
---


# Json.Document

Returns the content of the JSON document. jsonText: The content of the JSON document. The value of this parameter can be text or a binary value returned by a function like File.Content. encoding: A TextEncoding.Type that specifies the encoding used in the JSON document. If encoding is omitted, UTF8 is used.

## Signature

```m
Json.Document(jsonText as any, optional encoding as nullable number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| jsonText | any | |
| optional encoding | nullable number | |

## Returns

any

### Example 1

Returns the content of the specified JSON text as a record.

```m
let
Source = "{
""project"": ""Contosoware"",
""description"": ""A comprehensive initiative aimed at enhancing digital
presence."",
""components"": [
""Website Development"",
""CRM Implementation"",
""Mobile Application""
]
}",
jsonDocument = Json.Document(Source)
in
jsonDocument
```

// Output
```
[
project = "Contosoware",
description = "A comprehensive initiative aimed at enhancing digital
presence."
components =
{
"Website Development",
"CRM Implementation",
"Mobile Application"
}
]
```

### Example 2

Returns the content of a local JSON file.

```m
let
Source = (Json.Document(
File.Contents("C:\test-examples\JSON\Contosoware.json")
)
in
Source
```

// Output
```
A record, list, or primitive value representing the JSON data contained in the file
```

### Example 3

Returns the content of an online UTF16 encoded JSON file.

```m
let
Source = Json.Document(
Web.Contents("htts://contoso.com/products/Contosoware.json"),
TextEncoding.Utf16)
)
```

// Output
```
A record, list, or primitive value representing the JSON UTF16 data contained in the file
```

