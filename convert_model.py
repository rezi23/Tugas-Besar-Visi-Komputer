from tensorflow.keras.models import load_model

# Memuat model lama
model = load_model("mask_detector.model")

# Menyimpan ulang model ke format .h5
model.save("mask_detector.h5")

print("Model berhasil dikonversi ke format .h5!")
