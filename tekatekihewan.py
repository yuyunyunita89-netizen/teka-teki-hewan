import streamlit as st

def teka_teki_hewan():
    st.title("🦁 TEKA-TEKI HEWAN")
    st.write("Jawab pertanyaan berikut dengan memilih a, b, atau c.\n")

    # Daftar soal
    soal = [
        {
            "pertanyaan": "1. Hewan apa yang disebut raja hutan?",
            "pilihan": ["a. Harimau", "b. Singa", "c. Serigala"],
            "jawaban": "b"
        },
        {
            "pertanyaan": "2. Hewan apa yang bisa hidup di darat dan air?",
            "pilihan": ["a. Katak", "b. Gajah", "c. Kucing"],
            "jawaban": "a"
        },
        {
            "pertanyaan": "3. Hewan apa yang bisa terbang?",
            "pilihan": ["a. Kuda", "b. Burung", "c. Ikan"],
            "jawaban": "b"
        },
        {
            "pertanyaan": "4. Hewan apa yang paling besar di laut?",
            "pilihan": ["a. Paus Biru", "b. Hiu", "c. Lumba-lumba"],
            "jawaban": "a"
        },
        {
            "pertanyaan": "5. Hewan apa yang menghasilkan madu?",
            "pilihan": ["a. Lebah", "b. Semut", "c. Kupu-kupu"],
            "jawaban": "a"
        },
        {
            "pertanyaan": "6. Hewan apa yang bisa mengubah warna kulitnya?",
            "pilihan": ["a. Bunglon", "b. Ular", "c. Buaya"],
            "jawaban": "a"
        },
        {
            "pertanyaan": "7. Hewan apa yang dikenal dengan belalai panjang?",
            "pilihan": ["a. Badak", "b. Gajah", "c. Jerapah"],
            "jawaban": "b"
        },
        {
            "pertanyaan": "8. Hewan apa yang memiliki leher panjang?",
            "pilihan": ["a. Zebra", "b. Jerapah", "c. Kuda"],
            "jawaban": "b"
        },
        {
            "pertanyaan": "9. Hewan apa yang bisa berjalan mundur?",
            "pilihan": ["a. Kepiting", "b. Ular", "c. Tikus"],
            "jawaban": "a"
        },
        {
            "pertanyaan": "10. Hewan apa yang dikenal sebagai hewan peliharaan manusia?",
            "pilihan": ["a. Kucing", "b. Harimau", "c. Singa"],
            "jawaban": "a"
        }
    ]

    # Skor
    if "skor" not in st.session_state:
        st.session_state.skor = 0
    if "soal_ke" not in st.session_state:
        st.session_state.soal_ke = 0
    if "selesai" not in st.session_state:
        st.session_state.selesai = False

    # Jika belum selesai
    if not st.session_state.selesai:
        index = st.session_state.soal_ke
        s = soal[index]

        st.subheader(s["pertanyaan"])
        jawaban = st.radio("Pilih jawaban:", s["pilihan"], key=f"soal_{index}")

        if st.button("Kirim Jawaban"):
            # ambil huruf jawaban (misal 'a')
            if jawaban.startswith(s["jawaban"] + "."):
                st.success("Benar!")
                st.session_state.skor += 1
            else:
                st.error(f"Salah! Jawaban yang benar adalah: {s['jawaban']}. {s['pilihan'][ord(s['jawaban']) - 97]}")

            st.session_state.soal_ke += 1

            if st.session_state.soal_ke >= len(soal):
                st.session_state.selesai = True

            st.experimental_rerun()

    else:
        st.subheader("===== HASIL AKHIR =====")
        st.write(f"🎉 Skor kamu: **{st.session_state.skor}** dari **{len(soal)}**")

        if st.button("Main Lagi"):
            st.session_state.skor = 0
            st.session_state.soal_ke = 0
            st.session_state.selesai = False
            st.experimental_rerun()

# Jalankan aplikasi
teka_teki_hewan()
