# ase2alm
ASEのAtomsオブジェクトからALAMODEのinputファイルを作る

Atoms オブジェクトを与えるか、ase.ioを使っているのでase.ioで読めるファイル形式ならなんでも可。

## 使い方
```python
python ase2alm.py --a (cifファイルなど) -f (outputのfilename) -p (prefix)
```
MODEなどは書いてない。構造から書けるところだけ書いてある。
