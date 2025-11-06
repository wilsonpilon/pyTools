# 📂 Calculador de Tamanho de Subdiretórios (CustomTkinter)

Este utilitário em **Python** calcula o tamanho de cada subdiretório em um diretório selecionado, exibindo os resultados em uma interface gráfica moderna com **CustomTkinter**.

> ⚠️ Este utilitário será **integrado em uma ferramenta maior em breve**, com recursos adicionais como exportação para CSV/Excel, paginação e gráficos complementares.

---

## ✅ Funcionalidades

- Interface gráfica moderna via **CustomTkinter** (modo claro/escuro).
- Seleção interativa de diretório.
- Cálculo otimizado:
  - **Multithread** para velocidade.
  - **SQLite** para reduzir uso de memória em diretórios grandes.
- Resultados em:
  - **Tabela ordenada** por tamanho.
  - **Tamanho total do diretório**.
- Gráfico dinâmico:
  - Mostra **Top 10 maiores diretórios**.
  - Inclui segmento **“Outros”** (soma dos menores).
  - Paleta gradiente de vermelho a azul.
- Barra de progresso.

---

## 🔧 Tecnologias e dependências

- **Python 3.10+**
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Matplotlib](https://matplotlib.org/)
- **SQLite** (banco embutido, via `sqlite3` da biblioteca padrão)
- **tkinter** (interface padrão em Python)
- **ThreadPoolExecutor** (concorrência, da biblioteca padrão)
- **ttk** (componentes de interface, da biblioteca padrão)

**Instale as dependências via:**

```bash
pip install customtkinter matplotlib
```

---

## ▶️ Como executar

1. Instale as dependências:

   ```bash
   pip install customtkinter matplotlib
   ```

2. Baixe o repositório ou apenas o arquivo `tamanho.py`.

3. Execute o script:

   ```bash
   python tamanho.py
   ```

---

## 💻 Gerar executável com PyInstaller

1. Instale o PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Gere o executável:

   ```bash
   pyinstaller --onefile --noconsole tamanho.py
   ```

   - O executável estará em `dist/tamanho.exe` (Windows) ou `dist/tamanho` (Linux/Mac).
   - O argumento `--noconsole` oculta o terminal.

3. Para rodar o executável:

   ```bash
   ./dist/tamanho.exe
   # ou no Linux/Mac
   ./dist/tamanho
   ```

---

## 📦 Como empacotar em formato .zip

1. Gere o executável pelo passo anterior.
2. Localize o arquivo na pasta `dist/`.
3. Empacote o arquivo em `.zip` junto de qualquer arquivo extra (como banco de dados ou README):

   - Windows (prompt):

     ```cmd
     cd dist
     powershell Compress-Archive -Path tamanho.exe,../README.md -DestinationPath tamanho.zip
     ```

   - Linux/Mac (terminal):

     ```bash
     cd dist
     zip tamanho.zip tamanho README.md
     ```

4. O arquivo `tamanho.zip` estará pronto para distribuição.

---

## 🔗 Links úteis

- [CustomTkinter Docs](https://github.com/TomSchimansky/CustomTkinter)
- [Matplotlib Docs](https://matplotlib.org/)
- [GitHub do Projeto](https://github.com/wilsonpilon/pyTools)
