import pandas as pd
import pdf_code

df=pd.read_csv('articles.csv')

class Product:
    def __init__(self, pid):
            self.pid=pid
            self.price=df.loc[df['id']==self.pid,'price'].squeeze()
            self.prod_name=df.loc[df['id']==self.pid,'name'].squeeze()

    def checkStock(self,buy_amount):
        current_stock=df.loc[df['id']==self.pid,'in stock'].squeeze()
        if buy_amount<=current_stock:
            return  True
        else:
            return  False

    def Buy(self,buy_amount):
        new_stock=df.loc[df['id']==self.pid,'in stock'].squeeze()-buy_amount
        df.loc[df['id']==self.pid,'in stock']=new_stock
        df.to_csv('articles.csv',index=False)

class Receipt:
    def __init__(self,buy_amount,pro_obj):
        self.buy_amount=buy_amount
        self.prod=pro_obj

    def generate(self):
        content=[]
        content.append(f"Receipt nr.{str(self.prod.pid)}")
        content.append(f"Article: {self.prod.prod_name}")
        content.append(f"Price: $.{str(self.prod.price)}")
        content.append(f'Buy Amounts: {str(self.buy_amount)}')
        content.append(f"Total is $.{str(self.prod.price*self.buy_amount)}")
        return content

print(df)
try:
    product_id=int(input('Choose the article to buy: '))
    if product_id in df['id'].values:
        product=Product(product_id)
        buy_amount=int(input('How many do you want to buy? '))
        if product.checkStock(buy_amount):
            product.Buy(buy_amount)
            receive_receipt=Receipt(buy_amount=buy_amount,pro_obj=product)
            receipt_content=receive_receipt.generate()
            pdf_code.pdf_generator(receipt_content)
        else:
            print('Sold out!')
    else:
        print("This product not exist.")
except ValueError:(
    print("You should enter product's number."))
