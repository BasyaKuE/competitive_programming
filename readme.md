### テスト
```
oj t -c "python main.py" -d ./tests/
```

### 提出
```
acc s main.py -- -l 5078
# 再帰ある時
acc s main.py -- -l 5055
```

### 次の問題
```
acc add
```

### lint
```
black main.py
flake8 main.py
isort main.py
mypy main.py
```

### 言語
- 4047: PyPy3
- 5078: Python (PyPy 3.10-v7.3.12)

### 参考にしたもの
- https://qiita.com/shun198/items/6dffbb119a3a133b8e3c
- https://github.com/reo11/AtCoder
