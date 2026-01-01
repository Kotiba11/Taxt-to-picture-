import streamlit as st
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="AI Story Image", layout="centered")
st.title("🎨 محول القصص إلى صور")

# المدخلات
story = st.text_area("اكتب قصتك هنا:", placeholder="مثلاً: قطة صغيرة تلعب في الحديقة...", height=150)
style = st.selectbox("اختر النمط:", ["Anime", "Cyberpunk", "Oil Painting", "Cinematic", "Cartoon"])

if st.button("توليد الصورة الآن 🎉"):
    if story:
        with st.spinner("جاري إنشاء لوحتك الفنية..."):
            try:
                # هذه الخطوة هي السر: تحويل النص لرابط يفهمه المتصفح
                clean_text = urllib.parse.quote(story)
                image_url = f"https://pollinations.ai/p/{clean_text}?width=1024&height=1024&seed=123&model=flux&nologo=true"
                
                # عرض الصورة
                st.markdown(f"### النتيجة لنمط {style}:")
                st.image(image_url, use_container_width=True)
                st.success("تم التوليد بنجاح! إذا لم تظهر الصورة، انتظر ثواني فقط.")
            except Exception as e:
                st.error("حدث ضغط على الخادم، حاول مرة أخرى بعد قليل.")
    else:
        st.warning("من فضلك اكتب قصة أولاً!")
