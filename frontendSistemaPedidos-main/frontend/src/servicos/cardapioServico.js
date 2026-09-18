const API_URL = 'http://localhost:8000';

async function listarItens() {
  const resposta = await fetch(`${API_URL}/itens/`);
  if (!resposta.ok) throw new Error('Não foi possível carregar o cardápio.');
  return resposta.json();
}

// GET /categorias
export function listarCategorias() {
  return listarItens().then((itens) =>
    [...new Set(itens.map((item) => item.categoria))].map((categoria, ordem) => ({
      id: categoria,
      nome: categoria[0].toUpperCase() + categoria.slice(1),
      icone: '🍽️',
      ordem: ordem + 1,
    })),
  );
}

// GET /produtos?disponivel=true
export function listarProdutos() {
  return listarItens().then((itens) =>
    itens.map((item) => ({
      ...item,
      categoriaId: item.categoria,
      descricao: 'Produto disponível no cardápio.',
      imagem: '',
      destaque: false,
      disponivel: true,
    })),
  );
}
