print("""
# [jsonr - PyPi](https://pypi.org/project/jsonr)

```
flowa: (V8.5.2)

Python Highly customizable JSON objects and dataframes, and more!
```

## Installing
```shell
# Linux/macOS
python3 pip install -U jsonr

# Windows
py -3 -m pip install -U jsonr
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
""")
