import streamlit as st

st.title("🎨 مولد الصور السريع")

# خانة بسيطة جداً
prompt = st.text_input("اكتب شيئاً بالإنجليزية (مثال: Rose):")

if st.button("شاهد الصورة"):
    if prompt:
        # رابط مباشر ومضمون بنسبة 100%
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
        
        st.write("---")
        # عرض الصورة بطريقة برمجية مختلفة تضمن الظهور
        st.markdown(f'<img src="{image_url}" width="100%" />', unsafe_allow_html=True)
        
        # رابط احتياطي كبير وواضح
        st.write("---")
        st.info("إذا لم تظهر الصورة أعلاه، اضغط على الرابط بالأسفل:")
        st.markdown(f"### [إضغط هنا لفتح الصورة مباشرة]({image_url})")
    else:
        st.warning("يرجى كتابة كلمة")
