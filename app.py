import streamlit as st
import google.generativeai as genai

# إعداد المفتاح الخاص بك
API_KEY = "AIzaSyC8NoVlSnKMlaafqh9deN133eWgTE270c4"
genai.configure(api_key=API_KEY)

# إعدادات الواجهة
st.set_page_config(page_title="StoryToImage AI", page_icon="🎨")
st.title("🎨 تحويل القصص إلى صور")

# مدخلات المستخدم
story_text = st.text_area("نص القصة", placeholder="اكتب قصتك هنا بالتفصيل...", height=200)

col1, col2 = st.columns(2)
with col1:
    size = st.selectbox("قياس الصورة", ["16:9", "9:16"])
with col2:
    style = st.selectbox("نمط الرسم", ["تاريخي", "أنمي", "واقعي", "كرتوني"])

# زر التشغيل
if st.button("إنشاء المشهد"):
    if story_text:
        with st.spinner("جاري التحليل والتوليد..."):
            try:
                # الكود المصحح للموديل
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Describe a professional artistic scene for this story in English as a single prompt for image generation, style {style}: {story_text}"
                
                response = model.generate_content(prompt)
                desc = response.text
                
                st.subheader("الوصف الذكي:")
                st.info(desc)
                
                # توليد الصورة الحقيقية وعرضها
                st.subheader("المشهد البصري:")
                image_url = f"https://pollinations.ai/p/{desc.replace(' ', '_')}?width=1024&height=1024&nologo=true"
                st.image(image_url, caption="الصورة المولدة لقصتك")
                
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")
    else:
        st.warning("الرجاء كتابة نص أولاً")
