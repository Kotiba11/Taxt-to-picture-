import streamlit as st
import google.generativeai as genai

# إعداد المفتاح الخاص بك
API_KEY = "AIzaSyC8NoVlSnKMlaafqh9deN133eWgTE270c4"
genai.configure(api_key=API_KEY)

# إعدادات واجهة المستخدم لتشبه تصميمك
st.set_page_config(page_title="StoryToImage AI", page_icon="🎨")

# العنوان
st.title("🎨 StoryToImage AI")

# خانة نص القصة
story_text = st.text_area(
    "نص القصة", 
    placeholder="اكتب قصتك هنا بالتفصيل (كلما زادت التفاصيل زادت الجودة)...",
    height=200
)

# خيارات القياس والنمط في أعمدة
col1, col2 = st.columns(2)

with col1:
    size = st.selectbox("قياس الصورة", ["يوتيوب 16:9", "شورتس 9:16"])

with col2:
    style = st.selectbox("نمط الصور", ["كلاسيكي", "تاريخي", "أنمي", "كرتوني", "واقعي"])

# زر التشغيل
if st.button("توليد الوصف والمشهد"):
    if story_text:
        with st.spinner("جاري تحليل القصة وتوليد الوصف..."):
            try:
                # استدعاء موديل Gemini
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"حلل القصة التالية: {story_text}. ثم اقترح وصفاً دقيقاً لصورة تناسب هذه القصة بنمط {style} وقياس {size}."
                
                response = model.generate_content(prompt)
                
                # عرض النتيجة
                st.success("تم التوليد بنجاح!")
                st.subheader("الوصف المقترح للمشهد:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء كتابة نص القصة أولاً.")

# تذييل الصفحة
st.markdown("---")
st.caption("Powered by Gemini AI | Developed via Google AI Studio")
