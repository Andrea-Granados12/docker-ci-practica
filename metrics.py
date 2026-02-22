from pathlib import Path

EXTS = {".py"}

def count_lines(file_path: Path):
    total = 0
    code = 0
    comments = 0
    blank = 0

    for line in file_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        total += 1
        s = line.strip()
        if s == "":
            blank += 1
        elif s.startswith("#"):
            comments += 1
        else:
            code += 1

    return total, code, comments, blank

def main():
    root = Path(__file__).parent
    py_files = sorted([p for p in root.rglob("*") if p.suffix in EXTS and ".venv" not in str(p)])

    grand_total = grand_code = grand_comments = grand_blank = 0

    print("MÉTRICAS (Python) - Conteo de líneas")
    print("-" * 60)

    for f in py_files:
        total, code, comments, blank = count_lines(f)
        grand_total += total
        grand_code += code
        grand_comments += comments
        grand_blank += blank

        rel = f.relative_to(root)
        print(f"{rel}: total={total}, código={code}, comentarios={comments}, vacías={blank}")

    print("-" * 60)
    print(f"TOTAL PROYECTO: total={grand_total}, código={grand_code}, comentarios={grand_comments}, vacías={grand_blank}")

if __name__ == "__main__":
    main()
