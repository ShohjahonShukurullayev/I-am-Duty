import streamlit as st
import random

st.set_page_config(page_title="Bolalar Tozalash Vazifasi", page_icon="🧹")

st.title("🧹 I'm Duty Today Ilovasi")

st.markdown("""
6 ta bolani 2 ta guruhga bo‘ling (har biri 3 kishilik).  
Dastur har bir guruhdan 1 nafardan **“xonani tozalaydi”** deb belgilaydi,  
qolgan 4 nafar bolaga esa **1 dan 4 gacha takrorlanmaydigan raqam** beradi.  
Raqamga qarab tozalash joyi aniqlanadi:
""")

st.markdown("""
| Raqam | Tozalash joyi |
|:------:|:---------------|
| 1 | 🚽 Hojatxona |
| 2 | 🚿 Dush |
| 3 | 🍳 Oshxona |
| 4 | 🪟 Zal va balkon |
""")

# Guruhlarni kiritish
group1_input = st.text_input("1-guruh (3 ta ism, vergul bilan):", placeholder="Masalan: Ali, Vali, Sardor")
group2_input = st.text_input("2-guruh (3 ta ism, vergul bilan):", placeholder="Masalan: Zuhra, Jamshid, Gulnoza")

# Qayta random qilish uchun har safar yangi bosish
if st.button("🎲 Taqsimlashni boshlash yoki Qayta Random Qilish"):
    group1 = [n.strip() for n in group1_input.split(",") if n.strip()]
    group2 = [n.strip() for n in group2_input.split(",") if n.strip()]

    if len(group1) != 3 or len(group2) != 3:
        st.error("❌ Har bir guruhda aniq 3 ta ism bo‘lishi kerak!")
    else:
        # Har bir guruhdan tozalovchi tanlanadi
        cleaner1 = random.choice(group1)
        cleaner2 = random.choice(group2)

        # Qolgan bolalar raqam oladi
        receivers = [n for n in group1 + group2 if n not in (cleaner1, cleaner2)]

        # 1–4 raqamlar takrorlanmas tarzda tanlanadi
        numbers = random.sample(range(1, 5), 4)
        random.shuffle(receivers)

        # Raqam joylari xaritasi
        cleaning_places = {
            1: "🚽 Hojatxona tozalaydi",
            2: "🚿 Dush tozalaydi",
            3: "🍳 Oshxona tozalaydi",
            4: "🪟 Zal va balkon tozalaydi"
        }

        # Natijani shakllantirish
        assignment = {name: None for name in group1 + group2}
        for name, num in zip(receivers, numbers):
            assignment[name] = cleaning_places[num]
        assignment[cleaner1] = "🧹 Xonani tozalaydi"
        assignment[cleaner2] = "🧹 Xonani tozalaydi"

        # Natijani chiqarish
        st.success("✅ Taqsimlash yakunlandi!")
        st.subheader("📋 Natijalar:")

        for name in group1 + group2:
            if assignment[name] == "🧹 Xonani tozalaydi":
                st.warning(f"🧹 {name} — Xonani tozalaydi")
            else:
                st.info(f"{name} — {assignment[name]}")

        st.markdown("---")
        st.info(f"🧍‍♂️ Xonani tozalovchilar: **{cleaner1}** va **{cleaner2}**")


