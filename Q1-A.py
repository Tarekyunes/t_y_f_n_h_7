# Question 1:
# A- If you have two lists, ##L1=[‘HTTP’,’HTTPS’,’FTP’,’DNS’],L2=[80,443,21,53] convert it to generate this
# dictionary d={‘HTTP’:80,’HTTPS’:443,’FTP’:21,’DNS’:53 }

l1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
l2 = [80, 443, 21, 53]
d = dict(zip(l1, l2))
print(d)
