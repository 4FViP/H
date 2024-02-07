from pyrogram import Client
# DASTURCHI @ALAWE1 Kanal : @AWCODE3 "تخمط تثبت فشلك 
"""
PYROGRAM Module orqalik odiygina tayorlangan kod...
Shunchaki bu kod orqalik guruhdan gurhga odam olib otishingiz mumkin...
Tushunarli bo'lishi uchun boshlanishiga odiygina yozilgan...
Ogohlantirish ! Akuntingiz Spam bo'lsa yoki blok bo'lsa dasturchi javob bermaydi...

Negativ va Senior dasturchilar negativ yozmelar boshlanishiga kod bu...

Manba bilan olinglar do'stlar...

DASTURCHI @ALAWE1 Kanal : @AWCODE3

"""
api_id =  11750778
api_hash = 'd0352df3ddb5e00bcf16b55dae071b52' # API HASH KIRITING 
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash
)

app.start()
# DASTURCHI @ALAWE1 Kanal : @AWCODE3
while True:
    from_chat_id = -1991965557 # A'zo tanlamoqchi bolgan guruhingiz ID raqamini kiritng
    my_chat_id = -2036859731 # A'zolarni qo'shmoqchi bo'lgan guruhingiz ID raqamini kiritng
    members = [] # Foidalanuvchi idlarini ro'yxatga ko'chirish yani olish uchun
    # DASTURCHI @ALAWE1 Kanal : @AWCODE3
    for member in app.get_chat_members(from_chat_id):
        members.append(member.user.id)
    # DASTURCHI @ALAWE1 Kanal : @AWCODE3
    app.add_chat_members(chat_id=my_chat_id, user_ids=members)
# DASTURCHI @ALAWE1 Kanal : @AWCODE3
app.run()
