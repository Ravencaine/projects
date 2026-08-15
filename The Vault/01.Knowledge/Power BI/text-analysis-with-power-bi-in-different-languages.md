---
title: "Text Analysis with Power BI in different languages"
source: "https://www.flip-design.de/?p=677"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Text Analysis with Power BI in different languages | flip-it.de :: SQL, BI and more According to the msdn article „ How to integrate Text Analysis into Power BI „, I needed to detect the language of an comment and make a sentiment analysis of it. The reason to make it parametrized and not change the language key is easy, mostly in Germany I have comments in English, German Spain etc. So, after I completed the Howto above, i created a new M Function named „Language“ with this code: The code above is 1:1 from the msdn webpage to get a two letter code of the language of the key merged subject and body. This is also similar to the other steps, but it must be the first invoke function. The next step is to get the Key Phrases, but depending of the language of the column which are created before. The JSon Body has no longer the hard coded en, is uses a new parameter language which is given on the function header. So you must edit the „invoke custom Function“-call with our new language column: Now, we have our Key Phrases depending on the detected language and we can get the sentiment score also depending on the language with this code: That’s it, after we make another invoke function call, we get the sentiment score based on the given language. The order after that in the M Query Editor: Schreibe einen Kommentar Antwort abbrechen Du musst angemeldet sein, um einen Kommentar abzugeben.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=677)*
