def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "ancient_fragment.txt"

    try:
        print(f"Accessing Storage Vault: {filename}")

        txtfile = open(filename, "r")
        print("Connection established...\n")

        content = txtfile.read()
        print("RECOVERED DATA:")
        print(content)
        txtfile.close()

        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
