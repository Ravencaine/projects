---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-cognitive-services, resource, create, azure-portal, setup]
---

# Create a Cognitive Services Resource in Azure Portal

Register a Cognitive Services resource to get the endpoint URL and API key needed for Power Query custom functions.

## Prerequisites

- Microsoft Azure account (free account works)
- Credit card for identity verification (free tier applies)

## Steps

1. Go to **portal.azure.com** → sign in
2. Search for the specific service (e.g., "Text Analytics" for Language Detection/Key Phrases/Sentiment; "Computer Vision" for image analysis)
3. Click **Create**
4. Fill in:
   - **Subscription**: Azure subscription
   - **Resource group**: create new or use existing
   - **Region**: choose closest region
   - **Name**: resource name (e.g., `diepeveen-text-analytics`)
   - **Pricing tier**: F0 (Free, 5K transactions/month) or S0 (Pay-as-you-go)
5. Review + Create → wait for deployment
6. Go to **Keys and Endpoint** (in the resource sidebar)
7. Copy **Key 1** and **Endpoint URL**: these go into the Power Query custom function

## Security Notes

- Store the API key securely — never commit it to version control
- Use environment variables or Azure Key Vault in production
- For Power BI: the key is embedded in the pbix file — limit who can access the file

## Related

- [[language-detection-api]]
- [[power-query-custom-function-text-analytics]]
