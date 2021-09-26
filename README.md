# PythonUsingApi
Here I am using coingecko.com Api



<h2>Installation</h2>

```
pip install pycoingecko
```

or

```
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

<h2>Usage </h2>

```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

<h2>Examples</h2>

You can find full information about this API in this site https://www.coingecko.com/api/docs/v3

cg.get_coins_list - It will return list of all coins with id, name and symbol.

cg.get_coins_markets(*currency*) - It will return list of all coins with price, market cap, volume and market related data.
