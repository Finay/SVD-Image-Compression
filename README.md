SVD-Image-Compression
---
A demonstration of how a singular value decomposition can be used in image compression. The idea behind using SVDs for 
image compression is not my own, this demo was made to help others better understand the linear algebra behind the 
process. 

### Usage
Setup
```bash
$ pip install -r requirements.txt
```
Run the main image compression demo
```bash
$ python3 main.py
```
Run the SVD demo
```bash
$ python3 svd_demo.py
```

### Example
![Demo Image](https://github.com/Finay/SVD-Image-Compression/blob/main/images/DEMO.png)

### Modifying
The image utilized for the compression demo is located in the image folder of the project. To use a different image,
replace the image there or change the input filepath in the `main.py` file.