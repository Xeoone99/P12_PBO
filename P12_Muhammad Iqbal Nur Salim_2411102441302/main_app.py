import logging
from IValidationRule import SKSLimitRule
from RegistrationService import RegistrationService

# -------------------------------------------------------------
# PENTING: KONFIGURASI LOGGING (Wajib ada di bagian paling atas file utama)
# -------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

# Inisialisasi Logger (Wajib sama dengan yang ada di file services)
LOGGER = logging.getLogger('Registration')

def run_registration_app():
    """Fungsi eksekusi utama untuk menguji skenario registrasi."""
    
    # Siapkan aturan validasi yang akan di-inject
    rules_to_use = [
        SKSLimitRule(),
        # Tambahkan rule validasi lain Anda di sini
    ]
    
    # Inisialisasi Service (Dependency Injection)
    reg_service = RegistrationService(rules_to_use)
    
    # --------------------------------------------------
    # UJI SKENARIO 1: SUKSES (SKS = 20, di bawah batas 24)
    # --------------------------------------------------
    student_sukses = {'nim': '2411102441302', 'nama': 'Muhammad Iqbal', 'sks': 20}
    LOGGER.info("\n=== UJI COBA 1: REGISTRASI SUKSES ===")
    reg_service.register(student_sukses)
    
    # --------------------------------------------------
    # UJI SKENARIO 2: GAGAL (SKS = 30, MELEBIHI batas 24)
    # --------------------------------------------------
    student_gagal = {'nim': '2023000', 'nama': 'Budi Gagal', 'sks': 30}
    LOGGER.info("\n=== UJI COBA 2: REGISTRASI GAGAL ===")
    reg_service.register(student_gagal)

if __name__ == "__main__":
    run_registration_app()