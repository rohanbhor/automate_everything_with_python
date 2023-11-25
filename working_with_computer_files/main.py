from pathlib import Path


p1 = Path('task1/ghi.txt')
print(type(p1))


if not p1.exists():
    with open(p1, 'w') as f:
        f.write('content 3')

print(p1.name)
print(p1.stem)
print(p1.suffix)


p2 = Path('task1')
print(list(p2.iterdir()))