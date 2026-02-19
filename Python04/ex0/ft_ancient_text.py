def main():
	print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
	try:
		print("Accessing Storage Vault: ancient_fragment.txt\nConnection established...\n")
		with open("ancient_fragment.txt", "r") as file:
			content = file.read()
			print("RECOVERED DATA:")
			print(content)
	except FileNotFoundError:
		print("ERROR: Storage vault not found. Run data generator first.")
	finally:
		print("\nData recovery complete. Storage unit disconnected.")
		file.close()

if __name__ == "__main__":
	main()