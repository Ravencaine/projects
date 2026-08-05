---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: concept
tags: [dax, financial-functions, overview, time-value-of-money]
---

# Financial Functions in DAX

DAX financial functions perform financial calculations like net present value, rate of return, depreciation, and bond pricing.

## Time Value of Money

| Function | Description |
|----------|-------------|
| FV | Future value of an investment |
| PV | Present value |
| NPV | Net present value |
| XNPV | NPV with specific dates |
| RATE | Interest rate per period |
| NPER | Number of periods |
| PMT | Payment per period |
| PPMT | Principal payment in a period |
| IPMT | Interest payment in a period |
| CUMIPMT | Cumulative interest between periods |
| CUMPRINC | Cumulative principal between periods |

## Depreciation

| Function | Description |
|----------|-------------|
| SLN | Straight-line depreciation |
| SYD | Sum-of-years-digits depreciation |
| DDB | Double-declining balance depreciation |
| VDB | Variable declining balance depreciation |
| DB | Fixed-declining balance depreciation |

## Bond Pricing

| Function | Description |
|----------|-------------|
| PRICE | Price per $100 face value of a bond |
| PRICEDISC | Price per $100 of a discounted bond |
| PRICEMAT | Price at maturity |
| YIELD | Yield of a bond |
| YIELDDISC | Yield of a discounted bond |
| YIELDMAT | Yield at maturity |
| TBILLPRICE | T-bill price |
| TBILLYIELD | T-bill yield |
| TBILLEQ | T-bill bond-equivalent yield |

## Coupon / Date Functions

| Function | Description |
|----------|-------------|
| COUPDAYBS | Days from settlement to first coupon |
| COUPDAYS | Days in coupon period |
| COUPDAYSNC | Days from settlement to next coupon |
| COUPNCD | Next coupon date after settlement |
| COUPNUM | Number of coupons between settlement and maturity |
| COUPPCD | Previous coupon date before settlement |

## Accrued Interest

| Function | Description |
|----------|-------------|
| ACCRINT | Accrued interest for periodic payments |
| ACCRINTM | Accrued interest at maturity |

## Other Financial

| Function | Description |
|----------|-------------|
| DISC | Discount rate |
| INTRATE | Interest rate for a fully invested security |
| ISPMT | Interest payment for a given period |
| NOMINAL | Nominal annual interest rate |
| EFFECT | Effective annual interest rate |
| DURATION | Macauley duration of a security |
| MDURATION | Modified duration |
| PDURATION | Periods required to reach a value |
| RRI | Equivalent interest rate for growth |
| RECEIVED | Amount received at maturity |
| DOLLARDE | Convert fractional dollar to decimal |
| DOLLARFR | Convert decimal dollar to fractional |

## Example: NPV

```dax
NPV(Rate, CashFlow1, CashFlow2, ...)
```

## Example: PMT

```dax
Monthly Payment = PMT(Rate/12, Years*12, -LoanAmount)
```

## Related

- [[pmt]]
- [[xnpv]]
