class Tier(object):
    """Tier represents a limit and a function for the rate above that value and below the next value. All values above the last tier are expected to fall into that tier. 
    """
    def __init__(self, lim, func):
        self.lim = lim
        self.func = func
#extier = Tier(500, '(.05)*(x-500)')
#print(extier)

class Offer(object):
    """Offer is the extent of an offer from a utility to a residential customer. The class requires basic information and can be extended to add all of the rate tiers in the offer. The get_bill() method will return the cost for a given usage from this offer.
    """
    def __init__(self, name, utility, tariff, url, base=0, tiers=[Tier]):
        self.name = name        # name of offer
        self.utility = utility  # utility providing offer
        self.tariff = tariff    # the code on the fact sheet
        self.url = url          # where the fact sheet can be found
        self.base = base
        self.tiers = tiers
    def get_tiers(self):
        for tier in self.tiers:
            print("when usage is > than: " + str(tier.lim) +" rate is" + str(tier.func))
    def calc_bill(self, x):
        def num(s):
            try:
                return int(s)
            except ValueError:
                return float(s)
        base = self.base
        print("base is: " + str(base))
        for tier in self.tiers:
            if x > num(tier.lim): 
                result = eval(tier.func)
                print("x is %s, using %s" % (str(x), tier.func))
                print(result)
        return result
        
          
example = Offer('example_name', 'utility', 'abc123-10abcd-ef','url', '10',
            [Tier(500, '(.05)*(x-500)'), 
            Tier(1500, '(.05)*(1000) + (.03)*(x-1500)'), 
            Tier(2500, '(.10)*(x-2500)')])
print(example)
print(example.get_tiers())
print(example.calc_bill(x = 1800))
example2 = Offer('example_name2', 'utility2', 'xyz123-10abcd-ef','url.com', '100',
            [Tier(0, 'base'),
            Tier(500, '100 + (.12)*(x-500)'), 
            Tier(1500, '(.12)*(1500) + (.03)*(x-1500)'), 
            Tier(2000, '(.10)*(x-2000)')])
print(example2)
print(example2.get_tiers())
print(example2.calc_bill(x = 100))
print(example2.calc_bill(x = 1800))
