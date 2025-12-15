import logging
# Asumsikan IValidationRule diimpor dari file yang sama atau satu level di atas
from IValidationRule import IValidationRule

# Inisialisasi Logger
LOGGER = logging.getLogger('Registration') 

class RegistrationService:
    """Layanan utama (Service Layer) untuk mengelola proses pendaftaran mahasiswa.

    Layanan ini menjalankan semua aturan validasi yang disuntikkan
    saat inisialisasi (Dependency Injection).
    """
    
    def __init__(self, validation_rules: list):
        """Menginisialisasi RegistrationService.

        Args:
            validation_rules (list): Daftar objek IValidationRule yang akan digunakan.
        """
        self.rules = validation_rules
        LOGGER.info("RegistrationService berhasil diinisialisasi.")

    def register(self, student_data: dict) -> bool:
        """Melakukan proses pendaftaran mahasiswa.
        
        Akan menjalankan semua aturan validasi sebelum mencatat data.

        Args:
            student_data (dict): Data mahasiswa yang akan didaftarkan.

        Returns:
            bool: True jika registrasi sukses, False jika gagal.
        """
        # logging.INFO: Menandai awal proses
        LOGGER.info(f"Memulai proses registrasi untuk NIM: {student_data.get('nim')}")

        for rule in self.rules:
            if not rule.is_valid(student_data):
                # logging.ERROR: Jika ada rule yang gagal
                LOGGER.error("Registrasi dibatalkan: Gagal memenuhi salah satu aturan validasi.")
                return False

        # Asumsi: Logika penyimpanan data ke database di sini
        
        # logging.INFO: Menandai sukses
        LOGGER.info(f"Registrasi SUKSES! Mahasiswa {student_data.get('nim')} telah didaftarkan.")
        return True