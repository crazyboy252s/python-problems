def count_vowels(text: str) -> int:
  vowels = set("aeiou")
  count = 0
  for ch in text.lower():
    if ch in vowels:
      count += 1
  return count


def main() -> None:
  letters = input("Enter the letters all at once: ").strip()
  vowel_count = count_vowels(letters)
  print(f"Total vowels: {vowel_count}")


if __name__ == "__main__":
  main()