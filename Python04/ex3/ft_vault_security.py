def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    classified_data = "classified_data.txt"
    security_protocols = "security_protocols.txt"

    try:
        print("Initiating secure vault access...")

        with open(classified_data, "r") as f1:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            extracted1 = f1.read()
            print(extracted1)

        with open(security_protocols, "r") as f2:
            print("\nSECURE PRESERVATION:")
            extracted2 = f2.read()
            print(extracted2)

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
