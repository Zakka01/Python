def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename = "new_discovery.txt"
    data = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    try:
        print(f"Initializing new storage unit: {filename}")
        txtfile = open(filename, "w")

        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        for d in data:
            txtfile.write(f"{d}\n")
            print(d)

        txtfile.close()

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive {filename} ready for long-term preservation.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
