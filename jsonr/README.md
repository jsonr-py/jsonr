```
jsonr: (V8.6.6)

Highly customizable JSON objects and dataframes, and your python toolkit all in one.
```

## Installing
```shell
# Linux/macOS
python3 pip install -U jsonr

# Windows
py -3 -m pip install -U jsonr
```

# Architecture
```python
.mailmap
AUTHORS
LICENSE
MANIFEST.in
README.md
SECURITY.md
VERSION
pyproject.toml
setup.cfg
setup.py
jsonr/__init__.py
jsonr/__main__.py
jsonr/help.py
jsonr.egg-info/PKG-INFO
jsonr.egg-info/SOURCES.txt
jsonr.egg-info/dependency_links.txt
jsonr.egg-info/requires.txt
jsonr.egg-info/top_level.txt
jsonr/_core/__init__.py
jsonr/_core/_binary.py
jsonr/_core/_code.py
jsonr/_core/_concurrent.py
jsonr/_core/_crypto.py
jsonr/_core/_data.py
jsonr/_core/_dcompress.py
jsonr/_core/_debug.py
jsonr/_core/_devtools.py
jsonr/_core/_dtypes.py
jsonr/_core/_file.py
jsonr/_core/_formats.py
jsonr/_core/_functional.py
jsonr/_core/_guitk.py
jsonr/_core/_idata.py
jsonr/_core/_import.py
jsonr/_core/_international.py
jsonr/_core/_iprotocols.py
jsonr/_core/_language.py
jsonr/_core/_markup.py
jsonr/_core/_math.py
jsonr/_core/_mswindows.py
jsonr/_core/_mutimedia.py
jsonr/_core/_networking.py
jsonr/_core/_os.py
jsonr/_core/_packaging.py
jsonr/_core/_program.py
jsonr/_core/_runtime.py
jsonr/_core/_superseded.py
jsonr/_core/_text.py
jsonr/_core/_unix.py
jsonr/_typing/__init__.py
jsonr/_typing/jsonr_typing_flowa.py
jsonr/_typing/jsonr_typing_json.py
jsonr/_typing/jsonr_typing_pollinations.py
jsonr/_typing/jsonr_typing_string.py
jsonr/_utils/__init__.py
jsonr/_utils/_bond.py
jsonr/_utils/_convertions.py
jsonr/_utils/_infinity.py
jsonr/_utils/_insepct.py
jsonr/bases/__init__.py
jsonr/bases/new_base.py
jsonr/core/__init__.py
jsonr/core/dataframe.py
jsonr/core/new.py
jsonr/libs/__init__.py
jsonr/libs/flowa/__init__.py
jsonr/libs/flowa/_version.py
jsonr/libs/flowa/main/__init__.py
jsonr/libs/flowa/main/decisiontree.py
jsonr/libs/flowa/main/imagemodel.py
jsonr/libs/flowa/main/labelencoder.py
jsonr/libs/flowa/types/__init__.py
jsonr/libs/flowa/utils/__init__.py
jsonr/libs/pollinations/__init__.py
jsonr/libs/pollinations/abc/__init__.py
jsonr/libs/pollinations/abc/imageprotocol.py
jsonr/libs/pollinations/abc/textprotocol.py
jsonr/libs/pollinations/ai/__init__.py
jsonr/libs/pollinations/ext/__init__.py
jsonr/libs/pollinations/types/ImageModel.py
jsonr/libs/pollinations/types/ImageObject.py
jsonr/libs/pollinations/types/TextModel.py
jsonr/libs/pollinations/types/TextObject.py
jsonr/libs/pollinations/types/__init__.py
jsonr/typing/__init__.py
jsonr/utils/__init__.py
test/test_import.py
```

## JSON Objects
```python
import jsonr

json: jsonr.JSON = jsonr.New(auto=True, some_var='thanks for using jsonr!', other_var='im a random var!', lol='lol')
```
```javascript
// >>> {'some_var': 'thanks for using jsonr!', 'other_var': 'im a random var!', 'lol': 'lol'}
```
```python
json.test: int = 123

print(json['test'])
```
```javascript
// >>> 123
```
```python
json_copy: dict = json.copy()

new_json: jsonr.JSON = jsonr.New()
new_json.to(json_copy)

print(new_json)
```
```javascript
// >>> {'some_var': 'thanks for using jsonr!', 'other_var': 'im a random var!', 'lol': 'lol', 'test': 123}
```
```python
json.wipe()
```
```javascript
// >>> {}
```
For more JSON Object Examples view the [jsonr/examples](https://github.com/jsonr-py/jsonr/blob/master/examples)

## DataFrame Objects
```python
frame = jsonr.Frame(columns=["1A TEST-A", "B", "C"], rows=[[1, 2, 3], [4, 5, 6]])
```
```javascript
// >>>      | 1A TEST-A | B | C
// >>> -----------------------
// >>> 0    |         1 | 2 | 3
// >>> 1    |         4 | 5 | 6
```
```python
print(frame._1A_TEST_A)
```
```javascript
// >>> [1, 4]
```
```python
frame.add_row([7, 8, 9])
```
```javascript
// >>>      | 1A TEST-A | B | C
// >>> -----------------------
// >>> 0    |         1 | 2 | 3
// >>> 1    |         4 | 5 | 6
// >>> 2    |         7 | 8 | 9
```
```python
frame.add_column("D", [10, 11, 12])
```
```javascript
// >>>      | 1A TEST-A | B | C |  D
// >>> ----------------------------
// >>> 0    |         1 | 2 | 3 | 10
// >>> 1    |         4 | 5 | 6 | 11
// >>> 2    |         7 | 8 | 9 | 12
```
```python
X: list = frame.drop(columns=['B', 'C']) # Creates a new dataframe to not alter the original frame.
```
```javascript
// >>>      | 1A TEST-A |  D
// >>> --------------------
// >>> 0    |         1 | 10
// >>> 1    |         4 | 11
// >>> 2    |         7 | 12
```
```python
print(frame.describe())
```
```javascript
// >>> {'1A TEST-A': {'count': 3, 'mean': 4.0, 'std': 2.449489742783178, 'min': 1, '25%': 1, '50%': 4, '75%': 7, 'max': 7}, 'B': {'count': 3, 'mean': 5.0, 'std': 2.449489742783178, 'min': 2, '25%': 2, '50%': 5, '75%': 8, 'max': 8}, 'C': {'count': 3, 'mean': 6.0, 'std': 2.449489742783178, 'min': 3, '25%': 3, '50%': 6, '75%': 9, 'max': 9}, 'D': {'count': 3, 'mean': 11.0, 'std': 0.816496580927726, 'min': 10, '25%': 10, '50%': 11, '75%': 12, 'max': 12}}
```

For more DataFrame Object Examples view the [jsonr/examples](https://github.com/jsonr-py/jsonr/blob/master/examples)

## Links
GitHub = https://github.com/jsonr-py
Repository = https://github.com/jsonr-py/jsonr
PyPi = https://pypi.org/project/jsonr
