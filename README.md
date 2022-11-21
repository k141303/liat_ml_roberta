# liat_ml_roberta
Multi-Language RoBERTa trained by RIKEN-AIP LIAT.  
**This repository is not yet complete.**

## How to install

Can use pypi to install.

~~~bash
pip install liat_ml_roberta
~~~

## How to use

~~~python
from liat_ml_roberta import RoBERTaTokenizer


def main():
    tokenizer = RoBERTaTokenizer.from_pretrained(version="en_20190121_m10000_v24000_base")
    print(tokenizer.tokenize("This is a pen."))


if __name__ == "__main__":
    main()
~~~

## Versions

|name|lang|size|bpe merges|vocab size|wikipedia version|  
|:---:|:---:|:---:|:---:|:---:|:---:|  
|ja_20190121_m10000_v24000_base|ja|base|10000|24000|20190121|  
|en_20190121_m10000_v24000_base|en|base|10000|24000|20190121|  
