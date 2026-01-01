import streamlit as st
import requests
import urllib.parse

# إعدادات واجهة التطبيق
st.set_page_config(page_title="Magic Story Image", layout="centered")
st.title("🎨 محول القصص إلى صور (النسخة الشغالة)")

# خانة النص
story = st.text_area("اكتب قصتك هنا بالعربي:", placeholder="مثال: فارس يركب حصاناً أبيض في الغابة...", height=150)
style = st.selectbox("اختر نمط الرسم:", ["Artistic", "Anime", "Realistic", "3D Render"])

if st.button("توليد الصورة الآن ✨"):
    if story:
        with st.spinner("جاري الترجمة وإنشاء الصورة..."):
            try:
                # خطوة الإنقاذ: ترجمة بسيطة برمجياً عبر محرك ترجمة مجاني
                translation_url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=ar&tl=en&dt=t&q={urllib.parse.quote(story)}"
                r = requests.get(translation_url)
                translated_text = r.json()[0][0][0]
                
                # إنشاء رابط الصورة بالإنجليزية
                final_prompt = f"{translated_text}, {style} style, masterpiece, highly detailed"
                encoded_prompt = urllib.parse.quote(final_prompt)
                image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed=99&nologo=true"
                
                # عرض الصورة
                st.markdown("---")
                st.image(image_url, caption="تم توليد الصورة بناءً على ترجمة قصتك")
                st.success("نجحت العملية! إذا لم تظهر الصورة فوراً، انتظر 5 ثوانٍ لتحميلها.")
                
            except Exception as e:
                # في حال فشل الترجمة، نستخدم النص الأصلي مع تنظيفه
                image_url = f"https://pollinations.ai/p/{urllib.parse.quote(story)}?width=1024&height=1024"
                st.image(image_url)
    else:
        st.warning("أدخل نصاً أولاً")
