# Copilot Instructions for PiTU (Calculador de Tamanho de Subdiretórios)

## Project Overview
PiTU is a Python desktop application that calculates directory sizes with a modern GUI using CustomTkinter. It features two main components:
- `main.py`: Splash screen launcher with fade animations and main application entry point
- `tamanho.py`: Core directory size calculator with SQLite storage, threading, and data visualization

## Architecture Patterns

### GUI Framework Stack
- **CustomTkinter** for modern UI components (buttons, labels, frames)
- **tkinter.ttk** for complex widgets (Treeview tables, progress bars) that aren't yet available in CustomTkinter
- **PIL/ImageTk** for image handling in splash screens
- Mixed usage is intentional - use `ctk.*` for basic controls, `ttk.*` for data tables/progress

### Performance & Threading
- **SQLite** (`tamanhos.db`) for memory-efficient storage of large directory scans
- **ThreadPoolExecutor** with `os.cpu_count()` workers for parallel directory traversal
- Progress updates every 10 items via `janela.update_idletasks()` to maintain UI responsiveness
- Background threading for splash screen animations using `daemon=True`

### Data Visualization
- **Matplotlib** embedded via `FigureCanvasTkAgg` for charts within CustomTkinter frames
- Top 10 largest directories + "Outros" (Others) aggregation pattern
- Dynamic color mapping using `coolwarm` colormap with normalized values
- Size conversion hierarchy: Bytes → KB → MB → GB → TB

## Development Workflows

### Dependencies & Environment
```bash
pip install customtkinter matplotlib
```
Python 3.10+ required for modern features.

### Building Executable
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole tamanho.py
```
Use `--noconsole` to hide terminal window for end users.

### Database Management
- SQLite database (`tamanhos.db`) is recreated on each scan via `DROP TABLE IF EXISTS`
- Batch inserts using `executemany()` for performance
- No migration patterns - database is transient storage

## Key Conventions

### File Organization
- `main.py`: Application launcher with splash screen
- `tamanho.py`: Standalone calculator (can run independently)
- `splashscreen.png`: Required for splash screen (graceful fallback to text)
- `requirements.txt`: Minimal dependencies only

### Error Handling Patterns
- `FileNotFoundError` and `PermissionError` are caught and ignored during directory traversal
- Graceful image loading fallback: PNG → text label
- Directory selection cancellation handling via `if not diretorio: return`

### Internationalization
- Portuguese UI labels and messages throughout
- File size units in Portuguese: "Bytes", "KB", "MB", "GB", "TB"
- Variable names mix Portuguese (`tamanho`, `diretorio`) and English

### UI Patterns
- Dark theme default: `ctk.set_appearance_mode("dark")`
- Window sizing: 600x400 for splash, 800x750 for main, 1000x700 for future modules
- Center positioning using screen dimensions calculation
- Progress feedback for long operations via ttk.Progressbar

## Integration Points
- Splash screen launches main calculator via `abrir_pitu()` function
- Future modular design indicated in README - `tamanho.py` will become a module
- No external API dependencies - fully offline application
- File system integration through `os.walk()` and `filedialog`

## Testing & Debugging
No test suite present. Manual testing approach:
- Test with various directory sizes and permissions
- Verify SQLite performance with large datasets
- Check UI responsiveness during long scans
- Validate executable generation on target platforms