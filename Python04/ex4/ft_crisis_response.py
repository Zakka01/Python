def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    for filename in files:
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(f"\nROUTINE ACCESS: Attempting access to '{filename}'")
                print(f"SUCCESS: Archive recovered - ``{content}``")
                print("STATUS: Normal operations resumed")
            print("\nAll crisis scenarios handled successfully. "
                  "Archives secure.")
        except FileNotFoundError:
            print(f"\nCRISIS ALERT: Attempting access to '{filename}'")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print(f"\nCRISIS ALERT: Attempting access to '{filename}'")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    main()
