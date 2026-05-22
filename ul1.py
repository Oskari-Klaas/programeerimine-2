class Diary:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        formatted_entry = f"{self.count}: {text}"
        self.entries.append(formatted_entry)

    def remove_entry(self, index):
        self.entries.pop(index)

    def __str__(self):
        return "\n".join(self.entries)


class DiaryPersistence:
    @staticmethod
    def save_to_file(diary_obj, filename):
        # Grabs the text from the diary object and saves it
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(diary_obj))

    @staticmethod
    def load_from_file(filename):
        # Creates a brand new Diary object
        loaded_diary = Diary()
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            loaded_diary.entries = lines
            # Updates the counter so the next added entry has the correct number
            loaded_diary.count = len(lines)
        return loaded_diary


class DiaryStatistics:
    @staticmethod
    def print_statistics(diary_obj):
        total_entries = len(diary_obj.entries)
        total_characters = 0
        for entry in diary_obj.entries:
            total_characters += len(entry)
            
        # Prevents a crash if the diary is empty (dividing by zero)
        average_length = total_characters / total_entries if total_entries > 0 else 0
        
        print(f"sissekannete arv: {total_entries}")
        print(f"keskmine tähemärkide arv sissekandes: {average_length}")


if __name__ == "__main__":
    
    # Loome Diary objekti
    diary = Diary()
    
    diary.add_entry("Täna oli ilus ilm.")
    diary.add_entry("Õppisin programmeerimist.")
    diary.add_entry("SRP on tegelikult väga loogiline.")
    
    print("---- DIARY SISU ----")
    print(diary)
    print()

    # Statistika (kasutame staticmethod'e)
    print("---- STATISTIKA ----")
    DiaryStatistics.print_statistics(diary)
    print()

    # Salvestame faili (EI loo Persistence objekti)
    filename = "diary.txt"
    DiaryPersistence.save_to_file(diary, filename)
    
    print(f"Salvestatud faili: {filename}")
    print()

    # Laeme uuesti failist
    loaded_diary = DiaryPersistence.load_from_file(filename)
    
    print("---- FAILIST LAETUD ----")
    print(loaded_diary)
    print()

    # Kontrollime, kas loendur töötab edasi
    loaded_diary.add_entry("See lisati pärast laadimist.")
    
    print("---- PÄRAST UUT LISAMIST ----")
    print(loaded_diary)