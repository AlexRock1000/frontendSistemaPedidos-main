# CONTRATO

## 1. Dados que a tela exibe

- `nome` — texto — nome do produto nos cartões do cardápio e nos itens do carrinho e do pedido.
- `descricao` — texto — descrição do produto no cartão do cardápio.
- `preco` — número — preço unitário no cartão do cardápio.
- `imagem` — texto — imagem do produto no cartão do cardápio e no carrinho.
- `destaque` — booleano — selo “Mais pedido” no cartão do cardápio quando o valor é verdadeiro.
- `nome` da categoria — texto — título das seções do cardápio e opções do filtro de categorias.
- `icone` da categoria — texto — título da seção e imagem reserva do produto quando a imagem falha.
- `quantidade` do item — número — controles de quantidade no cardápio, no carrinho e na lista de itens do pedido.
- `quantidadeTotal` — número — contador da navegação, da barra do carrinho e do resumo do carrinho.
- `total` — número — total da barra do carrinho, do carrinho e do cartão do pedido.
- `cliente` — texto — nome do cliente no formulário do carrinho e no cartão do pedido.
- `tipo` — texto — opção “Comer aqui” ou “Para viagem” no formulário e no cartão do pedido.
- `observacao` — texto — campo opcional no formulário e observação no cartão do pedido quando preenchida.
- `numero` do pedido — número — identificação exibida como “Pedido #...” no cartão do pedido e nas mensagens.
- `status` — texto — etiqueta de status, filtro por status e seletor de status do pedido.
- `itens` — lista — produtos, quantidades e preços no carrinho e no cartão do pedido.
- `criadoEm` — texto — data e hora de criação no cartão do pedido.
- `em andamento` — número — quantidade de pedidos que não estão nos status finalizados.
- `contador` dos filtros — número — quantidade de pedidos em cada status e quantidade total de pedidos.

## 2. Ações que o usuário dispara

- Selecionar “Novo pedido” ou “Pedidos” — trocar a tela exibida.
- Selecionar uma categoria — mostrar somente os produtos daquela categoria.
- Selecionar “Todos” no cardápio — mostrar os produtos de todas as categorias.
- Adicionar um produto — colocar o produto no carrinho com quantidade 1 ou aumentar sua quantidade.
- Aumentar a quantidade — adicionar mais uma unidade do produto.
- Diminuir a quantidade — remover uma unidade; quando chegar a zero, retirar o produto do carrinho.
- Abrir “Ver pedido” — abrir o painel do carrinho.
- Fechar o carrinho — fechar o painel e manter os itens selecionados.
- Limpar o carrinho — remover todos os produtos selecionados.
- Preencher o nome do cliente — permitir o envio do pedido; o nome é obrigatório.
- Selecionar o tipo de consumo — registrar “Comer aqui” ou “Para viagem”.
- Preencher uma observação — registrar uma instrução opcional para o pedido.
- Enviar pedido — criar o pedido, limpar o carrinho e informar o número gerado.
- Selecionar “Ver pedidos” no aviso — abrir a tela de pedidos.
- Atualizar pedidos — buscar novamente os pedidos e os status disponíveis.
- Selecionar um filtro de status — mostrar somente os pedidos com o status escolhido.
- Alterar o status no seletor — atualizar o status do pedido.
- Clicar em “Iniciar preparo”, “Marcar pronto” ou “Marcar entregue” — avançar o pedido para o próximo status configurado.
- Clicar em “Fazer um pedido” — abrir a tela de novo pedido quando não houver pedidos.
- Clicar em “Ver todos” — remover o filtro de status quando nenhum pedido corresponder a ele.
- Restaurar dados de exemplo — apagar os pedidos atuais e carregar novamente os dados de exemplo.
- Fechar um aviso — ocultar a mensagem exibida.

## 3. O que o servidor precisaria fazer

- Navegação entre telas: nada no servidor; é uma mudança local de interface.
- Filtro de categorias: nada no servidor na implementação atual; os produtos já carregados são filtrados na tela.
- Adição, remoção e limpeza do carrinho: nada no servidor antes do envio; o carrinho fica mantido na tela.
- Carregamento do cardápio: fornecer as categorias ordenadas e os produtos disponíveis.
- Envio do pedido: validar o nome e a existência de itens, conferir a disponibilidade dos produtos, calcular os preços e o total, criar o pedido com status “Recebido” e retornar o pedido criado.
- Atualização da lista de pedidos: fornecer os pedidos, preferencialmente do mais recente para o mais antigo, e fornecer a lista de status.
- Filtro de status: nada no servidor na implementação atual; a filtragem é feita na tela.
- Alteração de status: verificar se o pedido e o novo status existem, salvar a alteração e atualizar a data de alteração.
- Avanço de status: aplicar a mesma atualização de status usando o próximo status configurado.
- Atualização em outras telas ou abas: avisar as demais telas interessadas quando um pedido for criado ou alterado?
- Restauração dos dados de exemplo: apagar os pedidos atuais e substituir os dados pelos exemplos originais?
- Avisos e mensagens de erro: devolver mensagens compreensíveis quando uma operação falhar.

## 4. Dúvidas para o professor

- ? O servidor deverá substituir completamente o banco simulado usado no navegador?
- ? A lista de status poderá ser alterada pelo servidor ou permanecerá fixa como no arquivo `statusPedido.json`?
- ? O usuário poderá escolher qualquer status no seletor ou só poderá avançar na ordem definida?
- ? Deve ser possível voltar um pedido para um status anterior?
- ? O status “Cancelado” precisa ter uma ação visível para cancelar pedidos?
- ? O nome do cliente deve ter outras validações além de ser obrigatório?
- ? O campo “Observação” deve aceitar no máximo 140 caracteres também no servidor?
- ? O tipo de consumo deve aceitar somente “local” e “viagem”?
- ? O servidor deve impedir o envio de produtos que ficaram indisponíveis depois que o cardápio foi carregado?
- ? O servidor deve rejeitar quantidades iguais a zero, negativas ou não inteiras?
- ? O servidor deve combinar itens repetidos do mesmo produto caso receba o mesmo produto mais de uma vez?
- ? A restauração dos dados de exemplo deve existir na versão final ou serve apenas para testes?
- ? A atualização automática dos pedidos deverá funcionar entre usuários diferentes ou apenas entre abas do mesmo navegador?
- ? As datas exibidas devem usar o fuso horário do servidor ou o fuso horário do navegador?
- ? A tela de pedidos deverá permitir excluir pedidos ou somente alterar seus status?
