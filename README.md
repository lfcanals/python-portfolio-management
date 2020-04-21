## Some concepts

### Volatility
To estimate if :
  - we will be able to reach the desired return 
  - it contains the required risk.
 

### Liquidity
Capacity to absorb our entry or exit position, logically this is more important for strategies that handle large positions, but the liquidity of a single contract can be critical at certain times (expiration date, moments of panic, etc.).

### Commissions
The cost of maintain a position or to chenge (open and close it).

### Slippage
Change of the execution price against the order price.
It might imply a profit or a lost.
In a stochastical model, the movement is assumed as random so at the same
volatility, the net effect of the slippafge might be considered zero.

### Correlation
Finally, when we are analyzing different instruments to include in our portfolio of strategies it is necessary to take into account the correlation with possible candidates.

Ideally, we will look for low correlation assets to exploit the same strategy.

### Sharpe ratio
Assuming normal deviation of the returns, it expresses the excess of return we
get assuming the risk of the portfolio/asset.

Mathematically, is the (expectedReturn - riskFreeRate)/stddevOfReturns
