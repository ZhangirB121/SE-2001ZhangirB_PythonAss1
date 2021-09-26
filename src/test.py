from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

r=cg.get_coins_markets(vs_currency='usd')

res=[]
i=int(0)
for x in r:
	i=i+1
	res.append(x['name'])
	if i==15:
		break
	
print(res)