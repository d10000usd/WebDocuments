Title - Add Key-Value Pairs


<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-37.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
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

