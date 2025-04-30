# Relatório de Teste – SauceDemo

## TC-001: Login Bem-sucedido
- **Objetivo:** Verificar login com credenciais válidas.
- **Passos Executados:**
  1. Acessar https://www.saucedemo.com/
  2. Inserir usuário `standard_user`
  3. Inserir senha `secret_sauce`
  4. Clicar no botão de login
  5. Verificar se a URL contém `/inventory`
- **Dados de Entrada:**
  - Usuário: `standard_user`
  - Senha: `secret_sauce`
- **Resultado Esperado:** Página de inventário carregada.
- **Resultado Obtido:** Página acessada com sucesso.
- **Status:** ✅ Passou
- **Início/Fim:** `10:23:10 / 10:23:14`
- **Duração:** 4s

---

## TC-002: Login Mal-sucedido
- **Objetivo:** Verificar erro de login com dados inválidos.
- **Passos Executados:**
  1. Inserir usuário `invalid_user`
  2. Inserir senha `wrong_password`
  3. Clicar no botão de login
  4. Validar mensagem de erro
- **Dados de Entrada:** `invalid_user / wrong_password`
- **Resultado Esperado:** Mensagem de erro exibida.
- **Resultado Obtido:** `"Epic sadface: Username and password do not match"`
- **Status:** ✅ Passou
