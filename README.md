# Real-Fake-Random-User-Agent

[`GetRandomUserAgent()`](https://github.com/ewwink/Real-Fake-Random-User-Agent/blob/main/rfrua.py#L8) generate fake random browser User-Agent, it has limited random generation (Thousands UA) but produced like real User-Agent.

## Browser List
- Firefox Version 93-104
- Chrome Version 93-104
- Opera Version 80-89
- Edge Version 93-104

it also generate number of `patch` and `build`

## Operating System
- Windows
- Linux
- MacOS


## How To

simply include `rfrua.py` or copy paste the content to your project

```python
from rfrua import GetRandomUserAgent

print(GetRandomUserAgent())
print(GetRandomUserAgent())
print(GetRandomUserAgent())
print(GetRandomUserAgent())
```

output
```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.5021.188 Safari/537.36 EDG/101.0.1140.66
Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.5149.148 Safari/537.36 EDG/98.0.1235.55
Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.5072.134 Safari/537.36 OPR/80.0.3918.183
```
