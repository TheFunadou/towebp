# TOWEBP

<div align="center">

```text
  _____ _______          ________ ____  _____  
 |_   _/ __ \ \        / /  ____|  _ \|  __ \ 
   | || |  | \ \  /\  / /| |__  | |_) | |__) |
   | || |  | |\ \/  \/ / |  __| |  _ <|  ___/ 
  _| || |__| | \  /\  /  | |____| |_) | |     
 |_____\____/   \/  \/   |______|____/|_|     
```

**TOWEBP** is a lightweight, high-performance command-line interface (CLI) to convert PNG, JPG, and JPEG images to WebP format.

Developed by [**theFunadou**](https://github.com/theFunadou).

</div>

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/theFunadou/towebp.git
cd towebp

# Install globally or in your environment
pip install .
```

---

## 💻 Usage

```bash
towebp [OPTIONS]
```

### Essential Examples:

- **Convert current directory:**
  ```bash
  towebp
  ```
- **Convert a specific directory recursively:**
  ```bash
  towebp -d ./assets -r
  ```
- **Convert and save in the same directory (instead of a 'webp' subfolder):**
  ```bash
  towebp -o .
  ```

---

## ⚙️ Options

| Option | Shortcut | Default | Description |
|---|---|---|---|
| `--directory` | `-d` | `.` | Root directory to search for images. |
| `--recursive` | `-r` | *Off* | Searches images recursively in subdirectories. |
| `--output-dir`| `-o` | `webp` | Output folder. Use `.` to save next to originals. |
| `--quality`   | `-q` | `80` | WEBP quality (0–100). |
| `--overwrite` | *None*| *Off* | Overwrite existing WebP files. |
| `--help-s`    | `--hs`| *Off* | Show help menu in Spanish. |

---

## 📄 License

Licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
