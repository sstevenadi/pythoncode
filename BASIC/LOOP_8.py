print ('----------------------------------------------------------')

print ('Jumlah telur pada bulan ke-1 = 0 / 0.0 kg')
print ('Jumlah telur pada bulan ke-2 = 0 / 0.0 kg')

for a in range (18):
    t = 270*a
    b = t/16
    print ('Jumlah telur pada bulan ke-{} = {} / {} kg'.format((a+3),t,b))

print ('----------------------------------------------------------')

u = b*14500
beli = 150000*3
p = 200000*20
tot = u-beli-p

print ('Total telur yang dihasilkan {} kg'.format(b))
print ('Total keuntungan adalah Rp {}'.format(round(tot,0)))