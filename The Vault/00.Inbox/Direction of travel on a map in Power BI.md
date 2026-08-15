---
title: "Direction of travel on a map in Power BI"
source: "https://medium.com/microsoft-power-bi/direction-of-travel-on-a-map-in-power-bi-abc2a31ac055"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-11-20
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*1As1zUProJaHDmJt.png)

A global commodity trading client of ours had a requirement to create a dashboard that presented the latest locations and headings for a range of container ships

This was part of a migration away from using Tableau, to using Power BI

The internal BI team had been using a dashboard in Tableau which catered for this requirement quite easily, but could not find a way to replicate this in Power BI, so the task was handed over to us

What follows is a simplified guide using some sample data that we have generated to make it straight forward to follow along

## Getting started

The first thing you will need is some sample shipping data

We created a simple spreadsheet with 49 rows to illustrate

[shipping data](https://www.selectdistinct.co.uk/wp-content/uploads/2023/10/shipping-data.xlsx)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*UTPtxFdMW0L0-EHz.png)

Shipping data is typically polled by the shipping companies and captures the direction of travel (Heading), the latitude and longitude and speed in knots at the time, as well as other static data about the vessel itself

The key data points we will focus on are

Heading — this is the direction the ship is travelling in in degrees, with zero degrees representing north

Latitude and Longitude — The geographical co-ordinates

Ship name — randomly generated ship names

You will also need an appropriate icon to represent the ships

In our case we used a AI image creator to represent a ship and removed the background

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*aB77-oVByRPaFXDK.png)

It is really important that this image faces North in its neutral position, we will be applying the heading as a rotation to illustrate the direction of travel

## Step by Step

The first step is to load the sample data into Power BI

On the Home ribbon in Power BI Desktop, select get data, then Excel workbook and select your excel file

If you download our sample data you will save yourself some time and not have to do anything to the field types

Once it is loaded you can then download the IconMapV3 from the marketplace, which is a free download

select the three dots and select get more visuals

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*hiFbuT1SoTjwQrP0.png)

In the search box type ‘Icon Map’

hit enter and look for Icon Map by James Dales

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*XXjXwANFog1Kobaq.png)

select icon map, then click add and the new visual appears in Power BI desktop

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Baj9DfX_xd4FDPxT.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*5rqUMyOtYL9GvcKb.png)

Now select this and drag it onto your canvas

![](https://miro.medium.com/v2/resize:fit:1250/format:webp/0*PdCRbmcCawBWqid0.png)

Field settings for the Icon Map

Category — use ship name

longitude = longitude

latitude = latitude

Size = IconSize

Add the icon

Select format your visual

Then go down to objects and expand the section

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*LZh_pdGXtbwR0PEG.png)

We will use the conditional formatting options under Image / WKT

within there we will use the icon field

The icon field is a url which Power BI uses to download the icon

we have used this

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*rppr-F5LIxEaOWqv.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*pLDIBJX0L5J-4rgE.png)

Then set the heading, we use the image rotation to turn the object by the correct number of degrees

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*UmSo62WrBQsBLtPQ.png)

You will now see the position and direction of travel of these ships on the map

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*mgT5zuG971RKdWGP.png)

## Conclusion

Showing the direction of travel on a map in Power BI is made much easier with this add in

This just the basics to get you started, and by following along with the example you can get similar results

Icon Map v3 is the latest release and has a great deal more features, some of which look very impressive

## Further Reading

[Icon Map (icon-map.com)](https://icon-map.com/)

There is a dedicated website to provide further information and support along with some excellent interactive examples

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*5Rxi60xJW32L9buC.png)

Subscribe to our channel to see more SQL tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)