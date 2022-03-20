# Bitcoinscraper
## Lina Stroobants

<br>

### Installatie VM - Ununtu
-   Werkte niet naar behoren. Kreeg ofwel veel errors ofwel geen en VM crashte... 7 op de 10 keer werkte het niet.
Dit maakte het moeilijk om hiermee te werken. Hierdoor heb ik deze scraper in Windows gemaakt.
<br> 

### Werking Crpytoscraper
Eens de python-file loopt, scrapet deze automatisch elke minuut de data en bewaart deze in een json-file "BitcoinScraping.json". Om de data dan uiteindelijk door te sturen naar de database in MongoDB, zet ik de json-file om naar een dataframe.
MongoDB verwacht een dictionary, een json-file werkt dus niet. Ik stuur niet alle hashes van elke minuut door. Ik geef enkel de eerste 5 per minuut door. Anders gaat er te veel data opgeslagen worden.

1. Scraper haalt via een request op de site "https://www.blockchain.com/btc/unconfirmed-transactions" de data op.
2. Voor ik data in een file zet, kijk ik eerst na of er al een json-file bestaat. Zo niet, dan maak ik deze aan.
3. Ik filter de gescrapte data. Ik heb niet alle data nodig, enkel Hash, Time, Amount (BTC) en Amount (USD).
4. De nieuwe data wordt toegevoegd met de reeds gescrapte data in de json-file
5. Elke minuut runt het programma opnieuw en wordt de nieuwe data gescraped