const express = require('express');
const fetch = require('node-fetch').default;

const app = express();
const port = 3000;
const path = require('path');

app.set('views', path.join(__dirname, 'views'));

app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', async (req, res) => {
    const url = 'https://api.bnm.gov.my/public/exchange-rate';
    const headers = {
      'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
      'Accept': 'application/vnd.BNM.API.v1+json',
      'Sec-Ch-Ua-Mobile': '?0',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
      'Sec-Ch-Ua-Platform': '"Windows"',
      'Origin': 'https://apikijangportal.bnm.gov.my',
      'Sec-Fetch-Site': 'same-site',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': 'https://apikijangportal.bnm.gov.my/',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'en-US,en;q=0.9',
      'Connection': 'close'
    };
    
    const params = new URLSearchParams({
      session: '0900',
      quote: 'rm'
    });
    
    (async () => {
      try {
        const response = await fetch(`${url}?${params.toString()}`, {
          headers,
        });
    
        if (response.ok) {
          const data = await response.json();
          //console.log(data);
          // Find the entry with currency_code 'SGD'
const sgdEntry = data.data.find(currency => currency.currency_code === 'SGD');

// Extract the currency_code and rate
const sgdCurrencyCode = sgdEntry.currency_code;
const sgdRate = sgdEntry.rate;

console.log(`Currency Code: ${sgdCurrencyCode}`);
console.log(`Rate:`, sgdRate);

res.render('index', { sgdCurrencyCode, sgdRate });

        } else {
          console.log(`Error: ${response.status}`);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    })();

    
  });
  
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
