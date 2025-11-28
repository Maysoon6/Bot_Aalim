from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# التوكن من متغيرات البيئة - آمن
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# دالة لعرض صفحة المحاضرات
async def show_fiqh_lectures_page(update, context, page_num):
    query = update.callback_query
    fiqh_lectures = context.user_data.get('fiqh_lectures', {})
    
    lectures_per_page = 10
    start_index = (page_num - 1) * lectures_per_page
    end_index = start_index + lectures_per_page
    
    audio_text = f"""
🎧 *المدخل إلى علم الفقه - المحاضرات الصوتية*

📖 الصفحة {page_num} من {((len(fiqh_lectures) - 1) // lectures_per_page) + 1}

اختر المحاضرة الصوتية:
    """
    
    keyboard = []
    
    for i in range(start_index, min(end_index, len(fiqh_lectures))):
        lecture_num = str(i + 1)
        lecture = fiqh_lectures[lecture_num]
        
        keyboard.append([InlineKeyboardButton(
            f"🔊 {lecture_num}. {lecture['title']}",
            callback_data=f"audio_fiqh_{lecture_num}"
        )])
    
    nav_buttons = []
    
    if page_num > 1:
        nav_buttons.append(InlineKeyboardButton("⬅️ الصفحة السابقة", callback_data=f"fiqh_page_{page_num-1}"))
    
    if end_index < len(fiqh_lectures):
        nav_buttons.append(InlineKeyboardButton("الصفحة التالية ➡️", callback_data=f"fiqh_page_{page_num+1}"))
    
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    keyboard.append([InlineKeyboardButton("🎬 فيديوهات يوتيوب", callback_data="youtube_fiqh")])
    keyboard.append([InlineKeyboardButton("⬅ الرجوع", callback_data="مدخل الى الفقه")])
    
    await query.edit_message_text(audio_text, reply_markup=InlineKeyboardMarkup(keyboard))

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🎓 *اهلا وسهلاً بطلاب عالم "* 🤖

اختر المرحلة الدراسية المناسبة:
    """
    
    keyboard = [
        [
            InlineKeyboardButton("📚 المرحلة التمهيدية", callback_data="level0"),
            InlineKeyboardButton("🎓 المرحلة الأولى", callback_data="level1")
        ],
        [
            InlineKeyboardButton("📖 المرحلة الثانية", callback_data="level2"),
            InlineKeyboardButton("🎯 المرحلة الثالثة", callback_data="level3")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# التعامل مع الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "level1":
        materials_text = """
🎓 *المرحلة الأولى - اختر المادة:*

اختر المادة التي تريد استعراض محتواها:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📘 التفسير الموضوعي", callback_data="تفسير_موضوعي"),
                InlineKeyboardButton("📗 علوم القرآن", callback_data="علوم_القرآن")
            ],
            [
                InlineKeyboardButton("📕 الحديث النبوي", callback_data="الحديث_النبوي"),
                InlineKeyboardButton("📙 الفقه العبادات", callback_data="فقه_العبادات")
            ],
            [
                InlineKeyboardButton("📒 العقيدة الإسلامية", callback_data="العقيدة_الإسلامية"),
                InlineKeyboardButton("📔 السيرة النبوية", callback_data="السيرة_النبوية")
            ],
            [
                InlineKeyboardButton("🔍 أصول الفقه", callback_data="أصول_الفقه"),
                InlineKeyboardButton("📖 البلاغة العربية", callback_data="البلاغة_العربية")
            ],
            [
                InlineKeyboardButton("🏠 الرجوع للقائمة الرئيسية", callback_data="back_main")
            ]
        ]
        await query.edit_message_text(materials_text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "level0":
        materials_text = """
📚 *المرحلة التمهيدية - اختر المادة:*

اختر المادة التي تريد استعراض محتواها:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📘 مختصر جامع العلوم والحكم", callback_data="جامع العلوم والحكم"),
                InlineKeyboardButton("📗 المدخل إلى اللغة العربية", callback_data="مدخل الى اللغة العربية")
            ],
            [
                InlineKeyboardButton("📕 المدخل إلى الفقه الإسلامي", callback_data="مدخل الى الفقه"),
                InlineKeyboardButton("📙 مداخل العلوم", callback_data="مداخل العلوم")
            ],
            [
                InlineKeyboardButton("📒 شرح المنهاج", callback_data="المنهاج"),
                InlineKeyboardButton("📔 المختصر في السيرة", callback_data="سيرة")
            ],
            [
                InlineKeyboardButton("🔍 معالم طلب العلم", callback_data="معالم طريق العلم"),
                InlineKeyboardButton("📖 مهارات القراءة", callback_data="مهارات القراءة")
            ],
            [
                InlineKeyboardButton("💖 أعمال القلوب", callback_data="أعمال القلوب"),
                InlineKeyboardButton("⚡ مفسدات القلوب", callback_data="مفسدات القلوب")
            ],
            [
                InlineKeyboardButton("🏠 الرجوع للقائمة الرئيسية", callback_data="back_main")
            ]
        ]
        await query.edit_message_text(materials_text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "level2":
        materials_text = """
📖 *المرحلة الثانية - اختر المادة:*

اختر المادة التي تريد استعراض محتواها:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📘 أفي السنّة شك", callback_data="أفي السنّة شك"),
                InlineKeyboardButton("📗 التأسيس الحديثي", callback_data="التأسيس الحديثي")
            ],
            [
                InlineKeyboardButton("📕 الشرح البيقونيّة", callback_data="البيقونية"),
                InlineKeyboardButton("📙 الشرح المطول نزهة النظر", callback_data="نزهة النظر")
            ],
            [
                InlineKeyboardButton("📒 المداخل الأولية لعلم الحديث", callback_data="مداخل_الحديث"),
                InlineKeyboardButton("📔 كتاب المدخل إلى علم الحديث", callback_data="كتاب_الحديث")
            ],
            [
                InlineKeyboardButton("🔍 المنهج الحديثي بين المتقدمين والمتأخرين", callback_data="منهج المتقدمين والمتأخرين"),
                InlineKeyboardButton("📖 شرح لغة المحدّث", callback_data="لغة المحدث")
            ],
            [
                InlineKeyboardButton("🔍 شرح نخبة الفكر", callback_data="نخبة الفكر"),
                InlineKeyboardButton("📖 شرح نظم المعين", callback_data="المعين")
            ],
            [
                InlineKeyboardButton("🔍 كتاب مناهج المحدثين", callback_data="كتاب مناهج"),
                InlineKeyboardButton("📖 غيث السّاري", callback_data="الساري")
            ],
            [
                InlineKeyboardButton("🔍 مدخل في فقه الحديث", callback_data="مدخل فقه"),
                InlineKeyboardButton("📖 مصادر التلقي والمعرفة", callback_data="مصادر التلقي")
            ],
            [
                InlineKeyboardButton("🏠 الرجوع للقائمة الرئيسية", callback_data="back_main")
            ]
        ]
        await query.edit_message_text(materials_text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "level3":
        await query.edit_message_text("🎯 *المرحلة الثالثة*\n\nلقد اخترت المرحلة الثالثة")

    # ملخص مادة مختصر العلوم
    elif query.data == "جامع العلوم والحكم":
        material_text = """
📘 *مادة: مختصر جامع العلوم والحكم*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 ملخصات", callback_data="ملخص جامع"),
            ],
            [
                InlineKeyboardButton("📝 الكتاب", callback_data="كتاب جامع")
            ],
            [ 
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0"),
            ],
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))
       
    elif query.data == "ملخص جامع":
        material_text = """
📘 *ملخصات المواد*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 الملخص الشمولي", callback_data="سمية_pdf"),
                InlineKeyboardButton("📝 ملخص مع شرح الدكتورة", callback_data="منة")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="جامع العلوم والحكم")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف سمية
    elif query.data == "سمية_pdf":
        try:
            await query.message.reply_document(
                document=open("files/سمية.pdf", "rb"), 
                filename="الملخص_الشمولي_جامع_العلوم.pdf"
            )
            await query.answer("✅ تم إرسال الملخص الشمولي")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # إرسال ملف منة
    elif query.data == "منة":
        try:
            await query.message.reply_document(
                document=open("files/منة.pdf", "rb"), 
                filename="ملخص_مع_الشرح_جامع_العلوم.pdf"
            )
            await query.answer("✅ تم إرسال ملخص الشرح")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    elif query.data == "كتاب جامع":
        try:
            await query.message.reply_document(
                document=open("files/مختصر جامع العلوم والحكم.pdf.pdf", "rb"), 
                filename="مختصر جامع العلوم والحكم.pdf"
            )
            await query.answer("✅ تم إرسال الكتاب")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # ملخص مدخل الى العربية
    elif query.data == "مدخل الى اللغة العربية":
        material_text = """
📗 *المدخل إلى اللغة العربية*

اختر نوع الملخص المناسب:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📝 ملخصات ", callback_data="ملخص العربية"),
                InlineKeyboardButton("🎧 المقرر صوتي  ", callback_data="صوتي_عربية")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "ملخص العربية":
        material_text = """
📘 *ملخصات المواد*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton(" ▪️ الملخص الشمولي ", callback_data="سمية_عربية"),
                InlineKeyboardButton(" ▫️الملخص المختصر", callback_data="رحمة_عربية")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ],
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف سمية للعربية
    elif query.data == "سمية_عربية":
        try:
            await query.message.reply_document(
                document=open("files/سمية_العربية.pdf", "rb"), 
                filename="الملخص_الشمولي_العربية.pdf"
            )
            await query.answer("✅ تم إرسال الملخص الشمولي")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # إرسال ملف رحمة للعربية
    elif query.data == "رحمة_عربية":
        try:
            await query.message.reply_document(
                document=open("files/رحمة_العربية.pdf", "rb"), 
                filename="الملخص_المختصر_العربية.pdf"
            )
            await query.answer("✅ تم إرسال الملخص المختصر")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    elif query.data == "صوتي_عربية":
        material_text = """
🔊  *المحاضرات الصوتية*

اختر نوع الصوت الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("🎧 مدخل إلى الأدب ", callback_data="محتوى_1"),
                InlineKeyboardButton("🎧 مدخل إلى البلاغة", callback_data="محتوى_2")
            ],
            [
                InlineKeyboardButton(" 🎧 مدخل إلى الصرف", callback_data="محتوى_3"),
                InlineKeyboardButton("🎧 مدخل إلى النحو", callback_data="محتوى_4")
            ],
            [
                InlineKeyboardButton("⬅️ رجوع", callback_data="مدخل الى اللغة العربية")
            ],
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data.startswith("محتوى_"):
        lecture_num = query.data.replace("محتوى_", "")
    
        lectures = {
            "1": {"audio": "الأدب.mp3", "title": "المدخل إلى الأدب"},
            "2": {"audio": "البلاغة.mp3", "title": "المدخل إلى علم البلاغة"},
            "3": {"audio": "الصرف.mp3", "title": "المدخل إلى علم الصرف" },
            "4": {"audio": "النحو.mp3", "title": "المدخل إلى علم النحو"}
        }
    
        lecture = lectures.get(lecture_num)
    
        if lecture:
            audio_path = f"audios/{lecture['audio']}"
            
            print(f"🎵 محاولة إرسال من مجلد audios: {audio_path}")
            
            try:
                await query.answer("⏳ جاري إرسال الملف الصوتي...")
                
                await context.bot.send_audio(
                    chat_id=query.message.chat_id,
                    audio=open(audio_path, "rb"),
                    title=lecture["title"],
                    performer="الشيخ سالم القحطاني",
                )
                
                print(f"✅ تم إرسال {lecture['audio']} بنجاح من مجلد audios")
                
            except FileNotFoundError:
                print(f"❌ الملف غير موجود في audios: {audio_path}")
                await query.answer("❌ الملف الصوتي غير متاح حالياً")
            except Exception as e:
                print(f"❌ خطأ: {str(e)}")
                await query.answer("❌ حدث خطأ في إرسال الملف الصوتي")
        else:
            await query.answer("❌ المحاضرة غير موجودة")

    # ملخص مدخل الى الفقه
    elif query.data == "مدخل الى الفقه":
        material_text = """
📕 *المدخل إلى الفقه الإسلامي*

اختر نوع الملخص المناسب:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 خدمات المادة", callback_data="ملخص_الفقة"),
            ],
            [
                InlineKeyboardButton("🎧 الملفات الصوتية", callback_data="صوتي_فقه")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "ملخص_الفقة":
        material_text = """
📘 *ملخصات المواد*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 ملخص مع المتن والشرائح", callback_data="فقه_منة"),
                InlineKeyboardButton("📝 الملخص المختصر", callback_data="فقه_هاجر")
            ],
            [
                InlineKeyboardButton("📚 الملخص الشمولي", callback_data="فقه_هدى")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    # إرسال ملفات الفقه
    elif query.data == "فقه_منة":
        try:
            await query.message.reply_document(
                document=open("files/فقه_منة.pdf", "rb"), 
                filename="ملخص_المتن_والشرائح_الفقه.pdf"
            )
            await query.answer("✅ تم إرسال ملخص المتن والشرائح")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "فقه_هاجر":
        try:
            await query.message.reply_document(
                document=open("files/فقه_هاجر.pdf", "rb"), 
                filename="الملخص_المختصر_الفقه.pdf"
            )
            await query.answer("✅ تم إرسال الملخص المختصر")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "فقه_هدى":
        try:
            await query.message.reply_document(
                document=open("files/فقه_هدى.pdf", "rb"), 
                filename="الملخص_الشمولي_الفقه.pdf"
            )
            await query.answer("✅ تم إرسال الملخص الشمولي")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "صوتي_فقه":
        # جميع المحاضرات الصوتية
        fiqh_lectures = {
            "1": {"audio": "1.mp3", "title": "تعريف بالمقرر وأهميته"},
            "2": {"audio": "2.mp3", "title": "مقدمات عامة عن علم الفقه"},
            "3": {"audio": "3.mp3", "title": "مراحل الفقه"},
            "4": {"audio": "4.mp3", "title": "مرحلة التشريع"},
            "5": {"audio": "5.mp3", "title": "مرحلة الصحابة"},
            "6": {"audio": "6.mp3", "title": "تتمة الكلام عن مرحلة الصحابة"},
            "7": {"audio": "7.mp3", "title": "المدارس الفقهية في زمن التابعين"},
            "8": {"audio": "8.mp3", "title": "مرحلة المذاهب"},
            "9": {"audio": "9.mp3", "title": "المذاهب المندرسة"},
            "10": {"audio": "10.mp3", "title": "تتمة المذاهب المندرسة"},
            "11": {"audio": "11.mp3", "title": "الإمام أبو حنيفة"},
            "12": {"audio": "12.mp3", "title": "المذهب الحنفي"},
            "13": {"audio": "13.mp3", "title": "الإمام مالك"},
            "14": {"audio": "14.mp3", "title": "المذهب المالكي"},
            "15": {"audio": "15.mp3", "title": "الإمام الشافعي"},
            "16": {"audio": "16.mp3", "title": "المذهب الشافعي"},
            "17": {"audio": "17.mp3", "title": "الإمام أحمد"},
            "18": {"audio": "18.mp3", "title": "المذهب الحنبلي (مرحلة المتقدمين)"},
            "19": {"audio": "19.mp3", "title": "المذهب الحنبلي (مرحلة المتوسطين)"},
            "20": {"audio": "20.mp3", "title": "المذهب الحنبلي (مرحلة المتأخرين)"},
            "21": {"audio": "21.mp3", "title": "التمذهب (ذم التعصب)"},
            "22": {"audio": "22.mp3", "title": "التمذهب (قبول وجود المذاهب)"},
            "23": {"audio": "23.mp3", "title": "التمذهب (تتمة الكلام عن قبول وجود المذاهب)"},
            "24": {"audio": "24.mp3", "title": "التمذهب (قبول التخرج على المدارس الفقهية)"},
            "25": {"audio": "25.mp3", "title": "التمذهب (مشروعيته)"},
            "26": {"audio": "26.mp3", "title": "التمذهب (تتمة مشروعيته)"},
            "27": {"audio": "27.mp3", "title": "التمذهب (القول بمنعه)"},
            "28": {"audio": "28.mp3", "title": "العصر الحاضر (طباعة الكتب)"},
            "29": {"audio": "29.mp3", "title": "تتمة الكتب المطبوعة"},
            "30": {"audio": "30.mp3", "title": "الخدمات الفقهية في العصر الحاضر"},
            "31": {"audio": "31.mp3", "title": "التجديد في أصول الفقه"},
            "32": {"audio": "32.mp3", "title": "المدرسة المقاصدية"},
            "33": {"audio": "33.mp3", "title": "دعوات أخرى في التجديد الأصولي"},
            "34": {"audio": "34.mp3", "title": "أهل الحديث وأهل الرأي"},
            "35": {"audio": "35.mp3", "title": "أهل الظاهر والمدرسة العقلية"},
            "36": {"audio": "36.mp3", "title": "أسباب اختلاف العلماء"},
            "37": {"audio": "37.mp3", "title": "تتمة أسباب الخلاف"},
            "38": {"audio": "38.mp3", "title": "الموقف من الخلاف الفقهي"},
            "39": {"audio": "39.mp3", "title": "خاتمة"}
        }
        
        # حفظ المحاضرات في context للمراجعة لاحقاً
        context.user_data['fiqh_lectures'] = fiqh_lectures
        context.user_data['current_page'] = 1
        
        await show_fiqh_lectures_page(update, context, 1)

    # معالجة التنقل بين الصفحات
    elif query.data.startswith("fiqh_page_"):
        page_num = int(query.data.replace("fiqh_page_", ""))
        await show_fiqh_lectures_page(update, context, page_num)

    # معالجة إرسال الملفات الصوتية
    elif query.data.startswith("audio_fiqh_"):
        lecture_num = query.data.replace("audio_fiqh_", "")
        fiqh_lectures = context.user_data.get('fiqh_lectures', {})
        
        lecture = fiqh_lectures.get(lecture_num)
        
        if lecture:
            try:
                await query.answer("⏳ جاري إرسال الملف الصوتي...")
                
                # إرسال الملف الصوتي
                await query.message.reply_audio(
                    audio=open(f"audios/{lecture['audio']}", "rb"),
                    title=f"{lecture_num}. {lecture['title']}",
                    performer="د. عامر بهجت"
                )
                
            except FileNotFoundError:
                await query.answer("❌ الملف الصوتي غير متاح حالياً")
            except Exception as e:
                await query.answer("❌ حدث خطأ في الإرسال")
        else:
            await query.answer("❌ المحاضرة غير موجودة")

    # معالجة زر اليوتيوب
    elif query.data == "youtube_fiqh":
        video_text = """
🎬 *فيديوهات يوتيوب - المدخل إلى علم الفقه*

🔗 قائمة التشغيل الكاملة:
https://youtube.com/playlist?list=PLF8wQ8_AW0LxNTFYRmIZVrPxZxoGuIBT3&si=b4JYI8Ra93fyn-0l

💡 انسخ الرابط وافتحه في اليوتيوب
        """
        
        keyboard = [
            [InlineKeyboardButton("⬅ الرجوع للمحاضرات الصوتية", callback_data="صوتي_فقه")]
        ]
        await query.edit_message_text(video_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # الرجوع للقائمة الرئيسية
    elif query.data == "back_main":
        await start(update, context)
# ملخص مداخل العلوم
    elif query.data == "مداخل العلوم":
        material_text = """
📙 *مداخل العلوم*

اختر نوع الملخص المناسب:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 الملخص الشمولي", callback_data="علوم_سمية"),
                InlineKeyboardButton("📝 ملخص مع الشرح", callback_data="علوم_منة")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملفات العلوم
    elif query.data == "علوم_سمية":
        try:
            await query.message.reply_document(
                document=open("files/تلخيص سلسلة مداخل العلوم.pdf", "rb"), 
                filename="الملخص_الشمولي_العلوم.pdf"
            )
            await query.answer("✅ تم إرسال الملخص الشمولي")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "علوم_منة":
        try:
            await query.message.reply_document(
                document=open("files/مَدَاخِل العُلوم.pdf", "rb"), 
                filename="ملخص_مع_الشرح_العلوم.pdf"
            )
            await query.answer("✅ تم إرسال ملخص الشرح")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    # ملخص المنهاج
    elif query.data == "المنهاج":
        material_text = """
📒 *شرح المنهاج من ميراث النبوة*

اختر نوع التخريج المطلوب:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 ملخص مع الشواهد", callback_data="منهاج_سمية"),
                InlineKeyboardButton("📊 تخريج حسب الباب", callback_data="منهاج_باب")
            ],
            [
                InlineKeyboardButton("👤 تخريج حسب الراوي", callback_data="منهاج_راوي"),
                InlineKeyboardButton("📖 تخريج حسب المخرج", callback_data="منهاج_مخرج")
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملفات المنهاج
    elif query.data == "منهاج_سمية":
        try:
            await query.message.reply_document(
                document=open("files/منهاج سمية.pdf", "rb"), 
                filename="ملخص_الشواهد_المنهاج.pdf"
            )
            await query.answer("✅ تم إرسال ملخص الشواهد")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "منهاج_باب":
        try:
            await query.message.reply_document(
                document=open("files/تخريج الباب.pdf", "rb"), 
                filename="تخريج_حسب_الباب.pdf"
            )
            await query.answer("✅ تم إرسال تخريج الباب")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "منهاج_راوي":
        try:
            await query.message.reply_document(
                document=open("files/تخريج الراوي.pdf", "rb"), 
                filename="تخريج_حسب_الراوي.pdf"
            )
            await query.answer("✅ تم إرسال تخريج الراوي")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    elif query.data == "منهاج_مخرج":
        try:
            await query.message.reply_document(
                document=open("files/تخريج المخرج.pdf", "rb"), 
                filename="تخريج_حسب_المخرج.pdf"
            )
            await query.answer("✅ تم إرسال تخريج المخرج")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")

    # ملخص مادة السيرة
    elif query.data == "سيرة":
        material_text = """
📘 *مادة: المختصر في السيرة*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 ملخص", callback_data="رقية_سيرة"),
                InlineKeyboardButton("📝 ملخص مع شواهد الأرجوزة", callback_data="سمية_سيرة"),
            ],
            [
                InlineKeyboardButton("📝 تواريخ الغزوات", callback_data="رقية_سيرة1"),
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف رقية
    elif query.data == "رقية_سيرة":
        try:
            await query.message.reply_document(
                document=open("files/المختصر في السيرة.pdf", "rb"), 
                filename="ملخص.pdf"
            )
            await query.answer("✅ تم إرسال الملخص")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # إرسال ملف سمية
    elif query.data == "سمية_سيرة":
        try:
            await query.message.reply_document(
                document=open("files/سيرة وارجوزة.pdf", "rb"), 
                filename="ملخص مع شواهد من الإرجوزة.pdf"
            )
            await query.answer("✅ تم إرسال ملخص الشرح")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    elif query.data == "رقية_سيرة1":
        try:
            await query.message.reply_document(
                document=open("files/غزوات.pdf", "rb"), 
                filename="تشجير تاريخ الغزوات.pdf"
            )
            await query.answer("✅ تم إرسال تشجير الغزوات")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # ملخص مادة أعمال القلوب
    elif query.data == "أعمال القلوب":
        material_text = """
📘 *مادة: أعمال القلوب*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📝 ملخص أعمال القلوب", callback_data="لينة"),
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف لينة
    elif query.data == "لينة":
        try:
            await query.message.reply_document(
                document=open("files/القلوب.pdf", "rb"), 
                filename="ملخص.pdf"
            )
            await query.answer("✅ تم إرسال الملخص")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # ملخص مادة مفسدات القلوب
    elif query.data == "مفسدات القلوب":
        material_text = """
📘 *مادة: مفسدات القلوب*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📝 ملخص عون", callback_data="عون"),
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف عون
    elif query.data == "عون":
        try:
            await query.message.reply_document(
                document=open("files/مفسدات.pdf", "rb"), 
                filename="ملخص عون.pdf"
            )
            await query.answer("✅ تم إرسال الملخص")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")
    
    # محاضرة مهارات القراءة
    elif query.data == "مهارات القراءة":
        material_text = """
📘 *مادة: محاضرة مهارات القراءة*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 تشجير المحاضرة", callback_data="تشجير_قراءة"),
                InlineKeyboardButton("📝 ملخص", callback_data="ملخص_قراءة"),
            ],
            [
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف تشجير القراءة
    elif query.data == "تشجير_قراءة":
        try:
            await query.message.reply_document(
                document=open("files/تشجير مهارات القراءة.pdf", "rb"), 
                filename="تشجير.pdf"
            )
            await query.answer("✅ تم إرسال التشجير")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # إرسال ملف ملخص القراءة
    elif query.data == "ملخص_قراءة":
        try:
            await query.message.reply_document(
                document=open("files/ملخص مهارات القراءة.pdf", "rb"), 
                filename="ملخص.pdf"
            )
            await query.answer("✅ تم إرسال الملخص")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # ملخص مادة معالم طريق العلم
    elif query.data == "معالم طريق العلم":
        material_text = """
📘 *كتاب: معالم في طريق طلب العلم*

اختر نوع الملخص الذي تريده:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("📄 ملخص الشيخ محمد", callback_data="معالم_شميس"),
                InlineKeyboardButton("📝 ملخص مختصر", callback_data="رحمة_معالم"),
            ],
            [
                InlineKeyboardButton("📝 فوائد منتقاة من الكتاب", callback_data="فوائد_معالم"),
                InlineKeyboardButton("⬅ الرجوع للمواد", callback_data="level0")
            ]
        ]
        await query.edit_message_text(material_text, reply_markup=InlineKeyboardMarkup(keyboard))

    # إرسال ملف معالم شميس
    elif query.data == "معالم_شميس":
        try:
            await query.message.reply_document(
                document=open("files/معالم_شميس.pdf.pdf", "rb"), 
                filename="ملخص الشيخ محمد شميس.pdf"
            )
            await query.answer("✅ تم إرسال الملخص")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    # إرسال ملف رحمة معالم
    elif query.data == "رحمة_معالم":
        try:
            await query.message.reply_document(
                document=open("files/تلخيص_معالم.pdf.pdf", "rb"), 
                filename="ملخص مختصر.pdf"
            )
            await query.answer("✅ تم إرسال الملخص المختصر")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")

    elif query.data == "فوائد_معالم":
        try:
            await query.message.reply_document(
                document=open("files/فوائد_معالم.pdf.pdf", "rb"), 
                filename="فوائد منتقاة.pdf"
            )
            await query.answer("✅ تم إرسال الفوائد المنتقاة")
        except FileNotFoundError:
            await query.answer("❌ الملف غير موجود حالياً")
        except Exception as e:
            await query.answer("❌ حدث خطأ في الإرسال")
   
    # الرجوع للقائمة الرئيسية
    elif query.data == "back_main":
        await start(update, context)
     

# تشغيل البوت
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 البوت يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()