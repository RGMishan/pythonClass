class health_care():
    print("\nHealth_Care Domain")
    def price():
        print("\nMust be implemented in child class")
        
class medicine(health_care):
    def price(self,item,no_items,price,gst):
        self.item = item
        self.no_items = no_items
        self.price = price
        self.gst = gst
    def price_val(self):
        c = (self.no_items)*(self.price)*(self.gst)
        return c
class materials(health_care):
        
    def price(self,item,no_items,price,gst):
        self.item = item
        self.no_items = no_items
        self.price = price
        self.gst = gst
    def price_val(self):
        l = (self.no_items)*(self.price)*(self.gst)
        return l
class liquids(health_care):
    def price(self,item,no_items,price,gst):
        self.item = item
        self.no_items = no_items
        self.price = price
        self.gst = gst
    def price_val(self):
        m = (self.no_items)*(self.price)*(self.gst)
        return m

type_med = 0.2
type_materials = 0.5
type_liquids = 0.9


item = input("Item_name= ")
no_items = input("\nNo of items : ")
price = input("\nEnter price")


h = health_care()
med = medicine()
med.price(item,int(no_items),int(price),int(type_med))
q = med.price_val()

item = input("Item_name= ")
no_items = input("\nNo of items : ")
price = input("\nEnter price ")
mat = materials()
mat.price(item,int(no_items),int(price),int(type_materials))
r = mat.price_val()

item = input("Item_name= ")
no_items = input("\nNo of items: ")
price = input("\nEnter price")
liq = liquids()
liq.price(item,int(no_items),int(price),int(type_liquids))
s = liq.price_val()

v = int(q) + int(r) + int(s)
print("\nTotal Price {}".format(v))
