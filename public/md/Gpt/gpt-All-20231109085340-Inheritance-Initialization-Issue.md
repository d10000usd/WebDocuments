# **<span style="font-size: 35px; font-style: italic;">Inheritance Initialization Issue</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-39.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 3</div></div>
It appears that you're facing an issue with your Python code, specifically related to the `__init__` method not being called from the base class 'SavePath'. To fix this, you need to explicitly call the base class's `__init__` method in the derived class using `super().__init__()`. Here's how you can modify your `DownloadOhlc` class to ensure the `__init__` method from 'SavePath' is called:

```python
import yfinance as yf
from commonclass import FileReader as fr

class DataSupper:
    """Super Class"""
    tickerCode = None
    tickerName = None
    selected_stock = ['^KQ11','^KS11','086520.KQ','009520.KQ','066970.KQ']
    
    def __init__(self):
        self.lastname = "홍"

class SavePath:
    """Super Class"""
    configpath = "/Users/hg/DEV/CloudDocuments/public/lib/json/config.json"
    
    def __init__(self):
        self.lastname = "홍"

class LocalFileReader(SavePath):
    """Inherited Class"""
    
    def __init__(self):
        super().__init__()  # Call the base class's __init__ method
        self.config = fr.read_file(SavePath.configpath)
        self.path1 = "홍"
        self.path3 = "1"

class DownloadOhlc(DataSupper, LocalFileReader):
    """Inherited Class"""
    
    def __init__(self):
        super().__init__()  # Call the base class's __init__ method
        self.path2 = "홍"
        self.path3 = DataSupper.tickerCode
        self.config = LocalFileReader.config

# Now the base class's __init__ methods are called in the derived class constructors.
```

By using `super().__init__()`, you ensure that the base class's `__init__` method is called, allowing you to initialize attributes and properties from the base classes.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-33.png)  
* Inheritance Initialization Issue  
* 20231109085340  
* Description for dev  
* #keyword  
****
Here's how you can modify your `DownloadOhlc` class to ensure the `__init__` method from 'SavePath' is called:

```python
import yfinance as yf
from commonclass import FileReader as fr

class DataSupper:
    """Super Class"""
    tickerCode = None
    tickerName = None
    selected_stock = ['^KQ11','^KS11','086520.KQ','009520.KQ','066970.KQ']
    
    def __init__(self):
        self.lastname = "홍"

class SavePath:
    """Super Class"""
    configpath = "/Users/hg/DEV/CloudDocuments/public/lib/json/config.json"
    
    def __init__(self):
        self.lastname = "홍"

class LocalFileReader(SavePath):
    """Inherited Class"""
    
    def __init__(self):
        super().__init__()  # Call the base class's __init__ method
        self.config = fr.read_file(SavePath.configpath)
        self.path1 = "홍"
        self.path3 = "1"

class DownloadOhlc(DataSupper, LocalFileReader):
    """Inherited Class"""
    
    def __init__(self):
        super().__init__()  # Call the base class's __init__ method
        self.path2 = "홍"
        self.path3 = DataSupper.tickerCode
        self.config = LocalFileReader.config

# Now the base class's __init__ methods are called in the derived class constructors.
```

By using `super().__init__()`, you ensure that the base class's `__init__` method is called, allowing you to initialize attributes and properties from the base classes.



<div style="background-color: grey; height: 15px;"></div>

  
</div> 
