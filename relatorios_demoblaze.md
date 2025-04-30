# Relatório de Teste – Demoblaze

## TC-004: Compra de Produto
- **Objetivo:** Simular uma compra completa.
- **Passos Executados:**
  1. Acessar https://www.demoblaze.com/
  2. Selecionar produto “Samsung galaxy s6”
  3. Adicionar ao carrinho
  4. Aceitar alerta
  5. Ir ao carrinho e clicar em “Place Order”
  6. Preencher formulário com dados fictícios
  7. Confirmar compra e capturar texto do modal
- **Dados de Entrada:**
  - Nome: João Silva
  - País: Brasil
  - Cartão: 1234567812345678
- **Resultado Esperado:** Confirmação de pedido.
- **Resultado Obtido:**
  - Texto do modal: `Thank you for your purchase!`
- **Status:** ✅ Passou
