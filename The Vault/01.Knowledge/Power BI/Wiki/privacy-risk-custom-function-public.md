---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [privacy-risk, custom-function, cognitive-services, data-exposure, power-query]
---

# Privacy Risk — Custom Function Data Source Must Be Public

Power Query blocks API calls across data sources of different privacy levels. For Cognitive Services custom functions to work, the Azure endpoint must be set to Public — transmitting your text data to Azure.

## Expected Behaviour

You create a custom function to call the Text Analytics API. Power Query silently blocks the API call because the privacy levels of the local table and the Azure endpoint don't match.

## Actual Behaviour

Power BI's data privacy levels prevent data from non-public sources from being sent to external endpoints. For the API call to work, the Azure Cognitive Services endpoint must be set to **Public** in the privacy settings.

## Why It Happens

Power BI enforces data sovereignty between data sources. By default, the Azure endpoint is set to Private or Organizational, which blocks outbound data transfer.

## How to Fix

1. File → Options → Privacy
2. Uncheck "Ignore Privacy Levels and potentially improve performance"
3. OR: File → Options → Global → Privacy → Privacy Levels
4. Set the Azure Cognitive Services URL to **Public** (this tells Power BI: "I consent to sending my data to this endpoint")

## CRITICAL WARNING

Setting the endpoint to **Public** means your text data is transmitted to Azure Cognitive Services and processed by Microsoft's servers. Ensure:
- Your text data does not contain PII (or use [[pii-detection]] first)
- Your organisation's privacy policy permits cloud API calls
- The Azure Cognitive Services resource is in the appropriate region for data residency requirements

## Related

- [[power-query-custom-function-text-analytics]]
- [[remove-pii-from-datasets]]
- [[responsible-ai-six-principles]]
