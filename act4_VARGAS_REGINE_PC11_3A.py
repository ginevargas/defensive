# 1a. Unicode Encoding Decorator
def encode_utf8(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.encode('utf-8')
        return result
    return wrapper

# 1b. Unicode Decoding Decorator
# code goes here
def decode_utf8(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, bytes):
            return result.decode('utf-8')
        return result
    return wrapper

# 2a. Read and Encode File Function with decorator(1b)
# code goes here
@decode_utf8
def read_and_encode_file(file_path):
    try:
        with open(file_path, 'rb')  as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
# 3a. Write UTF-8 File Decorator
def write_utf8_file(func):
    def wrapper(file_path, text):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    return wrapper

# 3b-c. Decode and Write File Function with decorator(3a)
@write_utf8_file
def decode_and_write_file(file_path, text):
    return text

# 2c. Test the Read and Encode File Function
encoded_content = read_and_encode_file('sample_text.txt')
print("Encoded Content:")
print(encoded_content)

# 3d. Test the Decode and Write File Function
text_to_write = "This is a sample text with Unicode characters: é, ñ, and ö."
decode_and_write_file('output.txt', text_to_write)
print("\nText written to output.txt with UTF-8 encoding.")
