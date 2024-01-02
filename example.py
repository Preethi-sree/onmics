import pandas as pd
fruits=['apple','banana','cherry','dragon fruit','fig']
quantity=[1200,3000,50000,123,780]
price=[20.00,10.00,5.00,100.00,50.00]
data=pd.DataFrame({"fruits":fruits,"quantity":quantity, "price":price})
print(data)
data.to_excel("fruit")