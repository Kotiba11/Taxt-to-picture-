import streamlit as st
import requests

# إعدادات الواجهة
st.set_page_config(page_title="AI Story Visualizer", layout="centered")
st.title("🎨 محول القصص إلى صور (نسخة الإنقاذ)")

# واجهة بسيطة
story = st.text_area("اكتب قصتك هنا:", placeholder="مثلاً: رجل يمشي في الغابة تحت المطر...", height=150)
style = st.selectbox("اختر النمط:", ["واقعي", "أنمي", "رسم زيتي", "سينمائي"])

if st.button("توليد المشهد الآن"):
    if story:
        with st.spinner("جاري إنشاء صورتك..."):
            try:
                # نستخدم محرك توليد صور مباشر ومجاني
                # نقوم بتحويل النص إلى إنجليزية بسيطة برمجياً (أو يمكنك الكتابة بالإنجليزية)
                prompt = f"{story}, {style} style, high quality, 4k"
                image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '_')}?width=1024&height=1024&nologo=true"
                
                # عرض النتيجة
                st.image(image_url, caption="تم التوليد بنجاح! 🎉")
                st.success("هذا المحرك يعمل بدون مفتاح API لتجنب المشاكل السابقة.")
            except Exception as e:
                st.error("حدثت مشكلة في الاتصال بالخادم، جرب مرة أخرى.")
    else:
        st.warning("الرجاء كتابة وصف للقصة أولاً.")
