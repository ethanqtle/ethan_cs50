def main():
    fileName = input("File name: ")
    print(fileType(fileName))


def fileExt(fileName):
    fileName = fileName.strip().lower()
    if fileName.rfind(".") >= 0:
        return fileName[fileName.rfind(".") :]
    else:
        return ""


def fileType(fileName):
    match fileExt(fileName):
        case ".gif":
            return "image/gif"
        case ".jpg" | ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


if __name__ == "__main__":
    main()
