---
created: 2026-08-01
updated: 2026-08-02
source: "Supercharge Your Power BI with Python Cleaning Magic - Janvi Gupta.md"
note_type: atomic
tags: [power-query, python, pandas, text-cleaning, whitespace, beginner]
---

# Text Cleaning in Power Query with Python

pandas string methods for cleaning messy text data inside Power Query Python scripts.

## Trimming Whitespace

`str.strip()` removes leading and trailing spaces — common issue from imported data.

```python
# Trim single column
dataset["ProductName"] = dataset["ProductName"].str.strip()

# Trim all string columns
for col in dataset.select_dtypes(include=["object"]).columns:
    dataset[col] = dataset[col].str.strip()
```

## Removing Extra Spaces

`str.replace()` with a regex collapses multiple spaces to one.

```python
# Replace multiple spaces with single space
dataset["Description"] = dataset["Description"].str.replace(r"\s+", " ", regex=True)
```

## Case Normalization

```python
# Lowercase everything
dataset["Category"] = dataset["Category"].str.lower()

# Title case
dataset["ProductName"] = dataset["ProductName"].str.title()

# Uppercase (e.g., for codes)
dataset["ProductCode"] = dataset["ProductCode"].str.upper()
```

## Removing Unwanted Characters

```python
# Remove special characters (keep only alphanumeric + space)
dataset["Notes"] = dataset["Notes"].str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)

# Remove digits
dataset["TextColumn"] = dataset["TextColumn"].str.replace(r"\d", "", regex=True)
```

## Finding and Replacing Text

```python
# Replace one value
dataset["Status"] = dataset["Status"].str.replace("Active", "Enabled")

# Replace with regex pattern
dataset["Email"] = dataset["Email"].str.lower().str.strip()
```

## Combining Text Operations

```python
# Clean pipeline: trim → lowercase → remove special chars
dataset["Email"] = (
    dataset["Email"]
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", "", regex=True)
)
```

## Related

- [[python-pandas-data-cleaning-patterns]] — broader cleaning patterns
- [[python-null-nan-handling-power-query]] — missing value handling
- [[python-script-in-power-query]] — how to run Python in PQ
