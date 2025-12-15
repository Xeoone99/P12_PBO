import logging
from abc import ABC, abstractmethod

# Inisialisasi Logger
LOGGER = logging.getLogger('Registration') 
# Nama 'Registration' akan digunakan konsisten di semua file.

class IValidationRule(ABC):
    """Interface (Abstraction) untuk aturan validasi pendaftaran mahasiswa.
    
    Rule ini digunakan untuk memisahkan aturan bisnis pendaftaran
    dari proses utamanya (Prinsip Dependency Inversion/DIP).
    """

    @abstractmethod
    def is_valid(self, student_data: dict) -> bool:
        """Memvalidasi data mahasiswa berdasarkan aturan tertentu.

        Args:
            student_data (dict): Objek data mahasiswa yang akan divalidasi.
                                 Contoh: {'nim': '123', 'nama': 'Budi', 'sks': 25}.

        Returns:
            bool: True jika validasi berhasil, False jika gagal.
        """
        pass

class SKSLimitRule(IValidationRule):
    """Rule yang memastikan SKS yang diambil mahasiswa tidak melebihi 24 SKS.
    
    Digunakan untuk menjaga batas maksimal beban studi.
    """
    
    def is_valid(self, student_data: dict) -> bool:
        """Memvalidasi batas maksimal SKS (Maks 24 SKS).

        Args:
            student_data (dict): Data mahasiswa, harus mengandung kunci 'sks'.

        Returns:
            bool: True jika SKS <= 24, False jika SKS > 24.
        """
        if student_data.get('sks', 0) > 24:
            # Menggunakan logging.WARNING untuk kegagalan validasi
            LOGGER.warning(
                f"Validasi GAGAL: {student_data.get('nim')} melebihi batas SKS (SKS: {student_data.get('sks')})."
            )
            return False
        
        # Menggunakan logging.INFO untuk sukses validasi
        LOGGER.info(
            f"Validasi SKS SUKSES untuk {student_data.get('nim')}."
        )
        return True