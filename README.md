## Dataset Size

This data set includes about 3349 versions of the source code of 2839 malicious packages.

## Dataset Format

`package name -> version -> source code zip file.`

Example:
`ython-binance -> 0.1 -> ython-binance-0.1.tar.gz`

## False positive

We have manually checked all collected malicious packages and have now removed all false positives.

## Reference

This dataset is the work of the ASE 2023 paper "An Empirical Study of Malicious Code In PyPI Ecosystem"

```
@misc{guo2023empirical,
      title={An Empirical Study of Malicious Code In PyPI Ecosystem}, 
      author={Wenbo Guo and Zhengzi Xu and Chengwei Liu and Cheng Huang and Yong Fang and Yang Liu},
      year={2023},
      eprint={2309.11021},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```

## Update

### 31 Mar. 2024 
Add new 431 malicious packages using typoSquatting attack method.

ref: [https://mp.weixin.qq.com/s/VIThE0I5BkQBW6hIOubnkQ](https://mp.weixin.qq.com/s/VIThE0I5BkQBW6hIOubnkQ)


### 04 Apr. 2024 
Add new 45 malicious packages using typoSquatting attack method.
