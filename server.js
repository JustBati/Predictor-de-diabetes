const express = require('express');
const fs = require('fs');
const csvParser = require('csv-parser');  // Necesitarás instalar este módulo usando npm
const createCsvWriter = require('csv-writer').createObjectCsvWriter;  // Necesitarás instalar este módulo usando npm

const app = express();

// Sirve los archivos estáticos desde la carpeta public
app.use(express.static('public'));

app.use(express.json());  // Para analizar cuerpos de solicitud JSON

app.post('/submit', (req, res) => {
    const data = req.body;
    const csvWriter = createCsvWriter({
        path: './Data/Sample.csv',
        header: Object.keys(data).map(key => ({id: key, title: key})),
    });

    csvWriter.writeRecords([data])  // Escribe los datos en el archivo CSV
    .then(() => {
        let rows = [];
        fs.createReadStream('./Data/Answer.csv')
            .pipe(csvParser())
            .on('data', (row) => {
                rows.push(row);
            })
            .on('end', () => {
                console.log('CSV file successfully processed');
                res.json(rows); // Envía todos los registros leídos del CSV
            });
    })
    .catch(err => {
        console.error('Error writing to CSV file', err);
        res.status(500).send('Server error');
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
