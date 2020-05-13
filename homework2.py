from pathlib import Path

p = Path('.')
for x in p.iterdir():
  if x.is_dir():
    print(x)
list(p.glob('**/*.mp3'))
