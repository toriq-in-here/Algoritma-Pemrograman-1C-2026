Jarak_Sekali_jalan_KM: float = 100.0
Konsumsi_BBM_per_KM: float = 40.0
Sisa_Bensin_Liter: float = 1.5
Harga_Per_Liter: int = 10_000


def hitung_perjalanan(
        jarak_sekali_jalan: float,
        konsumsi: float,
        sisa_bensin: float,
        harga_per_liter: int
) -> dict[str, float]:
    total_jarak = jarak_sekali_jalan * 2
    total_kebutuhan = total_jarak / konsumsi
    bensin_dibeli = max(total_kebutuhan - sisa_bensin, 0.0)
    total_biaya = bensin_dibeli * harga_per_liter

    return {
        "total_jarak": total_jarak,
        "total_kebutuhan": total_kebutuhan,
        "bensin_dibeli": bensin_dibeli,
        "total_biaya": total_biaya
    }


def format_rupiah(nilai: float) -> str:
    return f"Rp {nilai:,.0f}".replace(",", ".")


def main() -> None:
    hasil = hitung_perjalanan(
        Jarak_Sekali_jalan_KM,
        Konsumsi_BBM_per_KM,
        Sisa_Bensin_Liter,
        Harga_Per_Liter
    )

    print(f"Total jarak pulang-pergi   : {hasil['total_jarak']:.0f} KM")
    print(f"Total kebutuhan BBM        : {hasil['total_kebutuhan']:.2f} Liter")
    print(f"Total bensin yang dibeli   : {hasil['bensin_dibeli']:.2f} Liter")
    print(f"Total Biaya                : {format_rupiah(hasil['total_biaya'])}")


main()