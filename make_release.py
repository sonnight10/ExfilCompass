"""Prépare une nouvelle version à publier : python make_release.py
1. change __version__ dans exfilcompass/__init__.py (ex. 1.1.0), 2. lance build_exe.bat,
3. lance ce script : il crée ExfilCompass-<version>.zip (+ .sha256) à partir de dist/ExfilCompass.exe (l'exe est un fichier unique),
4. sur GitHub : Releases > Draft a new release, tag v<version>, joins le .zip (et le .sha256), Publish."""
import hashlib
import re
import sys
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
version = re.search(r'__version__ = "([^"]+)"', (root / "exfilcompass" / "__init__.py").read_text(encoding="utf-8")).group(1)
exe = root / "dist" / "ExfilCompass.exe"
if not exe.exists():
    sys.exit("dist/ExfilCompass.exe introuvable : lance d'abord build_exe.bat.")
zip_path = root / "dist" / f"ExfilCompass-{version}.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:     # l'exe est seul à la racine (le logiciel sait installer ça)
    z.write(exe, "ExfilCompass.exe")
sha = hashlib.sha256(zip_path.read_bytes()).hexdigest()
(zip_path.parent / (zip_path.name + ".sha256")).write_text(f"{sha}  {zip_path.name}\n", encoding="utf-8")
print(f"Version {version}\nFichier : {zip_path}\nSHA-256 : {sha}\nPublie-le comme Release GitHub avec le tag v{version}.")
