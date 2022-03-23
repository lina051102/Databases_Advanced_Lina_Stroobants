# Bitcoinscraper
## Lina Stroobants

<br>

### VM - Ubuntu
Werkte niet naar behoren. Kreeg ofwel veel errors ofwel geen en VM crashte... 7 op de 10 keer werkte het niet.
Dit maakte het moeilijk om hiermee te werken. Hierdoor heb ik deze scraper in Windows gemaakt.
<br> 

### Werking Cryptoscraper
Wanneer de python file loopt, scrapet ze automatisch elke minuut de data. In Redis wordt de hash vergeleken met diegene die al in de database op MongoDB staan. Als hij er nog niet bestaat, zet hij ze erbij. Voor 70 seconden blijft de hash in de cache opgeslagen. Na 60 seconden wordt die toegevoegd, maar ik heb een marge van 10 seconden genomen in het geval de scraper vertraagd is.

1. Via een request op de site "https://www.blockchain.com/btc/unconfirmed-transactions" haalt de scraper de nodige data (Hash, Time, Amount(BTC) en Amount(USD)) op. Ik geef enkel de eerste 10 mee, anders gaat er te veel data in de database zitten.

2. In Redis wordt de hash vergeleken met diegene die al in de database op MongoDB staan. Als hij er nog niet bestaat, zet hij ze erbij.

3. Voor 70 seconden blijft de hash in de cache opgeslagen. Na 60 seconden wordt die toegevoegd, maar ik heb een marge van 10 seconden genomen in het geval de scraper vertraagd is.

4. Na 1 minuut loopt de scraper opnieuw en wordt nieuwe data toegevoegd (de oude wordt dan verwijderd uit de database).