---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["accesscontrolentry", "m-function"]
---


# AccessControlEntry.ConditionToIdentities

Using the specified identityProvider, converts the condition into the list of identities for which condition would return true in all authorization contexts with identityProvider as the identity provider. An error is raised if it is not possible to convert condition into a list of identities, for example if condition consults attributes other than user or group identities to make a decision. Note that the list of identities represents the identities as they appear in condition and no normalization (such as group expansion) is performed on them. --- PAGE 313 ---

## Signature

```m
AccessControlEntry.ConditionToIdentities(identityProvider as function, condition
as function) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identityProvider | function | |
| condition | function | |

## Returns

list

