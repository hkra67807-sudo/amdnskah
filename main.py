<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>قائمة طعام مطعمي</title>
    <link href="https://fonts.googleapis.com/css2?family=Changa:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { background: #fdf2e9; font-family: 'Changa', sans-serif; margin: 0; padding: 20px; text-align: center; }
        .food-card { background: white; border-radius: 15px; padding: 15px; margin: 10px auto; width: 90%; max-width: 300px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .add-btn { background: #e67e22; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-family: 'Changa'; }
        .floating-cart { position: fixed; top: 20px; left: 20px; background: #e67e22; color: white; padding: 15px; border-radius: 50%; cursor: pointer; z-index: 100; }
        #cart-modal { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: white; padding: 20px; border-radius: 15px; box-shadow: 0 0 20px rgba(0,0,0,0.5); width: 90%; z-index: 1000; }
        .order-now-btn { background: #0088cc; color: white; border: none; padding: 15px; border-radius: 5px; width: 100%; font-size: 16px; margin-top: 10px; cursor: pointer; font-family: 'Changa'; }
    </style>
</head>
<body>

    <div class="floating-cart" onclick="openCart()">
        <span id="cart-count">0</span> 🛒
    </div>

    <h1>🍔 قائمة الطعام</h1>

    <div class="food-card">
        <img src="https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=500" style="width:100%; border-radius:10px;">
        <h3>برجر لحم</h3>
        <p>7,500 د.ع</p>
        <button class="add-btn" onclick="addToCart('برجر لحم', 7500)">إضافة للسلة +</button>
    </div>

    <div class="food-card">
        <img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500" style="width:100%; border-radius:10px;">
        <h3>بيتزا إيطالية</h3>
        <p>10,000 د.ع</p>
        <button class="add-btn" onclick="addToCart('بيتزا إيطالية', 10000)">إضافة للسلة +</button>
    </div>

    <div id="cart-modal">
        <h2>🛒 طلباتك</h2>
        <div id="cart-items"></div>
        <hr>
        <p>المجموع: <span id="total">0</span> د.ع</p>
        <button class="order-now-btn" onclick="sendToTelegram()">إرسال الطلب عبر تيليجرام ✈️</button>
        <button onclick="closeCart()" style="margin-top:10px; background:none; border:none; color:gray; cursor:pointer;">إغلاق</button>
    </div>

    <script>
        let cart = [];
        let total = 0;

        function addToCart(name, price) {
            cart.push({name, price});
            total += price;
            document.getElementById('cart-count').innerText = cart.length;
            updateCartUI();
        }

        function updateCartUI() {
            const container = document.getElementById('cart-items');
            container.innerHTML = cart.map(item => `<p>${item.name} - ${item.price} د.ع</p>`).join('');
            document.getElementById('total').innerText = total.toLocaleString();
        }

        function openCart() { document.getElementById('cart-modal').style.display = 'block'; }
        function closeCart() { document.getElementById('cart-modal').style.display = 'none'; }

        function sendToTelegram() {
            if (cart.length === 0) { alert("السلة فارغة!"); return; }
            
            let message = "طلب جديد من الموقع:%0A";
            cart.forEach(item => { message += `- ${item.name} (${item.price} د.ع)%0A`; });
            message += `%0A*المجموع الكلي: ${total.toLocaleString()} د.ع*`;
            
            // معرفك الشخصي Po_pou مضاف هنا تلقائياً
            const telegramUser = "Po_pou"; 
            window.open(`https://t.me/${telegramUser}?text=${message}`);
        }
    </script>
</body>
</html>
