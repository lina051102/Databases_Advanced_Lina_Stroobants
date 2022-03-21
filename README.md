# Bitcoinscraper
## Lina Stroobants

<br>

### Installatie VM - Ubuntu
-   Werkte niet naar behoren. Kreeg ofwel veel errors ofwel geen en VM crashte... 7 op de 10 keer werkte het niet.
Dit maakte het moeilijk om hiermee te werken. Hierdoor heb ik deze scraper in Windows gemaakt.
<br> 

### Werking Crpytoscraper
Wanneer de python file loopt, scrapet ze automatisch elke minuut de data. In Redis wordt de hash vergeleken met diegene die al in de database op MongoDB staan. Als hij er nog niet bestaat, zet hij ze erbij. Voor 70 seconden blijft de hash in de cache opgeslagen. Na 60 seconden wordt die toegevoegd, maar ik heb een marge van 10 seconden genomen in het geval de scraper vertraagd is.

1. Via een request op de site "https://www.blockchain.com/btc/unconfirmed-transactions" haalt de scraper de nodige data (Hash, Time, Amount(BTC) en Amount(USD)) op.

2. In Redis wordt de hash vergeleken met diegene die al in de database op MongoDB staan. Als hij er nog niet bestaat, zet hij ze erbij.

3. Voor 70 seconden blijft de hash in de cache opgeslagen. Na 60 seconden wordt die toegevoegd, maar ik heb een marge van 10 seconden genomen in het geval de scraper vertraagd is.

4. Na 1 minuut loopt de scraper opnieuw en wordt nieuwe data toegevoegd.