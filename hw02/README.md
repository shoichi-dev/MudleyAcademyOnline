
# config
```
symbol = "BTC-PERPETUAL"
timeFrame = "1h"
apiKey = "K0dNactS"
secret = "NGsHWQPlozOrWNbaYUklFZA573iDnpL2haSzd4ODqr0"
```

# Set zone  an=a1+(n−1)d
```
high_edge = 15000
low_edge = 5000
quota = 100  # 1 นัด = 10$ = 1000$
usd_size = 10  # 10$
gap_zone = 100  # ~101.0101...
```


# การทำงานของโปรแกรม
1. เช็ค position ที่เปิดอยู่และที่ pending
2. เช็คเทียบกับโซนว่ากระสุนมากหรือน้อยกว่า
3. เปิดออเดอร์โดยการ pending buy limit ที่แนวรับจากการคำนวน pivot point
4. ปิดตามโซนจากการคำนวนเลขอนุกรม

# สมัคร testnet 
(https://test.deribit.com/)

# Create api
(https://test.deribit.com/main#/account?scrollTo=api)

# deposit dericoins (เสกเหรียญเพื่อเอาไปเทรดบน test net)
(https://test.deribit.com/dericoins/)

