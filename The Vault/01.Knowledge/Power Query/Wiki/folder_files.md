---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [folder, m-function]
---


# Folder.Files

Returns a table containing a row for each file found in the specified folder and all its subfolders. path: The path to the folder you want to retrieve the files from. The supplied folder path must be a valid absolute path. options: (Optional) This parameter is currently intended for internal use only. Each row of the returned table contains properties of the file and a link to its content. Example Return a table containing all of the files found in C:\test-examples\example-folder and all of its subfolders. Usage Power Query M Folder.Files("C:\test-examples\example-folder") Output A table containing the files, their properties, and a link to their content. Last updated on 04/03/2026 --- PAGE 358 ---

## Signature

```m
Folder.Files(path as text, optional options as nullable record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| path | text | |
| optional options | nullable record | |

## Returns

table

