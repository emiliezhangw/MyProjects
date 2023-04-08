answer = input("File name: ").strip().lower()
#answer = input("File name: ").strip().endwith()

if "." in answer:
    answer = answer.rsplit('.', 1)[1]
    match answer:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "gif" | "png":
            print(f"image/{answer}")
        case "pdf" | "zip":
            print(f"application/{answer}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
