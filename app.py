import streamlit as st
import google.generativeai as genai

# إعداد المفتاح
API_KEY = "AIzaSyC8NoVlSnKMlaafqh9deN133eWgTE270c4"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="StoryToImage AI", page_icon="🎨")
st.title("🎨 تطبيق تحويل القصص إلى صور")

# الواجهة
story = st.text_area("نص القصة", placeholder="اكتب قصتك هنا...", height=200)
size = st.selectbox("قياس الصورة", ["16:9", "9:16"])
style = st.selectbox("نمط الصور", ["واقعي", "أنمي", "كرتوني", "تاريخي"])

if st.button("توليد الوصف والمشهد"):
    if story:
        with st.spinner("جاري المعالجة..."):
            try:
                # هذا هو التعديل الذي يحل مشكلة 404
                model = genai.GenerativeModel('gemini-pro')
                
                prompt = f"Describe a professional artistic scene for this story in English for AI image generation, style {style}: {story}"
                response = model.generate_content(prompt)
                description = response.text
                
                st.subheader("الوصف المقترح للمشهد:")
                st.info(description)
                
                # إضافة توليد الصورة فعلياً
                st.subheader("المشهد البصري:")
                img_url = f"https://pollinations.ai/p/{description.replace(' ', '_')}?width=1024&height=1024&nologo=true"
                st.image(img_url, caption="الصورة المولدة لقصتك")
                
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("يرجى إدخال نص")
