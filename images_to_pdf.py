import argparse
from PIL import Image
import os

def images_to_pdf(folder, output_pdf="output.pdf"):
    # 画像ファイルを集める
    files = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    files.sort()  # ファイル名順にソート

    if not files:
        print("画像ファイルが見つかりません")
        return

    images = []
    for file in files:
        path = os.path.join(folder, file)
        img = Image.open(path).convert("RGB")  # PDF用にRGB変換
        images.append(img)

    # 最初の画像を基準にPDF保存、残りはappend
    first_image, rest = images[0], images[1:]
    first_image.save(output_pdf, save_all=True, append_images=rest)
    print(f"PDFを作成しました: {output_pdf}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="画像をまとめてPDFに変換するツール")
    parser.add_argument("folder", help="画像フォルダのパス (例: ./images/)")
    parser.add_argument("-o", "--output", default="merged.pdf", help="出力するPDFファイル名 (デフォルト: merged.pdf)")
    args = parser.parse_args()

    images_to_pdf(args.folder, args.output)
