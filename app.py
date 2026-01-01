import streamlit as st
import google.generativeai as genai

# إعداد المفتاح
API_KEY = "AIzaSyC8NoVlSnKMlaafqh9deN133eWgTE270c4"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="AI Story Teller", layout="centered")
st.title("🎨 محول القصص إلى مشاهد")

story = st.text_area("نص القصة", placeholder="اكتب قصتك هنا...", height=200)
style = st.selectbox("نمط الصور", ["واقعي", "أنمي", "كرتوني", "تاريخي"])

if st.button("توليد المشهد الآن"):
    if story:
        with st.spinner("جاري محاولة الاتصال بالذكاء الاصطناعي..."):
            # محاولة استخدام الموديل بأكثر من مسمى لتفادي خطأ 404
            success = False
            for model_name in ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-pro']:
                try:
                    model = genai.GenerativeModel(model_name)
                    prompt = f"Describe a high-quality artistic scene for this story in English, style {style}: {story}"
                    response = model.generate_content(prompt)
                    
                    if response.text:
                        st.subheader("الوصف البصري:")
                        st.info(response.text)
                        
                        # توليد الصورة
                        image_url = f"https://pollinations.ai/p/{response.text.replace(' ', '_')}?width=1024&height=1024&seed=42"
                        st.image(image_url, caption="المشهد المولد")
                        success = True
                        break
                except:
                    continue
            
            if not success:
                st.error("عذراً، نظام Google يرفض الاتصال حالياً. تأكد من صلاحية المفتاح أو حاول لاحقاً.")
    else:
        st.warning("يرجى كتابة نص")
