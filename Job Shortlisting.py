
def main():
    MIN_AGE = 21
    REQUIRED_QUALIFICATION = "Bachelor"
    MIN_EXPERIENCE = 2
    num_candidates = int(input("Enter the number of candidates: "))
    shortlisted = 0
    rejected = 0

    for i in range(1, num_candidates + 1):
        print(f"\nEnter details for Candidate {i}:")
        name = input("Name: ")
        age = int(input("Age: "))
        qualification = input("Qualification: ")
        experience = int(input("Years of Experience: "))
        if age >= MIN_AGE and qualification.lower() == REQUIRED_QUALIFICATION.lower() and experience >= MIN_EXPERIENCE:
            print(f"{name} is Shortlisted.")
            shortlisted += 1
        else:
            print(f"{name} is Rejected.")
            rejected += 1
    print("\nSummary:")
    print(f"Shortlisted Candidates: {shortlisted}")
    print(f"Rejected Candidates: {rejected}")
if __name__ == "__main__":
    main()