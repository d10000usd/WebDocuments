# **<span style="font-size: 35px; font-style: italic;">Add Key-Value Pairs</span>**

> ## 1
Here's the Python code that achieves the described task:

```python
asdf = { "text": "kown"}
for a, b in seo_dict.items():
    asdf[a] = b
print(asdf)
```

This code will add the key-value pairs from the `seo_dict` dictionary to the `asdf` dictionary where the value of the `"text"` key is `"kown"`.
*****



> ## 2
I apologize for the confusion earlier. If you want to use a `while` loop to achieve this, you can do it like this:

```python
asdf = { "text": "kown"}
iterator = iter(seo_dict.items())
while True:
    try:
        a, b = next(iterator)
        asdf[a] = b
    except StopIteration:
        break
print(asdf)
```

This code will also add the key-value pairs from the `seo_dict` dictionary to the `asdf` dictionary where the value of the `"text"` key is `"kown"`.
*****



