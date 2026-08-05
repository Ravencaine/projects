---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: concept
tags: [dax, fundamentals, unicode, gb18030, localization]
---

# GB18030 Character Set Support

China's GB18030-2022 standard is the latest update to the Chinese character encoding standard. DAX and Power BI support GB18030-encoded data sources.

## Key Points

- GB18030 is a variable-length encoding supporting both single-byte (ASCII) and multi-byte (Chinese) characters
- Power BI and Analysis Services can import data from GB18030-encoded sources
- After importing GB18030 data, you may need to perform a full refresh of the model
- Unicode is recommended for new models; GB18030 is primarily for legacy system compatibility

## Importing GB18030 Data

When connecting to a GB18030 data source:
1. Ensure the source driver supports GB18030 encoding
2. Import the data
3. After import, perform a full model refresh

## UnicodeCharacterBehavior Setting

Analysis Services has a server-level setting `UnicodeCharacterBehavior` that controls how Unicode characters are handled. This setting affects compatibility with GB18030 sources.

## Related

- [[dax-data-types]]
