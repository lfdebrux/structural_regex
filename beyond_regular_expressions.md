%title: Beyond Regular Expressions
%author: Laurence de Bruxelles

-> Beyond Regular Expressions <-
================================

-> Because Regular Expressions are bad <-
-> and they should feel bad <-

---

The regex that broke the internet
=================================

    (?:(?:\"|'|\]|\}|\\|\d|
      (?:nan|infinity|true|false|null|undefined|symbol|math)
      |\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*(?:.*=.*)))

From the [Cloudflare blog](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019)

---

The 
