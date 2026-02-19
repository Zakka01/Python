def main():
	print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
	filename = "new_discovery.txt"
	data = ["[ENTRY 001] New quantum algorithm discovered",
			"[ENTRY 002] Efficiency increased by 347%",
			"[ENTRY 003] Archived by Data Archivist trainee"
	]
	try :
		print("Initializing new storage unit: new_discovery.txt\nStorage unit created successfully...\n")
		print("Inscribing preservation data...")
		if filename == "new_discovery.txt":
			with open(filename, "w") as file:
				for d in data:
					file.write(f"{d}\n")
					print(d)
	except FileNotFoundError :
		print("ERROR: Storage vault not found. Run data generator first.")
	finally:
		print("\nData inscription complete. Storage unit sealed.")
		print(f"Archive {filename} ready for long-term preservation.")

if __name__ == "__main__":
	main()