const express = require('express');
const db = require('./database.js');
const { PDFDocument, rgb } = require('pdf-lib');
const fs = require('fs');
const path = require('path');

// Inicializa o Express
const app = express();
const port = 3000;

// Middleware para servir arquivos estáticos (HTML, CSS, JS)
app.use(express.static('public'));
app.use(express.json()); // Para receber JSON no body das requisições

// Rota para listar clientes
app.get('/clientes', (req, res) => {
    db.all('SELECT * FROM clientes', (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

// Rota para adicionar um cliente
app.post('/clientes', (req, res) => {
    const { nome, cpf, endereco, telefone, email, rg } = req.body;

    db.run(
        'INSERT INTO clientes (nome, cpf, endereco, telefone, email, rg) VALUES (?, ?, ?, ?, ?, ?)',
        [nome, cpf, endereco, telefone, email, rg],
        function (err) {
            if (err) {
                console.error('Erro ao salvar cliente:', err);
                res.status(500).json({ error: err.message });
                return;
            }
            res.json({ id: this.lastID });
        }
    );
});

// Rota para excluir um cliente
app.delete('/clientes/:id', (req, res) => {
    const { id } = req.params;
    db.run('DELETE FROM clientes WHERE id = ?', [id], function (err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ message: 'Cliente excluído com sucesso' });
    });
});

// Rota para gerar uma declaração
app.post('/gerar-declaracao', async (req, res) => {
    const { clienteId, tipoDeclaracao } = req.body;

    // Busca o cliente no banco de dados
    db.get('SELECT * FROM clientes WHERE id = ?', [clienteId], async (err, cliente) => {
        if (err) {
            console.error('Erro ao buscar cliente:', err);
            res.status(500).json({ error: err.message });
            return;
        }

        try {
            // Carrega o template da declaração
            const templatePath = path.join(__dirname, 'declaracoes', `declaracao${tipoDeclaracao}.pdf`);
            console.log('Caminho do template:', templatePath);

            if (!fs.existsSync(templatePath)) {
                throw new Error('Arquivo de template não encontrado');
            }

            const pdfBytes = fs.readFileSync(templatePath);
            const pdfDoc = await PDFDocument.load(pdfBytes);
            const pages = pdfDoc.getPages();
            const firstPage = pages[0];

            // Preenche as informações do cliente
            const { width, height } = firstPage.getSize();
            const textOptions = { size: 12, color: rgb(0, 0, 0) };

            switch (tipoDeclaracao) {
                case '1': // DECLARAÇÃO1.pdf
                    firstPage.drawText(`Nome: ${cliente.nome}`, { x: 50, y: height - 100, ...textOptions });
                    firstPage.drawText(`CPF: ${cliente.cpf}`, { x: 50, y: height - 120, ...textOptions });
                    firstPage.drawText(`Endereço: ${cliente.endereco}`, { x: 50, y: height - 140, ...textOptions });
                    firstPage.drawText(`Telefone: ${cliente.telefone}`, { x: 50, y: height - 160, ...textOptions });
                    break;

                case '2': // DECLARAÇÃO2.pdf
                    firstPage.drawText(`Nome: ${cliente.nome}`, { x: 50, y: height - 100, ...textOptions });
                    firstPage.drawText(`CPF: ${cliente.cpf}`, { x: 50, y: height - 120, ...textOptions });
                    firstPage.drawText(`Endereço: ${cliente.endereco}`, { x: 50, y: height - 140, ...textOptions });
                    break;

                default:
                    throw new Error('Tipo de declaração inválido');
            }

            // Salva o PDF editado
            const modifiedPdfBytes = await pdfDoc.save();
            res.setHeader('Content-Type', 'application/pdf');
            res.send(modifiedPdfBytes);
        } catch (error) {
            console.error('Erro ao gerar a declaração:', error);
            res.status(500).json({ error: 'Erro ao gerar a declaração: ' + error.message });
        }
    });
});

// Inicia o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});