# Aplicativo de Tradução com Interface Gráfica

Este projeto é uma **Interface Gráfica de Usuário (GUI)** para tradução de textos, desenvolvida em Python utilizando a biblioteca **Tkinter**. O aplicativo utiliza a **API do Google Translator** para realizar traduções entre diferentes idiomas, oferecendo uma forma intuitiva e interativa de traduzir textos.

---

## Funcionalidades

- **Interface Amigável**: Desenvolvido com `Tkinter`, possui uma interface simples e fácil de usar.
- **Seleção de Idiomas**: Menus suspensos permitem selecionar o idioma de entrada e saída.
- **Atualização em Tempo Real**: Rótulos atualizados dinamicamente para refletir os idiomas selecionados.
- **Área de Texto**: Áreas de entrada e saída para facilitar a digitação e visualização do texto.
- **Barras de Rolagem**: Barras de rolagem integradas para suportar textos longos.
- **Botão de Tradução**: Um clique no botão aciona o processo de tradução.

---

## Pré-Requisitos

### Bibliotecas Necessárias

- **Tkinter**: Já vem instalado com o Python.
- **GoogleTrans**: Instale com o comando:
  ```bash
  pip install googletrans==4.0.0-rc1
  ```

---

## Instruções de Configuração

1. Clone este repositório ou copie o código para um arquivo Python (ex.: `tradutor.py`).
2. Instale as dependências necessárias.
3. Certifique-se de ter as imagens `languages.png` e `exchange.png` em uma pasta chamada `image`, localizada no mesmo diretório do script.
4. Execute o arquivo Python:
   ```bash
   python tradutor.py
   ```

---

## Como Usar

1. **Selecionar Idiomas**: Use os menus suspensos na parte superior para escolher os idiomas de entrada e saída.
2. **Inserir Texto**: Digite o texto a ser traduzido na área de texto à esquerda.
3. **Traduzir**: Clique no botão `Translate`. O texto traduzido será exibido na área de texto à direita.

---

## Visão Geral do Código

1. **Componentes Tkinter**: A interface é construída com widgets `Tkinter`, como `Label`, `Text`, `Button` e `Combobox`.
2. **API Google Translator**: Utiliza a biblioteca `googletrans` para realizar as traduções.
3. **Mudança Dinâmica de Idiomas**: A função `label_change` mantém os rótulos sincronizados com as seleções dos menus suspensos.
4. **Barras de Rolagem**: Adicionadas às áreas de texto para melhorar a usabilidade com textos longos.

---

## Limitações

- Requer conexão com a internet para realizar traduções.
- Limitado pelas capacidades e restrições da biblioteca `googletrans`.
- Pode apresentar problemas caso a API do `googletrans` seja atualizada ou descontinuada.

---

## Melhorias Futuras

- Adicionar suporte a entrada e saída de voz.
- Incluir um recurso de histórico para salvar traduções anteriores.
- Melhorar o tratamento de erros para lidar com idiomas não suportados ou problemas de conectividade com a API.

---

## Licença

Este projeto é open-source e está disponível sob a licença MIT. Sinta-se à vontade para modificar e compartilhar.

---

## Agradecimentos

- **Google Translate API** por possibilitar a funcionalidade de tradução.
- **Tkinter** por fornecer uma forma simples de criar aplicativos GUI em Python.
