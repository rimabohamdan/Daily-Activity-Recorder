print('Apply to record daily activities')
print("""
1. Add new activity.
2. View activity.
3. Exit.
""")

activities = []

choice = int(input("Enter your choice: "))
if choice == 1:
    activity_name = input("Enter activity name: ").capitalize()
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    activities.append((activity_name, start_time, end_time))
    print("Activity added successfully!")

elif choice == 2:
    if len(activities) == 0:
        print("No activities recorded yet.")
    else:
        print("Activities:")
        print(f"1. {activities[0][0]} - {activities[0][1]} to {activities[0][2]}")
        # Repeat for other activities if they exist

elif choice == 3:
    print("Exiting...")

else:
    print("Invalid choice. Please enter a valid option.")
  
