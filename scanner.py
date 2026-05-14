print("===== Vulnerability Scanner =====")

print("""
1. Port Scanner
2. Website Security Scanner
""")

choice = input("Enter choice: ")

if choice == "1":
    import port_scanner

elif choice == "2":
    import web_scanner

else:
    print("Invalid Choice")