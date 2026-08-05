---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# ODDFPRICE

Returns the price per $100 face value of a security having an odd (short or long) first period.

## Syntax

```dax
ODDFPRICE(<settlement>, <maturity>, <issue>, <first_coupon>, <rate>, <yld>, <redemption>, <frequency>[, <basis>])
```

## Remarks

Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899. The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For