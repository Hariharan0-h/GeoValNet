import numpy as np
import matplotlib.pyplot as plt

actual=np.array([320000,450000,600000,780000,980000])

pred=np.array([330000,440000,570000,700000,860000])

log_price=np.log1p(actual)

residuals=actual-pred

plt.figure(figsize=(7,5))

plt.scatter(log_price,residuals)

plt.axhline(
    0,
    linestyle="--"
)

plt.xlabel("Log Price")

plt.ylabel("Residual")

plt.title("Residuals vs Log Price")

plt.show()