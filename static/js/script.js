async function getCryptoData() {
     const response = await fetch('/get-crypto-data/');
     const data = await response.json();
     return data;
 }

 // Função para renderizar o gráfico usando Chart.js
 async function renderCryptoChart() {
     const cryptoData = await getCryptoData();

     var ctx = document.getElementById('cryptoChart').getContext('2d');
     var myChart = new Chart(ctx, {
         type: 'line',
         data: {
             labels: cryptoData.prices.map(entry => new Date(entry[0]).toLocaleTimeString()),
             datasets: [{
                 label: 'Price',
                 data: cryptoData.prices.map(entry => entry[1]),
                 borderColor: 'rgba(75, 192, 192, 1)',
                 borderWidth: 1
             }]
         }
     });
 }

 // Chame a função para renderizar o gráfico
 renderCryptoChart();