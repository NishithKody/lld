class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        chk = set()
        map = defaultdict(list)

        for i,txn in enumerate(transactions):
            [name,time,amt,city] = txn.split(',')
            map[name].append((time,city,i))

            if(int(amt)>1000):
                chk.add(i)

            for [tm,ct,ind] in map[name]:
                if(ct!=city and abs(int(tm)-int(time))<=60):
                    chk.add(ind)
                    chk.add(i)
        res = []
        
        for index in chk:
            res.append(transactions[index])
        
        return res
